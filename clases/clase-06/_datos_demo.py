"""
_datos_demo.py
------------------------------------------------------------------
Genera un mini-dataset de pedidos estilo Olist, SUCIO a propósito,
con SEMILLA FIJA para que siempre veas los mismos números en clase.

No necesitas internet. Los demás scripts (01 a 04) importan desde aquí:

    from _datos_demo import generar_pedidos

Datos sucios incluidos a propósito (para poder limpiarlos/validarlos):
- precios que llegan como TEXTO ("138.28")
- algunos precios nulos (vacíos)
- ciudades escritas inconsistentes ("sao paulo", "SAO PAULO ", " Sao Paulo")
------------------------------------------------------------------
"""

import numpy as np
import pandas as pd

SEMILLA = 42  # semilla fija => mismos números siempre


def generar_pedidos(n: int = 200) -> pd.DataFrame:
    """Devuelve un DataFrame de pedidos 'sucio' y reproducible."""
    rng = np.random.default_rng(SEMILLA)

    ciudades = ["sao paulo", "SAO PAULO ", " Sao Paulo",
                "rio de janeiro", "RIO DE JANEIRO", "curitiba"]
    categorias = ["muebles_decoracion", "informatica", "deportes",
                  "juguetes", "belleza"]

    order_id = [f"o{n_:04d}" for n_ in range(1, n + 1)]
    product_id = [f"p{rng.integers(1, 30):03d}" for _ in range(n)]
    categoria = rng.choice(categorias, size=n)

    # precio "real" entre 10 y 300; lo guardamos como TEXTO a propósito
    precio_num = np.round(rng.uniform(10, 300, size=n), 2)
    price = [f"{p:.2f}" for p in precio_num]

    freight = np.round(rng.uniform(0, 40, size=n), 2)
    city = rng.choice(ciudades, size=n)
    rating = rng.integers(1, 6, size=n)  # 1 a 5 estrellas

    df = pd.DataFrame({
        "order_id": order_id,
        "product_id": product_id,
        "categoria": categoria,
        "price": price,            # <-- TEXTO
        "freight_value": freight,
        "city": city,             # <-- inconsistente
        "rating": rating,
    })

    # Ensuciar: meter ~8% de precios nulos
    idx_nulos = rng.choice(df.index, size=int(n * 0.08), replace=False)
    df.loc[idx_nulos, "price"] = None

    return df


if __name__ == "__main__":
    demo = generar_pedidos()
    print("Forma:", demo.shape)
    print(demo.head())
    print("\nTipos de dato:")
    print(demo.dtypes)
    print("\nNulos por columna:")
    print(demo.isna().sum())
