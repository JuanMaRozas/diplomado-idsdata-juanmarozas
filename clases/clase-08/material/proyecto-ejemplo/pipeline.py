"""
DPL1046 · Clase 8 · pipeline.py  (proyecto integrador de ejemplo)

Pregunta de negocio:
    ¿Cuánto vamos a vender en las próximas semanas y qué meses venden más?

El pipeline tiene 3 pasos (como una cocina):
    1) EXTRAER     -> traer los datos: CSV de Olist + el dólar desde una API
    2) TRANSFORMAR -> limpiar, combinar y resumir (ventas por semana y por mes) y pronosticar
    3) CARGAR      -> guardar los resultados en una base SQLite y en archivos CSV

Córrelo desde la raíz del repo, con el entorno activo:
    python clases/clase-08/material/proyecto-ejemplo/pipeline.py

Los tests se ejecutan con:
    pytest clases/clase-08/material/proyecto-ejemplo/ -v
"""

import logging
import os
import sqlite3

import pandas as pd
import requests

# ---------------------------------------------------------------
# Parámetros del proyecto (los que podrías cambiar sin tocar la lógica)
# ---------------------------------------------------------------
RUTA_DATOS = "data/raw/"
CARPETA_SALIDA = "salida/"
SEMANAS_A_PRONOSTICAR = 8
REAL_EN_DOLARES = 0.19       # 1 real brasileño vale más o menos 0,19 dólares
REAL_EN_CLP_RESPALDO = 180   # si la API falla, usamos este valor


# ===============================================================
# PASO 1 · EXTRAER
# ===============================================================
def extraer_olist():
    """Lee los dos CSV de Olist que necesitamos: pedidos e ítems."""
    pedidos = pd.read_csv(RUTA_DATOS + "olist_orders_dataset.csv")
    items = pd.read_csv(RUTA_DATOS + "olist_order_items_dataset.csv")
    logging.info("Olist leído: %s pedidos y %s ítems", len(pedidos), len(items))
    return pedidos, items


def extraer_dolar():
    """Pide a una API (mindicador.cl) el dólar y lo convierte a pesos por real."""
    try:
        respuesta = requests.get("https://mindicador.cl/api/dolar", timeout=10)
        respuesta.raise_for_status()
        dolar_en_clp = respuesta.json()["serie"][0]["valor"]
        real_en_clp = dolar_en_clp * REAL_EN_DOLARES
        logging.info("Dólar de la API: %s CLP -> 1 real = %.1f CLP", dolar_en_clp, real_en_clp)
        return real_en_clp
    except requests.RequestException:
        logging.warning("La API del dólar no respondió: uso el valor de respaldo (%s)", REAL_EN_CLP_RESPALDO)
        return REAL_EN_CLP_RESPALDO


# ===============================================================
# PASO 2 · TRANSFORMAR
# ===============================================================
def calcular_ventas_semanales(pedidos, items, real_en_clp):
    """Ventas en pesos chilenos por semana, solo de pedidos entregados."""
    # Limpiar: nos quedamos con los pedidos entregados
    entregados = pedidos[pedidos["order_status"] == "delivered"]

    # Combinar: cada ítem con la fecha de su pedido
    tabla = items.merge(entregados, on="order_id", how="inner")

    # Columnas nuevas: ventas en pesos y semana (la fecha del lunes)
    tabla["ventas_clp"] = tabla["price"] * real_en_clp
    fecha = pd.to_datetime(tabla["order_purchase_timestamp"])
    tabla["semana"] = fecha.dt.to_period("W").dt.start_time.dt.strftime("%Y-%m-%d")

    # Resumir: sumar las ventas de cada semana
    semanales = tabla.groupby("semana")["ventas_clp"].sum().round(0).reset_index()
    return semanales


def calcular_ventas_mensuales(ventas_semanales):
    """Promedio semanal de cada mes del año (1 = enero ... 12 = diciembre).

    El índice compara cada mes con el promedio general:
    1,50 significa que ese mes vende un 50% más que una semana normal.
    """
    tabla = ventas_semanales.copy()
    tabla["mes"] = pd.to_datetime(tabla["semana"]).dt.month

    mensuales = tabla.groupby("mes")["ventas_clp"].mean().round(0).reset_index()
    mensuales = mensuales.rename(columns={"ventas_clp": "promedio_semanal_clp"})
    mensuales["indice"] = (mensuales["promedio_semanal_clp"] / tabla["ventas_clp"].mean()).round(2)
    return mensuales


def pronosticar(ventas_semanales, semanas=SEMANAS_A_PRONOSTICAR):
    """Pronóstico simple: repite el promedio de las últimas 4 semanas."""
    promedio = ventas_semanales["ventas_clp"].tail(4).mean()
    ultima_semana = pd.to_datetime(ventas_semanales["semana"]).max()

    fechas = []
    for i in range(1, semanas + 1):
        fecha = ultima_semana + pd.Timedelta(weeks=i)
        fechas.append(fecha.strftime("%Y-%m-%d"))

    return pd.DataFrame({"semana": fechas, "ventas_clp_estimado": round(promedio)})


# ===============================================================
# PASO 3 · CARGAR
# ===============================================================
def cargar(tablas, carpeta):
    """Guarda cada tabla en SQLite y en un CSV.

    Usa if_exists="replace": si corres el pipeline dos veces, la tabla se
    reescribe y queda igual (no se duplica).
    """
    conexion = sqlite3.connect(carpeta + "demanda.db")
    for nombre, tabla in tablas.items():
        tabla.to_sql(nombre, conexion, if_exists="replace", index=False)
        tabla.to_csv(carpeta + nombre + ".csv", index=False)
        logging.info("Guardada la tabla '%s' (%s filas)", nombre, len(tabla))
    conexion.close()


# ===============================================================
# EL PIPELINE COMPLETO
# ===============================================================
def main():
    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(CARPETA_SALIDA + "pipeline.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    logging.info("Pipeline de demanda: inicio")

    try:
        # 1) EXTRAER
        pedidos, items = extraer_olist()
        real_en_clp = extraer_dolar()
    except FileNotFoundError:
        logging.error("No encontré los CSV de Olist en '%s'. ¿Corriste el pipeline desde la raíz del repo?", RUTA_DATOS)
        return

    # 2) TRANSFORMAR
    ventas_semanales = calcular_ventas_semanales(pedidos, items, real_en_clp)
    # La primera y la última semana suelen estar incompletas: las quitamos
    ventas_semanales = ventas_semanales.iloc[1:-1].reset_index(drop=True)
    ventas_mensuales = calcular_ventas_mensuales(ventas_semanales)
    pronostico = pronosticar(ventas_semanales)

    # 3) CARGAR
    cargar(
        {
            "ventas_semanales": ventas_semanales,
            "ventas_mensuales": ventas_mensuales,
            "pronostico": pronostico,
        },
        CARPETA_SALIDA,
    )

    # Resumen para la gerencia
    mes_fuerte = ventas_mensuales.loc[ventas_mensuales["indice"].idxmax()]
    print()
    print("=== RESUMEN PARA LA GERENCIA ===")
    print("Período analizado:       ", ventas_semanales["semana"].min(), "->", ventas_semanales["semana"].max())
    print("Semanas analizadas:      ", len(ventas_semanales))
    print("Ventas totales (CLP):    ", f"{ventas_semanales['ventas_clp'].sum():,.0f}")
    print("Promedio semanal (CLP):  ", f"{ventas_semanales['ventas_clp'].mean():,.0f}")
    semana_fuerte = ventas_semanales.loc[ventas_semanales["ventas_clp"].idxmax(), "semana"]
    print("Semana más fuerte:       ", semana_fuerte)
    print("Mes que más vende:       ", int(mes_fuerte["mes"]), "(índice", mes_fuerte["indice"], ")")
    print("Pronóstico próximas", SEMANAS_A_PRONOSTICAR, "semanas (CLP):", f"{pronostico['ventas_clp_estimado'].sum():,.0f}")
    logging.info("Pipeline de demanda: terminado")


if __name__ == "__main__":
    main()
