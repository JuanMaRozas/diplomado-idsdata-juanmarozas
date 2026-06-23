"""
_datos_demo.py
------------------------------------------------------------------
Genera un mini-dataset estilo Olist para que TODOS los scripts de la
Clase 5 corran SIEMPRE, incluso si no está el dataset real en data/raw/.

Idea pedagógica: cada script intenta primero leer los CSV reales de Olist;
si no los encuentra, usa estos datos sintéticos. Así nadie se queda sin
poder ejecutar la clase por un tema de archivos.

NOTA: los datos son inventados pero "realistas a propósito": traen
   - valores nulos (celdas vacías),
   - una columna de precio que llega como TEXTO,
   - una columna de ciudad con texto inconsistente ("SP", " sao paulo ", ...),
   - una fecha como texto.
...para poder demostrar la limpieza de la Clase 5.
"""

import numpy as np
import pandas as pd

SEMILLA = 42  # misma semilla => mismos datos => clase reproducible


def tabla_pedidos(n: int = 200) -> pd.DataFrame:
    """Pedidos: order_id, product_id, price (TEXTO), freight_value, city (sucio), fecha (texto)."""
    rng = np.random.default_rng(SEMILLA)

    product_ids = [f"p{idx:03d}" for idx in range(1, 21)]  # 20 productos
    # Ciudades escritas "a la chilena/brasileña real": inconsistentes a propósito
    ciudades_sucias = ["sao paulo", "Sao Paulo", " SAO PAULO ", "SP",
                       "rio de janeiro", "Rio De Janeiro ", "rj", "curitiba"]

    precios = rng.normal(120, 60, n).clip(8, 400).round(2)
    # price llega como TEXTO (como pasa cuando viene de un Excel/CSV mal tipado)
    precios_texto = [f"{p:.2f}" for p in precios]

    df = pd.DataFrame({
        "order_id": [f"o{idx:04d}" for idx in range(1, n + 1)],
        "product_id": rng.choice(product_ids, n),
        "price": precios_texto,                              # <-- TEXTO, no número
        "freight_value": rng.normal(20, 8, n).clip(0, 60).round(2),
        "city": rng.choice(ciudades_sucias, n),             # <-- texto sucio
        "fecha_compra": pd.to_datetime("2018-01-01")
                        + pd.to_timedelta(rng.integers(0, 365, n), unit="D"),
    })
    # La fecha la entregamos como TEXTO (otra vez: realismo de dato sucio)
    df["fecha_compra"] = df["fecha_compra"].dt.strftime("%Y-%m-%d")

    # Metemos algunos NULOS en price y freight (5% aprox)
    idx_nulos_price = rng.choice(n, size=max(1, n // 20), replace=False)
    df.loc[idx_nulos_price, "price"] = None
    idx_nulos_freight = rng.choice(n, size=max(1, n // 25), replace=False)
    df.loc[idx_nulos_freight, "freight_value"] = np.nan
    return df


def tabla_productos() -> pd.DataFrame:
    """Productos: product_id + category (la categoría de cada producto)."""
    rng = np.random.default_rng(SEMILLA + 1)
    categorias = ["cama_mesa_bano", "belleza_salud", "deportes_ocio",
                  "informatica", "muebles_decoracion", "juguetes"]
    return pd.DataFrame({
        "product_id": [f"p{idx:03d}" for idx in range(1, 21)],
        "category": rng.choice(categorias, 20),
    })


def tabla_reviews(pedidos: pd.DataFrame) -> pd.DataFrame:
    """Reseñas: order_id + review_score (1 a 5). Algunas órdenes sin reseña."""
    rng = np.random.default_rng(SEMILLA + 2)
    # Solo el 85% de los pedidos tiene reseña (realismo)
    con_review = pedidos.sample(frac=0.85, random_state=SEMILLA)
    return pd.DataFrame({
        "order_id": con_review["order_id"].values,
        "review_score": rng.integers(1, 6, len(con_review)),
    })


if __name__ == "__main__":
    p = tabla_pedidos()
    print("PEDIDOS:", p.shape)
    print(p.head(3).to_string(index=False))
    print("\nPRODUCTOS:", tabla_productos().shape)
    print("\nREVIEWS:", tabla_reviews(p).shape)
