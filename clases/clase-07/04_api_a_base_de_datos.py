"""
04_api_a_base_de_datos.py  ·  Clase 7 · Bloque 2  ·  INTEGRADOR (APIs reales)
-----------------------------------------------------------------------------
El pipeline completo, end-to-end, contra APIs reales:

   EXTRAER (API real)  ->  TRANSFORMAR (pandas)  ->  CARGAR (base de datos)

1) Pide dólar + UF a mindicador.cl (reutilizando indicadores.py).
2) Los combina y valida con pandas.
3) Los GUARDA en una base de datos SQLite (un archivo .db, sin servidor).
4) Evita duplicados (idempotencia, Clase 6): si una fecha ya está, no la repite.
   -> Corre el script DOS veces: la 2ª no inserta nada.
5) Consulta la base con SQL, usando parámetros seguros (sin inyección).

SQLite = base "de bolsillo" (un archivo). En la industria se usa PostgreSQL
(un servidor), pero el código de SQLAlchemy es casi idéntico: cambia una sola
línea (la dirección de conexión, ver BD).
"""

import pandas as pd
from loguru import logger
from sqlalchemy import create_engine, text, inspect
from indicadores import pedir_indicador, a_tabla    # <- REUTILIZAMOS el módulo

BD = "sqlite:///indicadores.db"          # PostgreSQL: "postgresql://user:clave@host/bd"
TABLA = "indicadores"


# ---------- TRANSFORMAR ----------
def construir_tabla():
    dolar = a_tabla(pedir_indicador("dolar"), "dolar_clp")
    uf = a_tabla(pedir_indicador("uf"), "uf_clp")
    df = pd.merge(dolar, uf, on="fecha", how="inner").sort_values("fecha")
    df["fecha"] = df["fecha"].astype(str)          # SQLite guarda la fecha como texto
    # Contrato de datos mínimo (idea de la Clase 6): nada nulo, nada negativo
    assert df["dolar_clp"].notna().all(), "Hay dólar nulo"
    assert (df["dolar_clp"] > 0).all(), "Hay dólar <= 0"
    return df.reset_index(drop=True)


# ---------- CARGAR ----------
def fechas_ya_guardadas(engine):
    """Devuelve el set de fechas que ya existen en la base (para no duplicar)."""
    if TABLA not in inspect(engine).get_table_names():
        return set()
    return set(pd.read_sql(f"SELECT fecha FROM {TABLA}", engine)["fecha"])


def guardar(df, engine):
    """Guarda SOLO las filas cuyas fechas aún no están en la base (idempotencia)."""
    ya = fechas_ya_guardadas(engine)
    nuevas = df[~df["fecha"].isin(ya)]
    if nuevas.empty:
        logger.info("La base ya estaba al día: 0 filas nuevas (idempotente).")
        return 0
    nuevas.to_sql(TABLA, engine, if_exists="append", index=False)
    logger.success(f"Insertadas {len(nuevas)} filas nuevas en la base.")
    return len(nuevas)


# ---------- CONSULTAR (con SQL seguro) ----------
def consultar_sobre(engine, umbral):
    """Días en que el dólar superó un umbral. Usa parámetro :u (sin inyección)."""
    consulta = text(f"SELECT fecha, dolar_clp FROM {TABLA} "
                    f"WHERE dolar_clp > :u ORDER BY dolar_clp DESC")
    return pd.read_sql(consulta, engine, params={"u": umbral})


def main():
    logger.info("====== ETL: API real -> pandas -> base de datos ======")
    engine = create_engine(BD)

    df = construir_tabla()
    logger.info(f"Tabla construida y validada: {df.shape[0]} filas.")

    guardar(df, engine)

    total = pd.read_sql(f"SELECT COUNT(*) AS n FROM {TABLA}", engine)["n"][0]
    logger.info(f"La base ahora tiene {total} filas en total.")

    umbral = 950
    print(f"\n=== Consulta SQL: días con dólar sobre ${umbral} ===")
    print(consultar_sobre(engine, umbral).to_string(index=False))

    logger.success("====== ETL: FIN ======")


if __name__ == "__main__":
    main()
