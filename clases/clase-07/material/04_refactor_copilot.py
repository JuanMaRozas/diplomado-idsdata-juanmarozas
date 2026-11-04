"""
DPL1046 · Clase 7 · 04_refactor_copilot.py
Código que FUNCIONA, pero está desordenado. Sirve para practicar el
refactor con la IA de Copilot en VS Code (ver la slide "Práctica").

Regla de oro: el refactor ordena el código SIN cambiar lo que hace.
Los tests de test_refactor_copilot.py te avisan si algo cambió.
"""


def resumir_pedidos(pedidos):
    """Resume el total, promedio y entregas lentas de los pedidos entregados."""
    total = 0
    cantidad_entregados = 0
    entregas_lentas = 0

    for pedido in pedidos:
        if pedido["estado"] == "delivered":
            total += pedido["precio"] + pedido["flete"]
            cantidad_entregados += 1
            if pedido["dias"] > 20:
                entregas_lentas += 1

    if cantidad_entregados == 0:
        return {"total": 0, "promedio": 0, "lentas": 0}

    promedio = total / cantidad_entregados
    return {
        "total": total,
        "promedio": round(promedio, 2),
        "lentas": entregas_lentas,
    }


if __name__ == "__main__":
    pedidos = [
        {"estado": "delivered", "precio": 100, "flete": 10, "dias": 5},
        {"estado": "delivered", "precio": 200, "flete": 20, "dias": 25},
        {"estado": "canceled", "precio": 999, "flete": 99, "dias": 1},
    ]
    print(resumir_pedidos(pedidos))
