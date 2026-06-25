"""
02_pipeline_robusto.py
==================================================================
BLOQUE 2 — Que se ejecute solo y NO se rompa.

Tres ideas de "código de producción":

  1) MANEJO DE ERRORES: try/except para que un dato malo no tumbe todo.
  2) REINTENTOS (retry con backoff): si una fuente falla por azar,
     reintentamos unas veces antes de rendirnos. Típico con APIs.
  3) IDEMPOTENCIA: correr el script 2 veces seguidas NO duplica ni
     corrompe el resultado. Si ya estaba hecho, lo detecta y no rehace.

Cómo correrlo (¡córrelo DOS veces para ver la idempotencia!):
    python 02_pipeline_robusto.py
    python 02_pipeline_robusto.py
==================================================================
"""

import time
from pathlib import Path

import numpy as np
import pandas as pd
from loguru import logger

from _datos_demo import generar_pedidos

BASE   = Path(__file__).parent
SALIDA = BASE / "salida/pedidos_limpios.csv"


# ------------------------------------------------------------------
# 1) Una "fuente inestable" simulada (como una API que a veces falla)
# ------------------------------------------------------------------
def fuente_inestable(intento_actual: int) -> pd.DataFrame:
    """Falla los 2 primeros intentos a propósito, luego responde."""
    if intento_actual < 3:
        raise ConnectionError("La fuente no respondió (simulado)")
    return generar_pedidos(200)


# ------------------------------------------------------------------
# 2) Patrón retry con backoff: reintentar esperando cada vez más
# ------------------------------------------------------------------
def traer_con_reintentos(max_intentos: int = 4) -> pd.DataFrame:
    for intento in range(1, max_intentos + 1):
        try:
            logger.info(f"Intento {intento} de leer la fuente...")
            df = fuente_inestable(intento)
            logger.success(f"Fuente respondió en el intento {intento}")
            return df
        except ConnectionError as e:
            espera = 0.5 * intento  # backoff: 0.5s, 1.0s, 1.5s...
            logger.warning(f"Falló ({e}). Reintento en {espera:.1f}s")
            time.sleep(espera)
    raise RuntimeError("La fuente nunca respondió. Me rindo.")


# ------------------------------------------------------------------
# 3) Idempotencia: si el resultado ya existe, no lo rehago
# ------------------------------------------------------------------
def ya_esta_hecho() -> bool:
    return SALIDA.exists()


def procesar(df: pd.DataFrame) -> pd.DataFrame:
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"]).copy()  # .copy() evita SettingWithCopyWarning
    df["city"] = df["city"].str.strip().str.lower()
    return df


def main():
    logger.info("=== Pipeline robusto: INICIO ===")

    # Idempotencia primero: ¿ya hicimos este trabajo?
    if ya_esta_hecho():
        logger.info(f"'{SALIDA}' ya existe. No rehago nada. (idempotente)")
        logger.success("=== Pipeline robusto: FIN (sin cambios) ===")
        return

    # Traer datos con reintentos
    df = traer_con_reintentos()

    # Procesar con manejo de errores
    try:
        df = procesar(df)
    except Exception as e:
        logger.error(f"Error procesando: {e}")
        raise

    # Guardar
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SALIDA, index=False)
    logger.success(f"Guardado {df.shape[0]} filas en '{SALIDA}'")
    logger.success("=== Pipeline robusto: FIN ===")


if __name__ == "__main__":
    main()
