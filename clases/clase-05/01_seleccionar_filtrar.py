"""
01_seleccionar_filtrar.py  ·  Clase 5 · Bloque 1
====================================================================
OBJETIVO: aprender a quedarse SOLO con las filas y columnas que importan.

Lo que demuestra este script, paso a paso:
  1. Seleccionar una columna y varias columnas.
  2. Seleccionar por nombre (.loc) y por posición (.iloc).
  3. Filtrar con una "máscara" booleana (preguntas Sí/No por fila).
  4. Combinar condiciones con & (y) y | (o), con paréntesis.
  5. Lo mismo, más legible, con .query().

Cómo correrlo:
    python 01_seleccionar_filtrar.py
====================================================================
"""

import logging
import pandas as pd

# Importamos el generador de datos de ejemplo (vive al lado de este script).
from _datos_demo import tabla_pedidos

logging.basicConfig(level=logging.INFO, format="%(message)s")


def cargar_pedidos() -> pd.DataFrame:
    """
    Carga los pedidos. En un proyecto real leeríamos el CSV de Olist;
    aquí, para que la clase corra siempre, usamos datos de ejemplo y
    convertimos 'price' a número (en la Clase 5 Bloque 2 vemos por qué).
    """
    df = tabla_pedidos()
    # 'price' viene como texto en el ejemplo: lo pasamos a número para poder comparar.
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df


def main() -> None:
    df = cargar_pedidos()

    # ---- Gesto nº1: SIEMPRE mirar el dato antes de tocarlo -------------------
    logging.info("=== 0) Mirar primero ===")
    logging.info(f"Forma de la tabla (filas, columnas): {df.shape}")
    logging.info("Primeras 3 filas:\n%s\n", df.head(3).to_string(index=False))

    # ---- 1) Seleccionar columnas -------------------------------------------
    logging.info("=== 1) Seleccionar columnas ===")
    una_columna = df["price"]                       # una columna -> Serie
    varias = df[["order_id", "price", "city"]]      # varias -> DataFrame (¡lista!)
    logging.info("Solo 'price' (primeros 3):\n%s", una_columna.head(3).to_string(index=False))
    logging.info("3 columnas (primeras 2 filas):\n%s\n", varias.head(2).to_string(index=False))

    # ---- 2) .loc (por nombre) vs .iloc (por posición) ----------------------
    logging.info("=== 2) .loc (nombre) vs .iloc (posición) ===")
    logging.info("df.loc['price']  -> %s", df.loc[0, "price"])
    logging.info("df.iloc[0, 2]       -> %s  (misma celda, por posición)\n", df.iloc[0, 2])

    # ---- 3) Filtrar con una MÁSCARA ----------------------------------------
    logging.info("=== 3) Filtrar con una máscara (Sí/No por fila) ===")
    mascara_caro = df["price"] > 100        # esto NO filtra: arma la lista de Sí/No
    logging.info("La máscara es una columna de True/False:\n%s", mascara_caro.head(3).to_string(index=False))
    caros = df[mascara_caro]                # AHORA sí filtramos
    logging.info("Pedidos con price > 100: %d de %d filas\n", len(caros), len(df))

    # ---- 4) Combinar condiciones: & (y), | (o) -----------------------------
    logging.info("=== 4) Combinar condiciones con & y | (¡paréntesis!) ===")
    caros_sp = df[(df["price"] > 100) & (df["city"].str.strip().str.lower() == "sao paulo")]
    logging.info("Caros Y de Sao Paulo: %d filas", len(caros_sp))

    # ---- 5) Lo mismo, más legible, con .query() ----------------------------
    logging.info("=== 5) Lo mismo con .query() (se lee casi como una frase) ===")
    df2 = df.copy()
    df2["city"] = df2["city"].str.strip().str.lower()   # normalizamos para comparar
    caros_sp_query = df2.query("price > 100 and city == 'sao paulo'")
    logging.info("Con .query(): %d filas (mismo resultado)\n", len(caros_sp_query))

    logging.info("Listo ✅  Filtrar = preguntarle a la tabla y quedarse con los 'Sí'.")


if __name__ == "__main__":
    main()
