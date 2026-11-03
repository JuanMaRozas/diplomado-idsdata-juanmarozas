"""
DPL1046 · Clase 7 · test_refactor_copilot.py
Red de seguridad del refactor: estos tests deben pasar ANTES y DESPUÉS
de pedirle a Copilot que ordene 04_refactor_copilot.py.
"""

import importlib

modulo = importlib.import_module("04_refactor_copilot")
resumir_pedidos = modulo.resumir_pedidos

PEDIDOS = [
    {"estado": "delivered", "precio": 100, "flete": 10, "dias": 5},
    {"estado": "delivered", "precio": 200, "flete": 20, "dias": 25},
    {"estado": "canceled", "precio": 999, "flete": 99, "dias": 1},
]


def test_ignora_pedidos_no_entregados():
    assert resumir_pedidos(PEDIDOS)["total"] == 330


def test_promedio_por_pedido_entregado():
    assert resumir_pedidos(PEDIDOS)["promedio"] == 165.0


def test_cuenta_entregas_lentas():
    assert resumir_pedidos(PEDIDOS)["lentas"] == 1


def test_lista_vacia():
    assert resumir_pedidos([]) == {"total": 0, "promedio": 0, "lentas": 0}
