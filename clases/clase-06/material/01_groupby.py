"""
DPL1046 · Clase 6 · 01_groupby.py
Resumir una tabla: agrupar y calcular (groupby).

Córrelo con el botón ▶ o con:
    python clases/clase-06/material/01_groupby.py
"""

import pandas as pd

RUTA = "data/raw/"
pagos = pd.read_csv(RUTA + "olist_order_payments_dataset.csv")
clientes = pd.read_csv(RUTA + "olist_customers_dataset.csv")

# 1) Contar filas por grupo: ¿cuántos clientes hay en cada estado?
por_estado = clientes.groupby("customer_state").size()
print(por_estado.sort_values(ascending=False).head(5))

# 2) Una suma por grupo: ¿cuánto se pagó con cada medio de pago?
suma = pagos.groupby("payment_type")["payment_value"].sum()
print(suma.round(0))

# 3) Varios cálculos a la vez con .agg()
resumen = pagos.groupby("payment_type")["payment_value"].agg(["count", "sum", "mean"])
print(resumen.round(1))

# 4) Ordenar el resumen de mayor a menor
print(resumen.sort_values("sum", ascending=False).round(1))
