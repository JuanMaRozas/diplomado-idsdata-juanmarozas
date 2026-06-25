"""
04_pipeline_produccion.py
==================================================================
CASO INTEGRADOR — El pipeline "de producción" completo.

Junta TODO lo de la noche en un solo programa que podrías agendar
para que corra cada madrugada sin que nadie lo mire:

  - Configuración externa (config.yaml)
  - Funciones con un solo trabajo cada una
  - Logging a CONSOLA y a ARCHIVO (salida/pipeline.log)
  - Reintentos ante fallas de la fuente
  - Validación de calidad (contrato de datos)
  - Idempotencia (re-ejecutar no duplica)
  - Un reporte final de negocio

Cómo correrlo:
    python 04_pipeline_produccion.py
==================================================================
"""

import time
from pathlib import Path

import pandas as pd
import yaml
from loguru import logger

from _datos_demo import generar_pedidos

BASE = Path(__file__).parent  # carpeta del script, sin importar desde dónde lo corras

# Logging también a archivo, con rotación (se parte solo si crece mucho)
(BASE / "salida").mkdir(exist_ok=True)
logger.add(BASE / "salida/pipeline.log", rotation="1 MB", level="INFO")


def leer_config(ruta="config.yaml") -> dict:
    with open(BASE / ruta, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def traer_con_reintentos(n, max_intentos=3) -> pd.DataFrame:
    for intento in range(1, max_intentos + 1):
        try:
            logger.info(f"Leyendo fuente (intento {intento})...")
            return generar_pedidos(n)
        except Exception as e:
            logger.warning(f"Falló intento {intento}: {e}")
            time.sleep(0.3 * intento)
    raise RuntimeError("Fuente inaccesible tras varios intentos")


def limpiar(df) -> pd.DataFrame:
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    df["city"] = df["city"].str.strip().str.lower()
    return df


def validar(df) -> None:
    assert pd.api.types.is_numeric_dtype(df["price"]), "price no es número"
    assert (df["price"] >= 0).all(), "hay precios negativos"
    assert df["rating"].between(1, 5).all(), "rating fuera de 1-5"
    logger.success("Contrato de datos: OK")


def resumir(df, umbral_caro) -> pd.DataFrame:
    df["es_caro"] = df["price"] > umbral_caro
    return (df.groupby("categoria")
              .agg(pedidos=("order_id", "count"),
                   precio_promedio=("price", "mean"),
                   rating_promedio=("rating", "mean"))
              .round(2)
              .sort_values("precio_promedio", ascending=False))


def main():
    logger.info("================ PIPELINE NOCTURNO: INICIO ================")
    cfg = leer_config()
    carpeta = BASE / cfg["salida"]["carpeta"]
    destino = carpeta / cfg["salida"]["archivo_resumen"]

    # Idempotencia
    if destino.exists():
        logger.info(f"'{destino}' ya existe hoy. No rehago. (idempotente)")
        logger.info("================ PIPELINE NOCTURNO: FIN ================")
        return

    df = traer_con_reintentos(cfg["entrada"]["n_pedidos"])
    df = limpiar(df)
    validar(df)
    resumen = resumir(df, cfg["reglas_negocio"]["umbral_caro"])

    carpeta.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(destino)
    logger.success(f"Reporte guardado en '{destino}'")

    print("\n========== REPORTE EJECUTIVO ==========")
    print(resumen)
    print("=======================================")

    logger.info("================ PIPELINE NOCTURNO: FIN ================")


if __name__ == "__main__":
    main()
