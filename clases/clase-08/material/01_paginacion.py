"""
DPL1046 · Clase 8 · 01_paginacion.py
Paginación: una API que entrega los datos por partes (páginas).

Usamos PokeAPI (pública, sin clave). El patrón es el mismo en cualquier API.

Córrelo con el botón ▶ o con:
    python clases/clase-08/material/01_paginacion.py
"""

import requests
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon?limit=20"   # 20 registros por página
MAX_PAGINAS = 3                                       # tope para la clase
registros = []
pagina = 0

try:
    # Mientras exista una "página siguiente", seguimos pidiendo
    while url and pagina < MAX_PAGINAS:
        pagina = pagina + 1
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        registros.extend(datos["results"])   # sumamos lo que llegó a la lista
        print("Página", pagina, "→ total acumulado:", len(registros))

        url = datos["next"]                  # la API nos dice cuál es la siguiente

    tabla = pd.DataFrame(registros)
    print(tabla.head(3))
    print("Filas en la tabla final:", len(tabla))
except requests.exceptions.RequestException:
    print("No pude conectar con la API. Revisa tu internet y vuelve a intentarlo.")
