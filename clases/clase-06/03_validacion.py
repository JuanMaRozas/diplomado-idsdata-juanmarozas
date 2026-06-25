"""
03_validacion.py
==================================================================
BLOQUE 3 — Confiar en los datos: validación de calidad.

Antes de dejar pasar los datos al resto del pipeline, los REVISAMOS
con un "contrato": un conjunto de reglas que SIEMPRE deben cumplirse.
Si una regla se rompe, el pipeline se detiene con un mensaje claro,
en vez de seguir y producir un reporte equivocado.

Esto es la versión simple y casera de herramientas como
Great Expectations, pero se entiende línea por línea.

Cómo correrlo:
    python 03_validacion.py
==================================================================
"""

import pandas as pd
from loguru import logger

from _datos_demo import generar_pedidos


# ------------------------------------------------------------------
# Función de transformación que también vamos a TESTEAR (ver test_*)
# ------------------------------------------------------------------
def limpiar_precio(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte price (texto) a número y descarta filas sin precio."""
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    return df


# ------------------------------------------------------------------
# El "contrato de datos": reglas que SIEMPRE deben cumplirse
# ------------------------------------------------------------------
def validar(df: pd.DataFrame) -> None:
    """Lanza un error claro si los datos no cumplen las expectativas."""
    logger.info("Validando calidad de los datos...")

    # Regla 1: no deben faltar columnas clave
    columnas_clave = {"order_id", "price", "rating"}
    faltan = columnas_clave - set(df.columns)
    assert not faltan, f"Faltan columnas obligatorias: {faltan}"

    # Regla 2: price debe ser numérico
    assert pd.api.types.is_numeric_dtype(df["price"]), \
        "La columna price NO es numérica"

    # Regla 3: no hay precios negativos
    assert (df["price"] >= 0).all(), "Hay precios negativos"

    # Regla 4: rating siempre entre 1 y 5
    assert df["rating"].between(1, 5).all(), "Hay ratings fuera de 1-5"

    # Regla 5: no hay order_id duplicados
    assert not df["order_id"].duplicated().any(), "Hay order_id duplicados"

    logger.success("Validación OK: los datos cumplen el contrato")


def main():
    df = generar_pedidos(200)
    df = limpiar_precio(df)
    validar(df)
    print(f"\nDatos validados: {df.shape[0]} filas listas para usar.")


if __name__ == "__main__":
    main()
