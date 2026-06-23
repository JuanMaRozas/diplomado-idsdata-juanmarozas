"""
04_pipeline_categorias.py  ·  Clase 5 · Caso integrador
====================================================================
PREGUNTA DE NEGOCIO:
   "¿Qué categoría de producto tiene el PEOR rating promedio,
    y cuántos pedidos representa?"

Encadenamos las TRES herramientas de la noche en un pipeline:
   limpiar  ->  combinar (merge)  ->  agrupar (groupby)  ->  ordenar  ->  responder.

Esto es, en miniatura, lo que harás en el proyecto integrador.

Cómo correrlo:
    python 04_pipeline_categorias.py
====================================================================
"""

import logging
import pandas as pd

from _datos_demo import tabla_pedidos, tabla_productos, tabla_reviews

logging.basicConfig(level=logging.INFO, format="%(message)s")


def limpiar_pedidos(pedidos: pd.DataFrame) -> pd.DataFrame:
    """Paso 1: dejar los pedidos en condiciones (tipos + texto + nulos)."""
    pedidos = pedidos.copy()
    pedidos["price"] = pd.to_numeric(pedidos["price"], errors="coerce")
    pedidos["city"] = pedidos["city"].str.strip().str.lower()
    pedidos = pedidos.dropna(subset=["price"])     # sin precio no sirve
    return pedidos


def main() -> None:
    # --- Cargar las tres tablas crudas -------------------------------------
    pedidos = tabla_pedidos()
    productos = tabla_productos()
    reviews = tabla_reviews(pedidos)

    # --- Paso 1: LIMPIAR ----------------------------------------------------
    pedidos = limpiar_pedidos(pedidos)
    logging.info("1) Limpiar  -> pedidos válidos: %d", len(pedidos))

    # --- Paso 2: COMBINAR (merge) ------------------------------------------
    full = (pedidos
            .merge(productos, on="product_id", how="left")
            .merge(reviews, on="order_id", how="left"))
    logging.info("2) Combinar -> tabla unida: %s", full.shape)

    # --- Paso 3: AGRUPAR (groupby) -----------------------------------------
    resumen = full.groupby("category").agg(
        rating_prom=("review_score", "mean"),
        pedidos=("order_id", "count"),
    ).round(2)
    logging.info("3) Agrupar  -> %d categorías", len(resumen))

    # --- Paso 4: ORDENAR y RESPONDER ---------------------------------------
    peor = resumen.sort_values("rating_prom").head(1)
    logging.info("4) Ordenar  -> tabla por rating (de peor a mejor):\n%s\n",
                 resumen.sort_values("rating_prom").to_string())

    categoria = peor.index[0]
    rating = peor["rating_prom"].iloc[0]
    n_pedidos = int(peor["pedidos"].iloc[0])

    logging.info("=" * 56)
    logging.info("RESPUESTA: la categoría con peor rating es '%s'", categoria)
    logging.info("           rating promedio = %.2f  (%d pedidos)", rating, n_pedidos)
    logging.info("=" * 56)
    logging.info("\nEso es un pipeline: una pregunta de negocio respondida con datos.")


if __name__ == "__main__":
    main()
