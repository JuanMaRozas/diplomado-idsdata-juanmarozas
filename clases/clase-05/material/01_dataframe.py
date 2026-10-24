"""
DPL1046 · Clase 5 · 01_dataframe.py
Conocer una tabla de pandas: el DataFrame y sus columnas (Series).

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/01_dataframe.py
"""

import pandas as pd

RUTA = "data/raw/"

# Una tabla completa de pandas se llama DataFrame
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")

print("Filas y columnas:", orders.shape)
print("Nombres de columnas:", list(orders.columns))
print(orders.head(3))

# Cada columna de la tabla es una Series
estados = orders["order_status"]
print("Tipo de la tabla:", type(orders).__name__)
print("Tipo de una columna:", type(estados).__name__)

# Cuántas veces aparece cada valor
print(estados.value_counts())

# Qué tipo de dato tiene cada columna
print(orders.dtypes)
