"""
DPL1046 · Clase 7 · 04_refactor_copilot.py
Código que FUNCIONA, pero está desordenado. Sirve para practicar el
refactor con la IA de Copilot en VS Code (ver la slide "Práctica").

Regla de oro: el refactor ordena el código SIN cambiar lo que hace.
Los tests de test_refactor_copilot.py te avisan si algo cambió.
"""


def resumir_pedidos(p):
    t = 0
    c = 0
    for x in p:
        if x["estado"] == "delivered":
            t = t + x["precio"] + x["flete"]
            c = c + 1
    if c == 0:
        return {"total": 0, "promedio": 0, "lentas": 0}
    a = t / c
    l = 0
    for x in p:
        if x["estado"] == "delivered":
            if x["dias"] > 20:
                l = l + 1
    return {"total": t, "promedio": round(a, 2), "lentas": l}


if __name__ == "__main__":
    pedidos = [
        {"estado": "delivered", "precio": 100, "flete": 10, "dias": 5},
        {"estado": "delivered", "precio": 200, "flete": 20, "dias": 25},
        {"estado": "canceled", "precio": 999, "flete": 99, "dias": 1},
    ]
    print(resumir_pedidos(pedidos))
