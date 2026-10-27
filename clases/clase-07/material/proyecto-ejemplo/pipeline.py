"""
pipeline.py · Proyecto Integrador de Ejemplo
=============================================
Pronóstico de demanda: serie de tiempo y estacionalidad de ventas
Dataset: Olist (e-commerce brasileño real)

FLUJO:
  1. EXTRAER   → leer CSVs de Olist + tipo de cambio BRL→CLP desde API real
  2. TRANSFORMAR → limpiar, agregar ventas por semana, detectar estacionalidad
  3. CARGAR     → guardar en SQLite sin duplicar (idempotencia)
  4. ANALIZAR   → generar pronóstico y métricas clave
  5. EXPORTAR   → CSV resumen + datos para la presentación

Corre con:  python pipeline.py
"""

import os
import yaml
from loguru import logger
from src.extraer import extraer_olist, extraer_tipo_cambio
from src.transformar import (
    limpiar_y_agregar,
    calcular_estacionalidad,
    generar_pronostico,
)
from src.cargar import guardar_en_base, consultar_resumen


def cargar_config():
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    logger.info("=" * 60)
    logger.info("PIPELINE: Pronóstico de demanda — Olist")
    logger.info("=" * 60)

    config = cargar_config()

    # ──── 1. EXTRAER ────
    logger.info("Paso 1/5: Extrayendo datos de Olist (CSVs) y tipo de cambio (API)...")
    pedidos, items, categorias = extraer_olist(config["datos"]["carpeta"])
    tipo_cambio = extraer_tipo_cambio()
    logger.success(f"Extraídos: {len(pedidos)} pedidos, {len(items)} items, "
                   f"tipo de cambio BRL→CLP: ${tipo_cambio:.1f}")

    # ──── 2. TRANSFORMAR ────
    logger.info("Paso 2/5: Limpiando y agregando ventas por semana...")
    ventas_semana = limpiar_y_agregar(pedidos, items, categorias, tipo_cambio)
    logger.success(f"Serie de tiempo: {len(ventas_semana)} semanas de datos.")

    logger.info("Paso 3/5: Calculando estacionalidad y pronóstico...")
    estacionalidad = calcular_estacionalidad(ventas_semana)
    pronostico = generar_pronostico(ventas_semana, semanas_futuras=config["pronostico"]["semanas"])
    logger.success(f"Pronóstico generado: {len(pronostico)} semanas hacia adelante.")

    # ──── 3. CARGAR ────
    logger.info("Paso 4/5: Guardando en base de datos (idempotente)...")
    bd = config["base_datos"]["uri"]
    n = guardar_en_base(ventas_semana, pronostico, bd)
    logger.success(f"Base de datos actualizada: {n} filas nuevas.")

    # ──── 4. EXPORTAR ────
    logger.info("Paso 5/5: Exportando resumen...")
    carpeta_salida = config["salida"]["carpeta"]
    os.makedirs(carpeta_salida, exist_ok=True)

    ventas_semana.to_csv(f"{carpeta_salida}/ventas_por_semana.csv", index=False)
    estacionalidad.to_csv(f"{carpeta_salida}/estacionalidad.csv", index=False)
    pronostico.to_csv(f"{carpeta_salida}/pronostico.csv", index=False)

    resumen = consultar_resumen(bd)
    resumen.to_csv(f"{carpeta_salida}/resumen_ejecutivo.csv", index=False)

    logger.success(f"Archivos exportados a {carpeta_salida}/")

    # ──── RESUMEN ────
    print("\n" + "=" * 60)
    print("RESUMEN EJECUTIVO")
    print("=" * 60)
    print(f"Período analizado:      {ventas_semana['semana'].min()} → {ventas_semana['semana'].max()}")
    print(f"Total de semanas:       {len(ventas_semana)}")
    print(f"Ventas totales (CLP):   ${ventas_semana['ventas_clp'].sum():,.0f}")
    print(f"Promedio semanal (CLP): ${ventas_semana['ventas_clp'].mean():,.0f}")
    print(f"Semana más fuerte:      {ventas_semana.loc[ventas_semana['ventas_clp'].idxmax(), 'semana']}")
    print(f"Pronóstico próx. {config['pronostico']['semanas']} sem: ${pronostico['ventas_clp_estimado'].sum():,.0f}")
    print(f"Tipo de cambio usado:   1 BRL = ${tipo_cambio:.1f} CLP")
    print("=" * 60)
    logger.success("PIPELINE COMPLETADO.")


if __name__ == "__main__":
    main()
