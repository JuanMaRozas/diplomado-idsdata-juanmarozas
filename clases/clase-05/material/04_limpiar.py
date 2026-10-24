"""
DPL1046 · Clase 5 · 04_limpiar.py
Limpiar datos: valores vacíos y filas repetidas.

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/04_limpiar.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
reviews = pd.read_csv(RUTA + "olist_order_reviews_dataset.csv")
products = pd.read_csv(RUTA + "olist_products_dataset.csv")

# 1) Contar los valores vacíos de cada columna
print(orders.isna().sum())

# 2) Quitar las filas donde falta la fecha de entrega
entregados = orders.dropna(subset=["order_delivered_customer_date"])
print("Antes:", len(orders), "· Después:", len(entregados))

# 3) Contar filas repetidas (mismo order_id) y quitarlas
repetidas = reviews.duplicated(subset="order_id").sum()
print("Reseñas repetidas:", repetidas)
reviews_limpias = reviews.drop_duplicates(subset="order_id")
print("Reseñas antes:", len(reviews), "· después:", len(reviews_limpias))

# 4) Rellenar vacíos con un valor
categoria = products["product_category_name"].fillna("sin_categoria")
print("Productos sin categoría:", (categoria == "sin_categoria").sum())
