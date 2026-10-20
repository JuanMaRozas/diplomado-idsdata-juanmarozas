"""
DPL1046 · Clase 4 · 02_excel.py
Crear un Excel con 2 hojas y leerlo hoja por hoja.

Córrelo con el botón ▶ o con:
    python clases/clase-04/material/02_excel.py
"""

import pandas as pd

# 1) Creamos un Excel de ejemplo (simula un reporte que te mandan)
ventas = pd.DataFrame({
    "region": ["RM", "Biobío", "Valparaíso"],
    "ventas": [1200, 800, 950],
})
clientes = pd.DataFrame({
    "region": ["RM", "Biobío", "Valparaíso"],
    "clientes": [45, 30, 38],
})

with pd.ExcelWriter("data/reporte_demo.xlsx") as escritor:
    ventas.to_excel(escritor, sheet_name="Ventas", index=False)
    clientes.to_excel(escritor, sheet_name="Clientes", index=False)
print("Excel creado: data/reporte_demo.xlsx")

# 2) Lo leemos: primero, ¿qué hojas tiene?
archivo = pd.ExcelFile("data/reporte_demo.xlsx")
print("Hojas:", archivo.sheet_names)

# 3) Luego leemos una hoja por su nombre
hoja_ventas = pd.read_excel("data/reporte_demo.xlsx", sheet_name="Ventas")
print(hoja_ventas)
