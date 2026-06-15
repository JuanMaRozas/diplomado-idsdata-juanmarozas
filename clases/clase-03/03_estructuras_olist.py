"""
DPL1046 · Clase 3 · Script 3 · 03_estructuras_olist.py
---------------------------------------------------------------------------
Objetivo pedagógico: dominar las 4 estructuras nativas de Python
(list, tuple, set, dict) y las comprehensions, aplicadas al MISMO
dataset Olist que venimos usando desde la Clase 1.

Continuidad: en la Clase 1 leímos las tablas con pandas y usamos groupby.
Hoy bajamos un nivel: ¿qué estructura de Python conviene para cada tarea?

Tablas usadas (data/raw/):
  - olist_orders_dataset.csv          -> estados y fechas de las órdenes
  - olist_order_payments_dataset.csv  -> formas y montos de pago
  - olist_order_reviews_dataset.csv   -> reseñas con texto libre
---------------------------------------------------------------------------
"""
from pathlib import Path

import pandas as pd


def raiz_repo() -> Path:
    """Encuentra la raíz del repo subiendo desde este archivo.
    (Misma función de la Clase 1: el script corre desde cualquier carpeta.)"""
    aqui = Path(__file__).resolve()
    for carpeta in [aqui, *aqui.parents]:
        if (carpeta / ".git").exists() or (carpeta / "clases").is_dir():
            return carpeta
    return Path.cwd()


DATA = raiz_repo() / "data" / "raw"


# ─────────────────────────────────────────────────────────────────────────
# 1. LISTAS · secuencia ordenada y mutable
#    Caso Olist: los estados por los que pasa una orden, en orden.
# ─────────────────────────────────────────────────────────────────────────
def demo_listas() -> None:
    print(f"\n{'='*60}\n 1. LISTAS — ordenadas, mutables\n{'='*60}")

    orders = pd.read_csv(DATA / "olist_orders_dataset.csv")

    # Los estados posibles de una orden, como lista (mantiene el flujo lógico)
    flujo_estado = ["created", "approved", "processing",
                    "shipped", "delivered"]
    print(f"Flujo esperado de una orden: {flujo_estado}")
    print(f"Primer estado : {flujo_estado[0]}")
    print(f"Estado final  : {flujo_estado[-1]}")

    # Estados reales presentes en el dataset (algunos no llegan a 'delivered')
    estados_reales = orders["order_status"].value_counts()
    print("\nEstados reales en Olist (con conteo):")
    print(estados_reales.to_string())


# ─────────────────────────────────────────────────────────────────────────
# 2. TUPLAS · inmutables, ideales para registros que no deben cambiar
#    Caso Olist: la "huella" de una orden (id, estado) como dato fijo.
# ─────────────────────────────────────────────────────────────────────────
def demo_tuplas() -> None:
    print(f"\n{'='*60}\n 2. TUPLAS — inmutables, hasheables\n{'='*60}")

    orders = pd.read_csv(DATA / "olist_orders_dataset.csv").head(3)

    # Cada orden como tupla (id, estado): no se puede modificar por accidente
    huellas = [
        (row.order_id, row.order_status)
        for row in orders.itertuples()
    ]
    for hid, estado in huellas:
        print(f"  orden {hid[:8]}... → {estado}")

    # Las tuplas pueden ser CLAVES de diccionario (las listas no)
    conteo_par = {("delivered", "credit_card"): 0}
    print(f"\nTupla como clave de dict: {conteo_par}")
    # huellas[0][0] = "X"  ← TypeError: la tupla no se puede modificar


# ─────────────────────────────────────────────────────────────────────────
# 3. SETS · sin duplicados, búsqueda O(1)
#    Caso Olist: ¿qué clientes únicos hay? ¿qué órdenes tienen reseña?
# ─────────────────────────────────────────────────────────────────────────
def demo_sets() -> None:
    print(f"\n{'='*60}\n 3. SETS — sin duplicados, búsqueda O(1)\n{'='*60}")

    orders  = pd.read_csv(DATA / "olist_orders_dataset.csv")
    reviews = pd.read_csv(DATA / "olist_order_reviews_dataset.csv")

    # Conjunto de órdenes que tienen al menos una reseña
    ordenes_con_review = set(reviews["order_id"])
    ordenes_totales    = set(orders["order_id"])
    print(f"Órdenes totales      : {len(ordenes_totales):,}")
    print(f"Órdenes con reseña   : {len(ordenes_con_review):,}")

    # Operación de conjuntos: órdenes SIN reseña (diferencia)
    sin_review = ordenes_totales - ordenes_con_review
    print(f"Órdenes sin reseña   : {len(sin_review):,}")

    # Buscar si una orden tiene reseña: O(1) en un set vs O(n) en una lista
    una_orden = next(iter(ordenes_con_review))
    print(f"\n¿La orden {una_orden[:8]}... tiene reseña? "
          f"{una_orden in ordenes_con_review}")  # instantáneo


# ─────────────────────────────────────────────────────────────────────────
# 4. DICCIONARIOS · clave→valor, la estructura del pipeline
#    Caso Olist: un mapeo traducción de estados, y un registro de orden.
# ─────────────────────────────────────────────────────────────────────────
def demo_diccionarios() -> None:
    print(f"\n{'='*60}\n 4. DICCIONARIOS — clave→valor, O(1)\n{'='*60}")

    # Mapeo de traducción de estados (dict comprehension a partir de pares)
    pares = [("delivered", "Entregado"), ("shipped", "Enviado"),
             ("canceled", "Cancelado"), ("processing", "En proceso")]
    traduccion = {en: es for en, es in pares}
    print(f"Mapeo de estados: {traduccion}")

    # Acceso seguro con .get(): nunca lanza KeyError
    print(f"'delivered' → {traduccion.get('delivered', 'desconocido')}")
    print(f"'invoiced'  → {traduccion.get('invoiced', 'desconocido')}")  # no existe

    # Un registro de orden como dict (así llega de una API o un to_dict())
    orders = pd.read_csv(DATA / "olist_orders_dataset.csv").head(1)
    registro = orders.iloc[0].to_dict()
    print("\nUna orden como diccionario (claves):")
    print(f"  {list(registro.keys())}")
    print(f"  estado traducido: "
          f"{traduccion.get(registro['order_status'], registro['order_status'])}")


# ─────────────────────────────────────────────────────────────────────────
# 5. COMPREHENSIONS · transformaciones masivas en una línea
#    Caso Olist: clasificar pagos y filtrar reseñas negativas.
# ─────────────────────────────────────────────────────────────────────────
def demo_comprehensions() -> None:
    print(f"\n{'='*60}\n 5. COMPREHENSIONS — código limpio\n{'='*60}")

    payments = pd.read_csv(DATA / "olist_order_payments_dataset.csv")
    reviews  = pd.read_csv(DATA / "olist_order_reviews_dataset.csv")

    # List comprehension: montos de pago con tarjeta, sobre R$ 500
    pagos = payments.to_dict("records")
    altos_tarjeta = [
        p["payment_value"]
        for p in pagos[:5000]
        if p["payment_type"] == "credit_card" and p["payment_value"] > 500
    ]
    print(f"Pagos con tarjeta > R$500 (muestra 5k): {len(altos_tarjeta):,}")

    # Set comprehension: tipos de pago únicos
    tipos = {p["payment_type"] for p in pagos[:5000]}
    print(f"Tipos de pago únicos: {tipos}")

    # Dict comprehension: conteo de reseñas por puntaje (1 a 5 estrellas)
    scores = reviews["review_score"].tolist()
    conteo = {estrella: scores.count(estrella) for estrella in range(1, 6)}
    print(f"Reseñas por puntaje : {conteo}")


def main() -> None:
    demo_listas()
    demo_tuplas()
    demo_sets()
    demo_diccionarios()
    demo_comprehensions()
    print(f"\n{'='*60}")
    print(" Las mismas tablas Olist, vistas con estructuras de Python.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
