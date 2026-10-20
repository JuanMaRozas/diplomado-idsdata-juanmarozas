"""
DPL1046 · Clase 4 · 04_parquet.py
Parquet: un formato más liviano y rápido que el CSV.
Necesita pyarrow:  pip install -r clases/clase-04/material/requirements.txt

Córrelo con el botón ▶ o con:
    python clases/clase-04/material/04_parquet.py
"""

import os
import pandas as pd

RUTA = "data/raw/"
pagos = pd.read_csv(RUTA + "olist_order_payments_dataset.csv")

pagos.to_parquet("data/pagos.parquet", index=False)   # guarda en Parquet
leido = pd.read_parquet("data/pagos.parquet")         # lo vuelve a leer
print("Filas leídas desde Parquet:", len(leido))

tam_csv = os.path.getsize(RUTA + "olist_order_payments_dataset.csv") / 1_000_000
tam_pq = os.path.getsize("data/pagos.parquet") / 1_000_000
print("Tamaño del CSV (MB):", round(tam_csv, 1))
print("Tamaño del Parquet (MB):", round(tam_pq, 1))
