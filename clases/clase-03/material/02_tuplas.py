"""
DPL1046 · Clase 3 · 02_tuplas.py
TUPLAS  ( )  — ordenadas, NO se pueden modificar.
Idea: la "huella" de una orden: su id y su estado, fijos.

Córrelo con el botón ▶ o con:
    python clases/clase-03/material/02_tuplas.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")

ids = orders["order_id"].tolist()    # columna -> lista
estado_orden = orders["order_status"].tolist()

huella = (ids[0], estado_orden[0])   # ( ) = tupla

print("La tupla:", huella)
print("Id:", huella[0])
print("Estado:", huella[1])

# huella[1] = "otro"
# Si quitas el # de arriba, guardas y corres de nuevo,
# Python responde TypeError: una tupla no se puede modificar.
