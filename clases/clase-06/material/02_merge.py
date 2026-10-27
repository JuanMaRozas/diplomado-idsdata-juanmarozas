"""
DPL1046 · Clase 6 · 02_merge.py
Combinar dos tablas con una columna en común (merge).

Córrelo con el botón ▶ o con:
    python clases/clase-06/material/02_merge.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
clientes = pd.read_csv(RUTA + "olist_customers_dataset.csv")

print("orders:", orders.shape, "· clientes:", clientes.shape)

# Unimos las dos tablas por la columna que tienen en común: customer_id
pedidos = orders.merge(clientes, on="customer_id", how="left")

print("Después del merge:", pedidos.shape)
print(pedidos[["order_id", "customer_id", "customer_city", "customer_state"]].head(3))

# Con la tabla combinada ya podemos preguntar por estado
print(pedidos["customer_state"].value_counts().head(5))
