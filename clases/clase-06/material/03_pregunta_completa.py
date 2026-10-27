"""
DPL1046 · Clase 6 · 03_pregunta_completa.py
Responder una pregunta con 3 tablas:
"¿Cuánto vendió cada estado de Brasil?"

Córrelo con el botón ▶ o con:
    python clases/clase-06/material/03_pregunta_completa.py
"""

import pandas as pd

RUTA = "data/raw/"

# 1) Leer las 3 tablas
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
items = pd.read_csv(RUTA + "olist_order_items_dataset.csv")
clientes = pd.read_csv(RUTA + "olist_customers_dataset.csv")

# 2) Limpiar: solo pedidos entregados
entregados = orders[orders["order_status"] == "delivered"]

# 3) Combinar: ítems + pedidos + clientes
tabla = items.merge(entregados, on="order_id", how="inner")
tabla = tabla.merge(clientes, on="customer_id", how="inner")

# 4) Resumir: ventas por estado
ventas = tabla.groupby("customer_state")["price"].sum()
ventas = ventas.sort_values(ascending=False).round(0)

# 5) Responder y guardar
print("Los 5 estados que más vendieron:")
print(ventas.head(5))
ventas.to_csv("data/ventas_por_estado.csv")
print("Guardado en data/ventas_por_estado.csv")
