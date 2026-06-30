"""
02_paginacion.py  ·  Clase 7 · Bloque 1 (Pedir)
-----------------------------------------------
Las APIs reales no te dan 100.000 registros de una sola vez: te los entregan
POR PÁGINAS. Aquí usamos una API real, pública y sin llave (PokeAPI) que entrega
miles de registros de a 20. El patrón es IDÉNTICO en cualquier API industrial
(SII, Banco Mundial, ERP): solo cambia la dirección.
Esta API usa paginación "por cursor": en cada respuesta viene un campo 'next'
con la URL de la página siguiente. Cuando 'next' es None, no hay más páginas.
"""
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from loguru import logger
URL_INICIAL = "https://pokeapi.co/api/v2/pokemon?limit=20"
MAX_PAGINAS = 5     # tope de seguridad para la clase (si no, traería miles)
def traer_todo():
    """Patrón de paginación por cursor: seguir el campo 'next' hasta que sea None."""
    todos = []
    url = URL_INICIAL
    pagina = 0
    while url and pagina < MAX_PAGINAS:
        pagina += 1
        logger.info(f"Pidiendo página {pagina}: {url}")
        respuesta = requests.get(url, timeout=10, verify=False)
        respuesta.raise_for_status()
        datos = respuesta.json()
        todos.extend(datos["results"])                 # acumulamos lo recibido
        logger.info(f"  -> +{len(datos['results'])} registros (total: {len(todos)})")
        url = datos["next"]    # <- la API nos dice cuál es la página siguiente
        if url is None:
            logger.success("La API respondió next=None: no hay más páginas.")
    return todos, datos["count"]
def main():
    logger.info("=== Trayendo registros página por página (API real) ===")
    registros, total_disponible = traer_todo()
    logger.success(f"Traídos {len(registros)} de {total_disponible} registros disponibles "
                   f"(cortamos en {MAX_PAGINAS} páginas para la clase).")
    df = pd.DataFrame(registros)
    print("\nPrimeras 5 filas de la tabla final:")
    print(df.head().to_string(index=False))
    print(f"\nForma: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(f"Si quitáramos el tope, el bucle seguiría hasta traer los {total_disponible}.")
if __name__ == "__main__":
    main()
