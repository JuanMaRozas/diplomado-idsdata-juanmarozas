"""
DPL1046 · Clase 8 (extra, opcional) · 05_resumen_ejecutivo.py
Pandas calcula los números, la IA los explica. Nunca al revés.

Córrelo con el botón ▶ o con:
    python clases/clase-08/material/extra/05_resumen_ejecutivo.py
"""

import requests
import pandas as pd

URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"

# 1) Pandas calcula los números (la IA NO calcula)
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
entregados = orders[orders["order_status"] == "delivered"].dropna(
    subset=["order_delivered_customer_date"]
)
compra = pd.to_datetime(entregados["order_purchase_timestamp"])
entrega = pd.to_datetime(entregados["order_delivered_customer_date"])
dias = (entrega - compra).dt.days

promedio = round(dias.mean(), 1)
lentos = round((dias > 20).mean() * 100, 1)
print("Promedio de días de entrega:", promedio)
print("Porcentaje de entregas lentas (más de 20 días):", lentos)

# 2) Le damos a la IA SOLO esos números y le pedimos redactar
prompt = (
    "Eres analista de datos. Escribe un resumen ejecutivo de 3 líneas en español, "
    "usando SOLO estos datos, sin inventar otros:\n"
    f"- Promedio de días de entrega: {promedio}\n"
    f"- Entregas lentas (más de 20 días): {lentos}%\n"
)

try:
    respuesta = requests.post(
        URL, json={"model": MODELO, "prompt": prompt, "stream": False}, timeout=120
    )
    respuesta.raise_for_status()
    print("\nResumen ejecutivo (IA):")
    print(respuesta.json()["response"].strip())
except requests.exceptions.RequestException:
    print("\nNo encontré Ollama. Resumen simulado:")
    print(f"Las entregas tardan {promedio} días en promedio y {lentos}% supera los 20 días.")
