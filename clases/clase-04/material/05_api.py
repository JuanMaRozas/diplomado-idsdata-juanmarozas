"""
DPL1046 · Clase 4 · 05_api.py
Consumir una API pública real: mindicador.cl (indicadores de Chile).
No necesita clave. Necesita internet.

Córrelo con el botón ▶ o con:
    python clases/clase-04/material/05_api.py
"""

import requests
import pandas as pd

URL = "https://mindicador.cl/api"

try:
    respuesta = requests.get(URL, timeout=10)    # pedimos los datos
    respuesta.raise_for_status()                 # si hubo error, avisa
    print("Código de respuesta:", respuesta.status_code)

    datos = respuesta.json()                     # texto JSON -> diccionario
    print("Dólar hoy:", datos["dolar"]["valor"])
    print("UF hoy:", datos["uf"]["valor"])

    filas = []
    for nombre in ["dolar", "euro", "uf", "utm"]:
        filas.append({"indicador": nombre, "valor": datos[nombre]["valor"]})
    tabla = pd.DataFrame(filas)
    print(tabla)

except requests.exceptions.RequestException:
    print("No pude conectar con la API. Revisa tu internet y vuelve a intentar.")
