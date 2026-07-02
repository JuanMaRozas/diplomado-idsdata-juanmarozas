"""
src/extraer.py · Extracción de datos
------------------------------------
Fuente 1: CSVs de Olist (e-commerce brasileño real)
Fuente 2: API mindicador.cl (tipo de cambio BRL→CLP)

Cumple el requisito de ≥2 fuentes reales.
"""

import os
import requests
import urllib3
import pandas as pd
from loguru import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def extraer_olist(carpeta):
    """Lee los CSVs de Olist necesarios para el análisis de demanda."""
    obligatorios = {
        "pedidos": "olist_orders_dataset.csv",
        "items": "olist_order_items_dataset.csv",
    }
    for nombre, archivo in obligatorios.items():
        ruta = os.path.join(carpeta, archivo)
        if not os.path.exists(ruta):
            raise FileNotFoundError(
                f"No encontré '{archivo}' en '{carpeta}'. "
                f"Descarga el dataset de Olist de Kaggle y ponlo ahí."
            )

    pedidos = pd.read_csv(os.path.join(carpeta, obligatorios["pedidos"]))
    items = pd.read_csv(os.path.join(carpeta, obligatorios["items"]))

    # Categorías es opcional (no todos los mirrors del dataset lo traen)
    ruta_cat = os.path.join(carpeta, "product_category_name_translation.csv")
    if os.path.exists(ruta_cat):
        categorias = pd.read_csv(ruta_cat)
        logger.info(f"Olist cargado: {len(pedidos)} pedidos, {len(items)} items, "
                    f"{len(categorias)} categorías.")
    else:
        categorias = pd.DataFrame()
        logger.info(f"Olist cargado: {len(pedidos)} pedidos, {len(items)} items "
                    f"(sin archivo de categorías, no afecta el análisis).")

    return pedidos, items, categorias


def extraer_tipo_cambio(moneda="dolar"):
    """Pide el tipo de cambio actual a mindicador.cl (API real, sin llave).

    Devuelve el valor del dólar en CLP. Como Olist maneja BRL (real brasileño),
    usamos una conversión aproximada: 1 BRL ≈ 0.19 USD → multiplicamos.
    """
    url = f"https://mindicador.cl/api/{moneda}"
    try:
        r = requests.get(url, timeout=10, verify=False)
        r.raise_for_status()
        valor_usd_clp = r.json()["serie"][0]["valor"]
        # 1 BRL ≈ 0.19 USD (promedio histórico), entonces:
        brl_a_clp = valor_usd_clp * 0.19
        logger.info(f"Tipo de cambio obtenido: 1 USD = ${valor_usd_clp:.1f} CLP → "
                    f"1 BRL ≈ ${brl_a_clp:.1f} CLP")
        return brl_a_clp
    except Exception as e:
        logger.warning(f"No se pudo obtener tipo de cambio real: {e}. Usando fallback.")
        return 180.0  # fallback razonable: 1 BRL ≈ 180 CLP


if __name__ == "__main__":
    tc = extraer_tipo_cambio()
    print(f"1 BRL = ${tc:.1f} CLP")
