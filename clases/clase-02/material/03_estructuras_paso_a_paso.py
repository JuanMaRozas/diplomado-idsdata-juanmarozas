"""
DPL1046 · Clase 2 · 03_estructuras_paso_a_paso.py
---------------------------------------------------------------------------
Un script es una receta: Python la lee de ARRIBA hacia ABAJO, línea por línea.

Este archivo está dividido en PASOS. Puedes correrlo de dos formas:

  A) Completo, desde la terminal (en la raíz del repo, con (.venv) activo):
         python clases/clase-02/material/03_estructuras_paso_a_paso.py

  B) Solo una parte, desde VS Code:
         1. Selecciona con el mouse las líneas de UN paso.
         2. Presiona Shift + Enter.
     Python ejecuta solo lo seleccionado y recuerda lo anterior.
     IMPORTANTE: corre primero el PASO 0, porque carga los datos.

Todo lo que empieza con # es un comentario: Python lo ignora, es para ti.
---------------------------------------------------------------------------
"""

# =========================================================================
# PASO 0 · PREPARACIÓN (correr siempre primero)
# =========================================================================
import pandas as pd   # trae la herramienta pandas

# Leemos dos tablas de Olist y las guardamos en variables.
# Una variable es un nombre que guarda un valor:  nombre = valor
RUTA = "data/raw/"   # texto guardado en una variable
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
reviews = pd.read_csv(
    RUTA + "olist_order_reviews_dataset.csv")

print("Filas en orders:", len(orders))
print("Filas en reviews:", len(reviews))


# =========================================================================
# PASO 1 · LISTAS  [ ]  — ordenadas y se pueden modificar
# Idea: los estados por los que pasa una orden, en orden.
# =========================================================================
estados = ["created", "approved",
           "processing", "shipped",
           "delivered"]

print("La lista:", estados)
print("Cuántos:", len(estados))
print("El primero:", estados[0])
print("El último:", estados[-1])

estados.append("canceled")   # agrega al final
print("Ahora:", estados)

for estado in estados:      # repite para cada elemento
    print(" - estado:", estado)


# =========================================================================
# PASO 2 · TUPLAS  ( )  — ordenadas, NO se pueden modificar
# Idea: la "huella" de una orden: su id y su estado, fijos.
# =========================================================================
ids = orders["order_id"].tolist()    # columna -> lista
estado_orden = orders["order_status"].tolist()

huella = (ids[0], estado_orden[0])   # ( ) = tupla

print("La tupla:", huella)
print("Id:", huella[0])
print("Estado:", huella[1])

# huella[1] = "otro"
# Si quitas el # de arriba y corres esa línea, Python
# responde TypeError: una tupla no se puede modificar.


# =========================================================================
# PASO 3 · SETS  { }  — sin repetidos, sin orden
# Idea: ¿qué estados distintos existen? ¿qué órdenes no tienen reseña?
# =========================================================================
print("Con repetidos:", len(estado_orden))

estados_unicos = set(estado_orden)  # sin repetidos
print("Distintos:", estados_unicos)
print("Cuántos:", len(estados_unicos))

todas = set(orders["order_id"])      # todas
con_resena = set(reviews["order_id"])  # con reseña
sin_resena = todas - con_resena      # resta

print("Sin reseña:", len(sin_resena))


# =========================================================================
# PASO 4 · DICCIONARIOS  { clave: valor }  — como una libreta de contactos
# Idea: traducir los estados al español, y describir una orden.
# =========================================================================
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
