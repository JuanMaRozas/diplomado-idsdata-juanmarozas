"""
test_validacion.py
==================================================================
Tests automáticos con pytest. Un test es una función que comprueba
que tu código hace lo que prometes. Si algún día rompes algo sin
querer, los tests te avisan ANTES de que el error llegue al cliente.

Cómo correrlos (desde la carpeta clase-06):
    pytest -v
==================================================================
"""

import pandas as pd

from importlib import import_module

# importamos la función desde el script 03 (el nombre empieza con número,
# así que usamos import_module en vez de "import 03_validacion")
mod = import_module("03_validacion")
limpiar_precio = mod.limpiar_precio


def test_convierte_texto_a_numero():
    """Un precio en texto debe quedar como número."""
    df = pd.DataFrame({"price": ["100.50", "20.00"]})
    resultado = limpiar_precio(df)
    assert pd.api.types.is_numeric_dtype(resultado["price"])
    assert resultado["price"].iloc[0] == 100.50


def test_descarta_filas_sin_precio():
    """Las filas con precio vacío deben eliminarse."""
    df = pd.DataFrame({"price": ["100.50", None, "30.00"]})
    resultado = limpiar_precio(df)
    assert resultado.shape[0] == 2  # quedaron 2 de 3


def test_precio_basura_se_vuelve_nulo_y_se_descarta():
    """Un texto que no es número ('abc') no debe romper el pipeline."""
    df = pd.DataFrame({"price": ["100.50", "abc"]})
    resultado = limpiar_precio(df)
    assert resultado.shape[0] == 1  # 'abc' se descartó
