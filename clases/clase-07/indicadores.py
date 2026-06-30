"""
indicadores.py  ·  Clase 7  ·  MÓDULO REUTILIZABLE (APIs reales)
----------------------------------------------------------------
Este archivo es una "caja de herramientas": guarda las funciones para pedir
indicadores económicos reales a la API pública de Chile https://mindicador.cl
(dólar, UF, etc.). NO pide llave: es abierta.
Sirve para DOS cosas, y esa es la lección de buenas prácticas de hoy:
  1) Se puede EJECUTAR:   python indicadores.py     -> corre la demo de abajo.
  2) Se puede IMPORTAR:   from indicadores import pedir_indicador
     ...y entonces la demo de abajo NO se ejecuta. Solo te llevas la función.
Lo que hace esa magia es la última línea:  if __name__ == "__main__": main()
(lo explicamos en detalle en 06_reutilizar.py).
"""
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from loguru import logger
BASE = "https://mindicador.cl/api"
def pedir_indicador(nombre, reintentos=3):
    """Pide un indicador REAL a mindicador.cl y devuelve el JSON (un dict).
    'nombre' puede ser: "dolar", "uf", "utm", "euro", "ipc", etc.
    Incluye reintentos con espera creciente (backoff), como en la Clase 6,
    porque una API real a veces no responde a la primera.
    """
    url = f"{BASE}/{nombre}"
    for intento in range(1, reintentos + 1):
        try:
            respuesta = requests.get(url, timeout=10, verify=False)
            respuesta.raise_for_status()      # si el servidor respondió mal, avisa
            return respuesta.json()           # convierte el texto JSON en dict
        except Exception as e:
            logger.warning(f"Intento {intento} falló para '{nombre}': {e}")
            time.sleep(0.5 * intento)         # backoff: espera cada vez un poco más
    raise RuntimeError(f"No se pudo obtener '{nombre}' tras {reintentos} intentos")
def a_tabla(datos, nombre_columna):
    """Convierte el JSON de la API en una tabla de pandas: fecha + <nombre_columna>.
    El dato útil viene escondido dentro de la clave 'serie' (una lista de dicts).
    """
    df = pd.DataFrame(datos["serie"])                  # la tabla está en 'serie'
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.date  # de texto largo a fecha real
    df = df.rename(columns={"valor": nombre_columna})  # nombre claro
    return df[["fecha", nombre_columna]].sort_values("fecha").reset_index(drop=True)
def main():
    """Demo del módulo. SOLO corre si ejecutas este archivo directamente."""
    logger.info("Corriendo indicadores.py como PROGRAMA PRINCIPAL (no fue importado).")
    datos = pedir_indicador("dolar")
    tabla = a_tabla(datos, "dolar_clp")
    logger.success(f"Dólar: {len(tabla)} días obtenidos de la API real.")
    print(tabla.tail(5).to_string(index=False))
if __name__ == "__main__":
    main()
