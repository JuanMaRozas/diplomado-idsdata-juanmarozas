"""
DPL1046 · Clase 4 · 01_csv.py
Leer un archivo CSV con pandas: completo, y de forma "liviana".

Córrelo con el botón ▶ o con:
    python clases/clase-04/material/01_csv.py
"""

import pandas as pd

RUTA = "data/raw/"

# 1) Lectura simple: toda la tabla
pagos = pd.read_csv(RUTA + "olist_order_payments_dataset.csv")
print("Filas y columnas:", pagos.shape)
print("Columnas:", list(pagos.columns))
print(pagos.head(3))

# 2) Lectura liviana: solo 2 columnas y solo 5 filas
liviana = pd.read_csv(
    RUTA + "olist_order_payments_dataset.csv",
    usecols=["order_id", "payment_value"],
    nrows=5,
)
print(liviana)

# Si un archivo usa punto y coma (frecuente en Chile), se agrega sep=";"
# pd.read_csv("archivo.csv", sep=";")
