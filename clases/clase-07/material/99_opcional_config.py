"""
DPL1046 · Clase 7 (opcional) · 99_opcional_config.py
Configuración externa: los parámetros viven en config.yaml, no en el código.

Córrelo con el botón ▶ o con:
    python clases/clase-07/material/99_opcional_config.py
"""

import yaml
import pandas as pd

# 1) Leer el archivo de configuración
with open("clases/clase-07/material/config.yaml", encoding="utf-8") as archivo:
    config = yaml.safe_load(archivo)

print("Configuración leída:", config)

# 2) Usar los valores de la configuración
ruta = config["datos"]["carpeta"] + config["datos"]["pedidos"]
umbral = config["umbral_dias_lento"]

orders = pd.read_csv(ruta)
compra = pd.to_datetime(orders["order_purchase_timestamp"])
entrega = pd.to_datetime(orders["order_delivered_customer_date"])
dias = (entrega - compra).dt.days

print("Pedidos con entrega lenta (más de", umbral, "días):", (dias > umbral).sum())
