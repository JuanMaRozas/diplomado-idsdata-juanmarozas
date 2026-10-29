"""
DPL1046 · Clase 8 (extra, opcional) · 02_dos_fuentes.py
Combinar DOS fuentes: ventas de Olist (CSV) + dólar de Chile (API).

Córrelo con el botón ▶ o con:
    python clases/clase-08/material/extra/02_dos_fuentes.py
"""

import requests
import pandas as pd

RUTA = "data/raw/"

# ---- Fuente 1: ventas por mes desde los CSV de Olist ------------------------
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
items = pd.read_csv(RUTA + "olist_order_items_dataset.csv")

tabla = items.merge(orders, on="order_id", how="inner")
tabla["mes"] = pd.to_datetime(tabla["order_purchase_timestamp"]).dt.strftime("%Y-%m")
ventas = tabla.groupby("mes")["price"].sum().round(0).reset_index()
ventas = ventas[ventas["mes"].str.startswith("2017")]
print("Ventas por mes (2017):", len(ventas), "meses")

# ---- Fuente 2: dólar diario de 2017 desde la API ----------------------------
try:
    respuesta = requests.get("https://mindicador.cl/api/dolar/2017", timeout=15)
    respuesta.raise_for_status()
    serie = respuesta.json()["serie"]            # lista de {"fecha", "valor"}

    dolar = pd.DataFrame(serie)
    dolar["mes"] = pd.to_datetime(dolar["fecha"]).dt.strftime("%Y-%m")
    dolar_mes = dolar.groupby("mes")["valor"].mean().round(1).reset_index()
    dolar_mes = dolar_mes.rename(columns={"valor": "dolar_clp"})

    # ---- Combinar: una fila por mes con las dos fuentes ---------------------
    combinada = ventas.merge(dolar_mes, on="mes", how="left")
    print(combinada)
except requests.exceptions.RequestException:
    print("No pude conectar con la API. Las ventas sí se calcularon:")
    print(ventas)
