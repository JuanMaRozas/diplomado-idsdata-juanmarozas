"""
DPL1046 · Clase 5 · 05_juntar_todo.py
Juntar lo aprendido para responder una pregunta:
"¿Cuántos días tarda en llegar un pedido entregado?"

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/05_juntar_todo.py
"""

import pandas as pd

RUTA = "data/raw/"

# 1) Leer
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")

# 2) Limpiar: solo pedidos entregados, con fecha de entrega
entregados = orders[orders["order_status"] == "delivered"]
entregados = entregados.dropna(subset=["order_delivered_customer_date"]).copy()

# 3) Crear la columna nueva
compra = pd.to_datetime(entregados["order_purchase_timestamp"])
entrega = pd.to_datetime(entregados["order_delivered_customer_date"])
entregados["dias_entrega"] = (entrega - compra).dt.days

# 4) Responder
print("Pedidos entregados:", len(entregados))
print("Promedio de días:", round(entregados["dias_entrega"].mean(), 1))
print("Mínimo y máximo:", entregados["dias_entrega"].min(), entregados["dias_entrega"].max())
print("Pedidos que tardaron más de 30 días:", (entregados["dias_entrega"] > 30).sum())
