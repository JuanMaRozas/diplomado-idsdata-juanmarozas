"""
DPL1046 · Clase 5 · 06_secretos_env.py
Guardar un secreto (clave de una API) FUERA del código, en el archivo .env.

Antes de correrlo, crea el archivo .env en la raíz del repo:
    echo "API_KEY=clave_de_ejemplo_1234" > .env

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/06_secretos_env.py
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()                      # lee el archivo .env
clave = os.getenv("API_KEY")       # busca la variable API_KEY

if clave is None:
    print("No hay API_KEY en tu archivo .env")
    print("Crea el archivo .env en la raíz del repo (ver el comando arriba).")
else:
    print("Clave cargada. Termina en:", clave[-4:])
    cabeceras = {"Authorization": "Bearer " + clave}
    try:
        r = requests.get("https://mindicador.cl/api/dolar",
                         headers=cabeceras, timeout=10)
        r.raise_for_status()
        ultimo = r.json()["serie"][0]
        print("Dólar al", ultimo["fecha"][:10], ":", ultimo["valor"])
    except requests.exceptions.RequestException:
        print("No pude conectar con la API.")
