"""
DPL1046 · Clase 4 · 03_json.py
JSON anidado: diccionarios y listas dentro de otros diccionarios,
tal como responde una API. Lo convertimos en una tabla.

Córrelo con el botón ▶ o con:
    python clases/clase-04/material/03_json.py
"""

import pandas as pd

# Así llega un JSON desde una API: un diccionario con una lista adentro
respuesta = {
    "marketplace": "Olist",
    "vendedores": [
        {"vendedor": "Tienda A", "estado": "SP", "ventas": 50000},
        {"vendedor": "Tienda B", "estado": "RJ", "ventas": 32000},
    ],
}

print("Marketplace:", respuesta["marketplace"])
print("Lista de vendedores:", respuesta["vendedores"])
print("El primero:", respuesta["vendedores"][0])
print("Su nombre:", respuesta["vendedores"][0]["vendedor"])

# Convertimos la lista de diccionarios en una tabla
tabla = pd.json_normalize(respuesta["vendedores"])
print(tabla)
