"""
DPL1046 · Clase 2 · 03b_listas.py
LISTAS  [ ]  — ordenadas y se pueden modificar.
Idea: los estados por los que pasa una orden de Olist, en orden.

Córrelo con el botón ▶ o con:
    python clases/clase-02/material/03b_listas.py
"""

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
