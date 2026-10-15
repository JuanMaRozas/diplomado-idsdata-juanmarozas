"""
DPL1046 · Clase 2 · 03a_leer_datos.py
---------------------------------------------------------------------------
Un script es una receta: Python la lee de ARRIBA hacia ABAJO, línea por línea.

Cómo correrlo (con el archivo abierto en VS Code):
    - Haz clic en el botón ▶ de arriba a la derecha, o
    - escribe en la terminal (en la raíz del repo, con (.venv) activo):
          python clases/clase-02/material/03a_leer_datos.py

Todo lo que empieza con # es un comentario: Python lo ignora,
es una explicación para ti.
---------------------------------------------------------------------------
"""

import pandas as pd   # trae la herramienta pandas

# Una variable guarda un valor:  nombre = valor
RUTA = "data/raw/"   # texto guardado en una variable

# Leemos dos tablas de Olist.
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
reviews = pd.read_csv(
    RUTA + "olist_order_reviews_dataset.csv")

print("Filas en orders:", len(orders))
print("Filas en reviews:", len(reviews))
