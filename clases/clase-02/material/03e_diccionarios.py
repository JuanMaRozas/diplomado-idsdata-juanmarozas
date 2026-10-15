"""
DPL1046 · Clase 2 · 03e_diccionarios.py
DICCIONARIOS  { clave: valor }  — como una libreta de contactos.
Idea: traducir los estados al español, y describir una orden.

Córrelo con el botón ▶ o con:
    python clases/clase-02/material/03e_diccionarios.py
"""

import pandas as pd

RUTA = "data/raw/"
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")

ids = orders["order_id"].tolist()
estado_orden = orders["order_status"].tolist()

traduccion = {
    "delivered": "Entregado",
    "shipped": "Enviado",
    "canceled": "Cancelado",
}

print("El diccionario:", traduccion)
print("delivered:", traduccion["delivered"])
print("invoiced:",
      traduccion.get("invoiced", "no lo tengo"))

traduccion["processing"] = "En proceso"   # pareja nueva
print("Ahora:", traduccion)

orden = {"id": ids[0], "estado": estado_orden[0]}
print("Una orden:", orden)
print("En español:", traduccion[orden["estado"]])
