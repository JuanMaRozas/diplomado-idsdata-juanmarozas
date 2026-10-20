"""
DPL1046 · Clase 3 · 05_ficha_proyecto.py
Tu proyecto integrador descrito con las 4 estructuras de Python.

Idea: la "ficha" de tu proyecto es un DICCIONARIO. Dentro guarda
una cadena de texto, una LISTA, un SET y una TUPLA.

Pasos:
  1. Cambia los valores por los de tu pareja y tu tema.
  2. Guarda el archivo (Cmd+S / Ctrl+S).
  3. Ejecútalo con el botón ▶ o con:
         python clases/clase-03/material/05_ficha_proyecto.py
"""

tema = "Radar de satisfacción del cliente"              # texto
integrantes = ["Ana Pérez", "Luis Soto"]                 # lista (en orden)
tablas = {"reviews", "order_items", "products"}          # set (sin repetidos)
entregas = ("Unidad 1", "Unidad 2", "Unidad 3")          # tupla (no cambia)

ficha = {                                                # diccionario
    "tema": tema,
    "integrantes": integrantes,
    "tablas": tablas,
    "entregas": entregas,
}

print("Tema:", ficha["tema"])
print("Cantidad de integrantes:", len(ficha["integrantes"]))
for nombre in ficha["integrantes"]:
    print(" - integrante:", nombre)
print("Tablas de Olist:", ficha["tablas"])
print("Entregas:", ficha["entregas"])
