"""
00_primer_request.py  ·  Clase 7 · Bloque 1 (Pedir)
---------------------------------------------------
El "hola mundo" de una API REAL: le pedimos a mindicador.cl (Banco Central de
Chile) el valor del dólar de hoy y lo mostramos. Sin pandas todavía: solo
entender qué es pedir datos a una API y qué nos devuelve (un JSON).
Necesitas internet. La API es pública y NO pide llave.
"""
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from loguru import logger
URL = "https://mindicador.cl/api/dolar"
def pedir_dolar():
    """Pide los datos del dólar a la API real. Devuelve un dict (el JSON)."""
    logger.info(f"Pidiendo datos a {URL} ...")
    respuesta = requests.get(URL, timeout=10, verify=False)
    respuesta.raise_for_status()                # si el servidor respondió mal, avisa
    return respuesta.json()                      # convierte el texto JSON en dict
def main():
    logger.info("=== Primer request a una API real ===")
    datos = pedir_dolar()
    # 'datos' es un diccionario de Python (lo vimos en la Clase 2)
    logger.info(f"Indicador: {datos['nombre']} (en {datos['unidad_medida']})")
    # La lista de valores históricos viene en la clave 'serie'.
    # El primero de la lista es el más reciente.
    hoy = datos["serie"][0]
    logger.success(f"Valor más reciente: ${hoy['valor']} CLP  (fecha {hoy['fecha'][:10]})")
    print("\nAsí se ve el JSON crudo que devolvió la API (algunas claves):")
    print({k: datos[k] for k in ["codigo", "nombre", "unidad_medida"]})
    print("serie -> lista de", len(datos["serie"]), "valores; el primero es:", datos["serie"][0])
if __name__ == "__main__":
    main()
