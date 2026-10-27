"""
DPL1046 · Clase 6 · 04_pandas_a_sqlite.py
Guardar una tabla en una base de datos SQLite y consultarla con SQL.

Córrelo con el botón ▶ o con:
    python clases/clase-06/material/04_pandas_a_sqlite.py
"""

import sqlite3
import pandas as pd

RUTA = "data/raw/"
pagos = pd.read_csv(RUTA + "olist_order_payments_dataset.csv")

# 1) Abrir (o crear) la base de datos: es un solo archivo
conexion = sqlite3.connect("data/curso.db")

# 2) Guardar la tabla de pandas dentro de la base
pagos.to_sql("pagos", conexion, if_exists="replace", index=False)
print("Filas guardadas en la tabla 'pagos':", len(pagos))

# 3) Consultar con SQL y recibir una tabla de pandas
consulta = """
    SELECT payment_type, COUNT(*) AS cantidad, ROUND(SUM(payment_value)) AS total
    FROM pagos
    GROUP BY payment_type
    ORDER BY total DESC
"""
resultado = pd.read_sql_query(consulta, conexion)
print(resultado)

# 4) Cerrar la conexión
conexion.close()
