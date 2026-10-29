"""
DPL1046 · Clase 6 (opcional) · 99_opcional_carga_repetible.py
Cargar a la base de datos SIN duplicar: correr dos veces = mismo resultado.

Córrelo con el botón ▶ o con:
    python clases/clase-06/material/99_opcional_carga_repetible.py
"""

import sqlite3
import pandas as pd

RUTA = "data/raw/"
pagos = pd.read_csv(RUTA + "olist_order_payments_dataset.csv")
conexion = sqlite3.connect("data/curso.db")


def contar_filas():
    """Cuenta las filas que hay hoy en la tabla 'pagos'."""
    return pd.read_sql_query("SELECT COUNT(*) AS n FROM pagos", conexion)["n"][0]


# 1) Partimos de cero
pagos.to_sql("pagos", conexion, if_exists="replace", index=False)
print("Primera carga:", contar_filas())

# 2) Mala idea: append agrega OTRA copia de todo
pagos.to_sql("pagos", conexion, if_exists="append", index=False)
print("Con append (duplica):", contar_filas())

# 3) Buena idea: replace deja siempre el mismo resultado
pagos.to_sql("pagos", conexion, if_exists="replace", index=False)
print("Con replace (no duplica):", contar_filas())

conexion.close()
