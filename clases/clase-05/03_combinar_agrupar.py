"""
03_combinar_agrupar.py  ·  Clase 5 · Bloque 3
====================================================================
OBJETIVO: pasar de MUCHAS tablas a UNA respuesta. El superpoder de pandas.

Lo que demuestra este script, paso a paso:
  1. merge: unir tablas por una columna en común (el "BUSCARV" de tablas).
  2. groupby + agg: resumir millones de filas sin un solo for.
  3. value_counts: el "top" de una columna en una línea.
  4. sort_values + head: armar un ranking listo para presentar.

Cómo correrlo:
    python 03_combinar_agrupar.py
====================================================================
"""

import logging
import pandas as pd

from _datos_demo import tabla_pedidos, tabla_productos, tabla_reviews

logging.basicConfig(level=logging.INFO, format="%(message)s")


def cargar_tablas():
    pedidos = tabla_pedidos()
    pedidos["price"] = pd.to_numeric(pedidos["price"], errors="coerce")
    productos = tabla_productos()
    reviews = tabla_reviews(pedidos)
    return pedidos, productos, reviews


def main() -> None:
    pedidos, productos, reviews = cargar_tablas()
    logging.info("Tablas de entrada -> pedidos:%s  productos:%s  reviews:%s\n",
                 pedidos.shape, productos.shape, reviews.shape)

    # ---- 1) merge: pegar la categoría del producto a cada pedido -----------
    logging.info("=== 1) merge (unir tablas por una columna en común) ===")
    full = pedidos.merge(productos, on="product_id", how="left")   # añade 'category'
    full = full.merge(reviews, on="order_id", how="left")          # añade 'review_score'
    logging.info("Tabla unida: %s columnas -> %s", full.shape, list(full.columns))
    logging.info("(how='left' = conservo todos mis pedidos aunque falte el match)\n")

    # ---- 2) groupby + agg: resumir por categoría ---------------------------
    logging.info("=== 2) groupby + agg (resumir sin for) ===")
    price_mean = full.groupby("category")["price"].mean()
    logging.info("%s\n", price_mean.to_string())

    resumen = full.groupby("category").agg(
        precio_prom=("price", "mean"),
        pedidos=("order_id", "count"),
        rating_prom=("review_score", "mean"),
    ).round(2)
    logging.info("Resumen por categoría:\n%s\n", resumen.to_string())

    # ---- 3) value_counts: el top de una columna ----------------------------
    logging.info("=== 3) value_counts (top categorías por nº de pedidos) ===")
    top = full["category"].value_counts().head(3)
    logging.info("%s\n", top.to_string())

    # ---- 4) sort_values + head: un ranking presentable ---------------------
    logging.info("=== 4) sort_values + head (ranking listo) ===")
    ranking = resumen.sort_values("precio_prom", ascending=False).head(3)
    logging.info("Top 3 categorías más caras (precio promedio):\n%s\n", ranking.to_string())

    logging.info("Listo ✅  merge junta, groupby resume, sort ordena: ese es el esqueleto de un reporte.")


if __name__ == "__main__":
    main()
