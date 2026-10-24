"""
DPL1046 · Clase 5 · 02_seleccionar_filtrar.py
Elegir columnas, filtrar filas y ordenar.

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/02_seleccionar_filtrar.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
items = pd.read_csv(RUTA + "olist_order_items_dataset.csv")

# 1) Elegir columnas: una lista dentro de corchetes
dos_columnas = orders[["order_id", "order_status"]]
print(dos_columnas.head(3))

# 2) Filtrar filas: una condición dentro de corchetes
cancelados = orders[orders["order_status"] == "canceled"]
print("Pedidos cancelados:", len(cancelados))

# 3) Dos condiciones a la vez: cada una entre paréntesis, unidas con &
caros = items[(items["price"] > 500) & (items["freight_value"] > 50)]
print("Ítems caros con flete alto:", len(caros))

# 4) Ordenar de mayor a menor y quedarse con los 3 primeros
top3 = items.sort_values("price", ascending=False).head(3)
print(top3[["order_id", "price"]])

# 5) Una fila por su posición
print(orders.iloc[0])
