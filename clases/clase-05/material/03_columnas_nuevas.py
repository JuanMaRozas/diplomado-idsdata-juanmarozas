"""
DPL1046 · Clase 5 · 03_columnas_nuevas.py
Crear columnas nuevas: un cálculo y una fecha.

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/03_columnas_nuevas.py
"""

import pandas as pd

RUTA = "data/raw/"
items = pd.read_csv(RUTA + "olist_order_items_dataset.csv")
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")

# 1) Columna nueva a partir de un cálculo entre columnas
items["total"] = items["price"] + items["freight_value"]
print(items[["price", "freight_value", "total"]].head(3))

# 2) Las fechas llegan como texto: hay que convertirlas
orders["compra"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["entrega"] = pd.to_datetime(orders["order_delivered_customer_date"])

# 3) Restar fechas da una duración; .dt.days la pasa a días
orders["dias_entrega"] = (orders["entrega"] - orders["compra"]).dt.days
print(orders[["compra", "entrega", "dias_entrega"]].head(3))

# 4) Promedio de días (pandas ignora los vacíos)
print("Días promedio de entrega:", round(orders["dias_entrega"].mean(), 1))

# 5) Sacar el mes de una fecha
orders["mes"] = orders["compra"].dt.month
print(orders["mes"].value_counts().sort_index())
