"""
DPL1046 · Clase 7 · 03_logging.py
Logging: un diario de lo que hace tu programa (en pantalla y en un archivo).

Córrelo con el botón ▶ o con:
    python clases/clase-07/material/03_logging.py
"""

import logging
import pandas as pd

# Configuración: qué nivel, qué formato y a dónde escribir
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("data/pipeline.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logging.info("Inicio del programa")

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
logging.info("Pedidos leídos: %s", len(orders))

sin_entrega = orders["order_delivered_customer_date"].isna().sum()
logging.warning("Pedidos sin fecha de entrega: %s", sin_entrega)

try:
    pd.read_csv("data/raw/no_existe.csv")
except FileNotFoundError:
    logging.error("No se encontró el archivo no_existe.csv")

logging.info("Fin del programa")
