"""
src/transformar.py · Transformación y análisis de series de tiempo
-----------------------------------------------------------------
Limpia datos de Olist, agrega ventas por semana, calcula estacionalidad
y genera un pronóstico simple con media móvil.
"""

import numpy as np
import pandas as pd
from loguru import logger


def limpiar_y_agregar(pedidos, items, categorias, tipo_cambio_brl_clp):
    """Transforma datos crudos de Olist en ventas semanales en CLP.

    Pasos:
      1. Filtrar solo pedidos entregados.
      2. Cruzar pedidos con items (merge).
      3. Convertir precios BRL → CLP.
      4. Agregar ventas por semana.
    """
    # 1. Solo pedidos entregados (no cancelados, no en tránsito)
    entregados = pedidos[pedidos["order_status"] == "delivered"].copy()
    entregados["order_purchase_timestamp"] = pd.to_datetime(
        entregados["order_purchase_timestamp"]
    )
    logger.info(f"Pedidos entregados: {len(entregados)} de {len(pedidos)} totales "
                f"({len(entregados)/len(pedidos)*100:.0f}%)")

    # 2. Cruzar con items para obtener precios
    ventas = pd.merge(
        entregados[["order_id", "order_purchase_timestamp"]],
        items[["order_id", "product_id", "price"]],
        on="order_id",
        how="inner",
    )

    # 3. Convertir BRL → CLP
    ventas["precio_clp"] = (ventas["price"] * tipo_cambio_brl_clp).round(0)

    # 4. Agregar por semana (lunes como inicio)
    ventas["semana"] = ventas["order_purchase_timestamp"].dt.to_period("W").dt.start_time
    ventas["semana"] = ventas["semana"].dt.date

    semanal = (
        ventas.groupby("semana")
        .agg(
            n_pedidos=("order_id", "nunique"),
            n_items=("product_id", "count"),
            ventas_clp=("precio_clp", "sum"),
        )
        .reset_index()
        .sort_values("semana")
    )

    # Quitar primera y última semana (pueden estar incompletas)
    semanal = semanal.iloc[1:-1].reset_index(drop=True)
    semanal["semana"] = semanal["semana"].astype(str)

    logger.info(f"Serie de tiempo: {len(semanal)} semanas, "
                f"desde {semanal['semana'].iloc[0]} hasta {semanal['semana'].iloc[-1]}")
    return semanal


def calcular_estacionalidad(ventas_semana):
    """Calcula el patrón de estacionalidad mensual (qué meses venden más).

    Devuelve un DataFrame con 12 filas (una por mes) y el índice de estacionalidad:
      > 1.0 = meses fuertes (sobre el promedio)
      < 1.0 = meses débiles (bajo el promedio)
    """
    df = ventas_semana.copy()
    df["semana"] = pd.to_datetime(df["semana"])
    df["mes"] = df["semana"].dt.month
    df["nombre_mes"] = df["semana"].dt.strftime("%B")

    promedio_global = df["ventas_clp"].mean()
    estacional = (
        df.groupby(["mes", "nombre_mes"])["ventas_clp"]
        .mean()
        .reset_index()
        .sort_values("mes")
    )
    estacional["indice"] = (estacional["ventas_clp"] / promedio_global).round(2)
    estacional = estacional.rename(columns={"ventas_clp": "promedio_mensual_clp"})

    mes_fuerte = estacional.loc[estacional["indice"].idxmax(), "nombre_mes"]
    mes_debil = estacional.loc[estacional["indice"].idxmin(), "nombre_mes"]
    logger.info(f"Estacionalidad: mes más fuerte = {mes_fuerte}, "
                f"mes más débil = {mes_debil}")

    return estacional[["mes", "nombre_mes", "promedio_mensual_clp", "indice"]]


def generar_pronostico(ventas_semana, semanas_futuras=8):
    """Pronóstico simple con media móvil ponderada + estacionalidad.

    No es un modelo sofisticado (ARIMA, Prophet) — es lo que un ingeniero de datos
    puede hacer con pandas en 20 líneas. Para el diplomado, es perfecto.
    """
    df = ventas_semana.copy()
    df["semana"] = pd.to_datetime(df["semana"])

    # Media móvil de las últimas 8 semanas como base
    ventana = min(8, len(df))
    base = df["ventas_clp"].tail(ventana).mean()

    # Tendencia: comparar últimas 4 semanas vs. anteriores 4
    if len(df) >= 8:
        reciente = df["ventas_clp"].tail(4).mean()
        anterior = df["ventas_clp"].iloc[-8:-4].mean()
        tendencia_semanal = (reciente - anterior) / 4
    else:
        tendencia_semanal = 0

    # Generar semanas futuras
    ultima_semana = df["semana"].max()
    futuras = []
    for i in range(1, semanas_futuras + 1):
        semana = ultima_semana + pd.Timedelta(weeks=i)
        estimado = max(0, base + tendencia_semanal * i)
        futuras.append({
            "semana": semana.date(),
            "ventas_clp_estimado": round(estimado),
            "tipo": "pronóstico",
        })

    resultado = pd.DataFrame(futuras)
    resultado["semana"] = resultado["semana"].astype(str)
    logger.info(f"Pronóstico: {semanas_futuras} semanas, "
                f"promedio estimado ${resultado['ventas_clp_estimado'].mean():,.0f} CLP/semana")
    return resultado


if __name__ == "__main__":
    print("Este módulo se usa desde pipeline.py")
