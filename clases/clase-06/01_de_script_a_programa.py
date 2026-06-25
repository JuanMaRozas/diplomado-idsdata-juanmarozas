"""
01_de_script_a_programa.py
==================================================================
BLOQUE 1 — De un script "feo" a un programa serio.

Misma tarea de siempre (cargar -> limpiar -> resumir), pero ahora
con las 3 herramientas que separan a un estudiante de un profesional:

  1) FUNCIONES: el código se parte en bloques con nombre y un solo trabajo.
  2) LOGGING: en vez de print(), usamos un registro con hora y nivel.
  3) CONFIGURACIÓN EXTERNA: los parámetros viven en config.yaml.

Cómo correrlo:
    python 01_de_script_a_programa.py
==================================================================
"""

from pathlib import Path

import pandas as pd
import yaml
from loguru import logger

from _datos_demo import generar_pedidos


# ------------------------------------------------------------------
# 0) Leer la configuración externa (config.yaml)
# ------------------------------------------------------------------
def leer_config(ruta: str = "config.yaml") -> dict:
    """Abre el archivo YAML y lo devuelve como un diccionario de Python."""
    # __file__ es la ruta del script — así funciona sin importar desde dónde lo corras
    base = Path(__file__).parent
    with open(base / ruta, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------------
# 1) Cargar los datos (cada función hace UNA sola cosa)
# ------------------------------------------------------------------
def cargar(n_pedidos: int) -> pd.DataFrame:
    logger.info(f"Cargando {n_pedidos} pedidos de ejemplo...")
    df = generar_pedidos(n_pedidos)
    logger.info(f"Cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df


# ------------------------------------------------------------------
# 2) Limpiar (lo que aprendimos en la Clase 5, ahora en una función)
# ------------------------------------------------------------------
def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Limpiando datos...")

    nulos_antes = df["price"].isna().sum()
    # precio: de texto a número (lo que no se pueda, queda nulo)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    # los precios que faltan: los descartamos (decisión de negocio)
    df = df.dropna(subset=["price"]).copy()  # .copy() evita SettingWithCopyWarning
    logger.warning(f"Descartadas {nulos_antes} filas sin precio")

    # ciudad: a minúsculas y sin espacios sobrantes
    df["city"] = df["city"].str.strip().str.lower()

    logger.info(f"Datos limpios: {df.shape[0]} filas quedaron")
    return df


# ------------------------------------------------------------------
# 3) Resumir según las reglas de negocio (vienen de la config)
# ------------------------------------------------------------------
def resumir(df: pd.DataFrame, umbral_caro: int) -> pd.DataFrame:
    logger.info(f"Resumiendo por categoría (umbral caro = {umbral_caro})...")
    df["es_caro"] = df["price"] > umbral_caro
    resumen = (
        df.groupby("categoria")
          .agg(pedidos=("order_id", "count"),
               precio_promedio=("price", "mean"),
               caros=("es_caro", "sum"))
          .round(2)
          .sort_values("pedidos", ascending=False)
    )
    return resumen


def main():
    logger.info("=== INICIO del programa ===")
    cfg = leer_config()

    df = cargar(cfg["entrada"]["n_pedidos"])
    df = limpiar(df)
    resumen = resumir(df, cfg["reglas_negocio"]["umbral_caro"])

    print("\nRESUMEN POR CATEGORÍA")
    print(resumen)

    logger.success("=== FIN del programa (todo OK) ===")


if __name__ == "__main__":
    main()
