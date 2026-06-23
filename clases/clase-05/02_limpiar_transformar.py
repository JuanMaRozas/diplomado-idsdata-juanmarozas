"""
02_limpiar_transformar.py  ·  Clase 5 · Bloque 2
====================================================================
OBJETIVO: convertir datos sucios en datos usables. El 80% del trabajo real.

Lo que demuestra este script, paso a paso:
  1. Diagnóstico: df.info() y df.isna().sum() (ver tipos y vacíos).
  2. Nulos: fillna (rellenar) y dropna (descartar).
  3. Tipos: 'price' de texto a número; fecha de texto a datetime y sacar el mes.
  4. Columna nueva SIN for: total = price + freight, y clasificar caro/barato.
  5. Texto: .str.strip().str.lower() para que "SP" y " sao paulo " no peleen.

Cómo correrlo:
    python 02_limpiar_transformar.py
====================================================================
"""

import logging
import numpy as np
import pandas as pd

from _datos_demo import tabla_pedidos

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    df = tabla_pedidos()   # datos a propósito SUCIOS (nulos, texto, fechas-texto)

    # ---- 1) Diagnóstico: ¿en qué estado llega el dato? ---------------------
    logging.info("=== 1) Diagnóstico (mirar antes de limpiar) ===")
    logging.info("Tipos de cada columna:\n%s", df.dtypes.to_string())
    logging.info("\nVacíos (nulos) por columna:\n%s\n", df.isna().sum().to_string())

    # ---- 2) Tipos: texto -> número, y texto -> fecha -----------------------
    logging.info("=== 2) Arreglar tipos ===")
    # 'price' viene como texto: a número. errors='coerce' deja NaN lo que no se pueda.
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    # fecha de texto a fecha real -> ahora podemos sacar el mes
    df["fecha_compra"] = pd.to_datetime(df["fecha_compra"])
    df["mes"] = df["fecha_compra"].dt.month
    logging.info("price ahora es: %s | fecha ahora es: %s",
                 df["price"].dtype, df["fecha_compra"].dtype)
    logging.info("Ejemplo de mes extraído: %s\n", df["mes"].head(3).tolist())

    # ---- 3) Nulos: rellenar o descartar (es una DECISIÓN) ------------------
    logging.info("=== 3) Manejar nulos ===")
    nulos_price = int(df["price"].isna().sum())
    logging.info("Nulos en price antes: %d", nulos_price)
    # Decisión: el flete vacío lo interpretamos como 0 (no hubo costo de envío).
    df["freight_value"] = df["freight_value"].fillna(0)
    # Decisión: una fila sin precio no sirve para análisis de ventas -> la descartamos.
    df = df.dropna(subset=["price"])
    logging.info("Filas tras descartar precios nulos: %d\n", len(df))

    # ---- 4) Columna nueva SIN for (vectorización) --------------------------
    logging.info("=== 4) Crear columnas nuevas (sin un solo for) ===")
    df["total"] = df["price"] + df["freight_value"]            # de golpe, toda la columna
    df["tipo"] = np.where(df["price"] > 100, "caro", "barato")  # clasificar por regla
    logging.info("Nuevas columnas total/tipo:\n%s\n",
                 df[["price", "freight_value", "total", "tipo"]].head(3).to_string(index=False))

# ---- 5) Limpiar texto para que los grupos no se partan -----------------
    logging.info("=== 5) Normalizar texto ===")
    antes = df["city"].nunique()
    
    # 1. Pasamos a minúsculas.
    # 2. Quitamos espacios en blanco sucios.
    # 3. ¡Usamos .str.replace() para matar el acento de la 'ã'!
    df["city"] = (
        df["city"]
        .str.lower()
        .str.strip()
        .str.replace("ã", "a", regex=False)
    )
    
    despues = df["city"].nunique()
    logging.info("Ciudades distintas antes: %d  ->  después de limpiar: %d", antes, despues)
    logging.info("(Ahora 'SP', ' sp ' y 'São Paulo' se unificaron correctamente)\n")

    logging.info("Listo ✅  Dato limpio = análisis confiable. 'Garbage in, garbage out'.")


if __name__ == "__main__":
    main()
