"""
DPL1046 · Clase 2 · 03d_sets.py
SETS  { }  — sin repetidos, sin orden.
Idea: ¿qué estados distintos existen? ¿qué órdenes no tienen reseña?

Córrelo con el botón ▶ o con:
    python clases/clase-02/material/03d_sets.py
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

todas = set(orders["order_id"])      # todas
con_resena = set(reviews["order_id"])  # con reseña
sin_resena = todas - con_resena      # resta

print("Sin reseña:", len(sin_resena))
