"""
DPL1046 · Clase 7 · 01_funciones.py
Funciones: una receta con nombre que puedes usar muchas veces.

Córrelo con el botón ▶ o con:
    python clases/clase-07/material/01_funciones.py
"""

import pandas as pd

RUTA = "data/raw/"


def calcular_dias(compra, entrega):
    """Devuelve los días que pasan entre dos fechas (escritas como texto)."""
    dias = (pd.to_datetime(entrega) - pd.to_datetime(compra)).days
    return dias


def cargar_tabla(nombre, ruta=RUTA):
    """Lee una tabla CSV de la carpeta de datos y la devuelve."""
    return pd.read_csv(ruta + nombre)


# Usar una función: su nombre, y entre paréntesis lo que necesita
dias = calcular_dias("2017-10-02 10:56:33", "2017-10-10 21:25:13")
print("Días entre las dos fechas:", dias)

# La misma función, con otros datos: ahí está la ventaja
print("Otro pedido:", calcular_dias("2018-07-24", "2018-08-07"))

# Funciones que leen datos
orders = cargar_tabla("olist_orders_dataset.csv")
items = cargar_tabla("olist_order_items_dataset.csv")
print("orders:", orders.shape, "· items:", items.shape)
