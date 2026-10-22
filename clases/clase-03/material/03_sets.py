"""
DPL1046 · Clase 3 · 03_sets.py
SETS  { }  — sin repetidos, sin orden.
Idea: ¿qué estados distintos existen? ¿qué órdenes no tienen reseña?

Córrelo con el botón ▶ o con:
    python clases/clase-03/material/03_sets.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
reviews = pd.read_csv(
    RUTA + "olist_order_reviews_dataset.csv")

estado_orden = orders["order_status"].tolist()
print("Con repetidos:", len(estado_orden))

estados_unicos = set(estado_orden)  # sin repetidos
print("Distintos:", estados_unicos)
print("Cuántos:", len(estados_unicos))

todas_1 = orders["order_id"]
todas = set(orders["order_id"])

print(len(todas_1))
print(len(todas))

con_resena_1 = reviews["order_id"]     # todas
con_resena = set(reviews["order_id"])  

print(len(con_resena_1))
print(len(con_resena))

# con reseña
sin_resena = todas - con_resena      # resta

print("Sin reseña:", len(sin_resena))
