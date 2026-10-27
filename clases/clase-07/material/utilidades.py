"""
DPL1046 · Clase 7 · utilidades.py
Dos funciones de nuestro proyecto, guardadas en su propio archivo para
poder usarlas desde otros archivos y probarlas con pytest.
"""

import pandas as pd


def calcular_dias(compra, entrega):
    """Devuelve los días que pasan entre dos fechas (escritas como texto)."""
    return (pd.to_datetime(entrega) - pd.to_datetime(compra)).days


def clasificar_entrega(dias):
    """Clasifica una entrega según los días que tardó."""
    if dias < 0:
        raise ValueError("Los días no pueden ser negativos")
    if dias <= 7:
        return "rápida"
    elif dias <= 20:
        return "normal"
    else:
        return "lenta"
