"""
DPL1046 · Clase 7 · 02_errores.py
Decisiones (if / elif / else), repeticiones (for) y errores (try / except).

Córrelo con el botón ▶ o con:
    python clases/clase-07/material/02_errores.py
"""

import pandas as pd


def clasificar_entrega(dias):
    """Clasifica una entrega según los días que tardó."""
    if dias <= 7:
        return "rápida"
    elif dias <= 20:
        return "normal"
    else:
        return "lenta"


# for: repetir lo mismo para cada elemento de una lista
for dias in [3, 12, 45]:
    print(dias, "días →", clasificar_entrega(dias))

# try / except: ¿y si el archivo no existe?
def leer_tabla(ruta):
    """Lee un CSV; si no existe, avisa con un mensaje claro."""
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print("No encontré el archivo:", ruta)
        return None


for ruta in ["data/raw/olist_orders_dataset.csv", "data/raw/no_existe.csv"]:
    tabla = leer_tabla(ruta)
    if tabla is not None:
        print("Leído:", ruta, "→", len(tabla), "filas")

# Otro error típico: convertir texto a número
for texto in ["12", "abc", "7"]:
    try:
        print("Número leído:", int(texto))
    except ValueError:
        print("No es un número:", texto)
