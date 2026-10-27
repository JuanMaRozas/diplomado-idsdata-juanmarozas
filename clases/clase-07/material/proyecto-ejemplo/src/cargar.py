"""
src/cargar.py · Carga a base de datos con idempotencia
------------------------------------------------------
Guarda ventas semanales y pronóstico en SQLite.
Si una semana ya existe, NO la duplica (idempotencia).
"""

import pandas as pd
from loguru import logger
from sqlalchemy import create_engine, text, inspect


def _semanas_existentes(engine, tabla):
    """Devuelve el set de semanas ya guardadas en una tabla."""
    if tabla not in inspect(engine).get_table_names():
        return set()
    return set(pd.read_sql(f"SELECT semana FROM {tabla}", engine)["semana"])


def guardar_en_base(ventas_semana, pronostico, uri_base):
    """Guarda ventas y pronóstico en SQLite, sin duplicar semanas existentes."""
    engine = create_engine(uri_base)
    total_nuevas = 0

    # Guardar ventas históricas
    ya = _semanas_existentes(engine, "ventas_semana")
    nuevas = ventas_semana[~ventas_semana["semana"].isin(ya)]
    if not nuevas.empty:
        nuevas.to_sql("ventas_semana", engine, if_exists="append", index=False)
        total_nuevas += len(nuevas)
        logger.info(f"ventas_semana: +{len(nuevas)} semanas nuevas.")
    else:
        logger.info("ventas_semana: al día (0 nuevas, idempotente).")

    # Guardar pronóstico (reemplazar siempre — es una estimación que cambia)
    pronostico.to_sql("pronostico", engine, if_exists="replace", index=False)
    logger.info(f"pronostico: reescrito con {len(pronostico)} semanas.")

    return total_nuevas


def consultar_resumen(uri_base):
    """Consulta SQL para generar un resumen ejecutivo desde la base."""
    engine = create_engine(uri_base)
    consulta = text("""
        SELECT
            'histórico' AS tipo,
            COUNT(*) AS semanas,
            CAST(SUM(ventas_clp) AS INTEGER) AS total_clp,
            CAST(AVG(ventas_clp) AS INTEGER) AS promedio_semanal_clp,
            CAST(MAX(ventas_clp) AS INTEGER) AS maximo_semanal_clp
        FROM ventas_semana
        UNION ALL
        SELECT
            'pronóstico',
            COUNT(*),
            CAST(SUM(ventas_clp_estimado) AS INTEGER),
            CAST(AVG(ventas_clp_estimado) AS INTEGER),
            CAST(MAX(ventas_clp_estimado) AS INTEGER)
        FROM pronostico
    """)
    return pd.read_sql(consulta, engine)


if __name__ == "__main__":
    print("Este módulo se usa desde pipeline.py")
