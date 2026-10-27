"""
DPL1046 · Clase 7 · test_utilidades.py
Pruebas automáticas (pytest) para utilidades.py.

Córrelo con:
    pytest clases/clase-07/material/ -v
"""

import pytest
from utilidades import calcular_dias, clasificar_entrega


def test_calcular_dias():
    assert calcular_dias("2017-10-02", "2017-10-10") == 8


def test_entrega_rapida():
    assert clasificar_entrega(5) == "rápida"


def test_entrega_normal():
    assert clasificar_entrega(15) == "normal"


def test_entrega_lenta():
    assert clasificar_entrega(45) == "lenta"


def test_dias_negativos_da_error():
    with pytest.raises(ValueError):
        clasificar_entrega(-1)
