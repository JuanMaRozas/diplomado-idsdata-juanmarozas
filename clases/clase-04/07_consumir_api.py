"""
07_consumir_api.py
==================
CLASE 4 · Lectura de Datos del Mundo Real (Bloque 2: APIs)
DPL1046 · Programación en Python y Manipulación de Datos · UDLA

OBJETIVO DEL SCRIPT
-------------------
Consumir una API REAL, pública y chilena, SIN autenticación, para que el
alumno principiante vea de punta a punta cómo se traen datos desde internet
a Python y se convierten en una tabla de pandas.

Usamos https://mindicador.cl  -> indicadores económicos de Chile
(dólar, euro, UF, UTM...). Es gratuita, no pide clave y devuelve JSON.

CONCEPTOS QUE MUESTRA
---------------------
    - requests.get()        -> "tocar la puerta" de la API
    - timeout               -> no esperar para siempre si no responde
    - response.status_code  -> 200 = OK, 404 = no existe, 500 = error servidor
    - response.json()       -> convertir la respuesta en dict de Python
    - try/except            -> sobrevivir si no hay internet (visto en Clase 3)

CÓMO SE EJECUTA
---------------
    python clases/clase-04/07_consumir_api.py
    (requests ya está instalado desde la Clase 1)
"""

import logging

import pandas as pd
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

# URL base de la API. Una API REST es solo una dirección web que devuelve datos.
URL_API = "https://mindicador.cl/api"
TIMEOUT_SEG = 10   # si en 10 s no responde, cortamos. NUNCA dejar sin timeout.


def consultar_indicadores() -> dict | None:
    """Le pide a la API el resumen de indicadores del día.

    Devuelve el JSON ya convertido a diccionario, o None si algo falló.
    Toda la lógica de red va dentro de try/except: la red SIEMPRE puede fallar.
    """
    logging.info("Consultando %s ...", URL_API)
    try:
        # GET = "dame datos". Es como escribir la URL en el navegador.
        respuesta = requests.get(URL_API, timeout=TIMEOUT_SEG)

        # raise_for_status() lanza un error si el código NO es 2xx (ej. 404, 500).
        respuesta.raise_for_status()

        logging.info("La API respondió con código %s (OK).", respuesta.status_code)
        return respuesta.json()   # convierte el texto JSON en dict de Python

    except requests.exceptions.Timeout:
        logging.error("La API tardó más de %s s. ¿Internet lento?", TIMEOUT_SEG)
    except requests.exceptions.ConnectionError:
        logging.error("No hay conexión. ¿Estás conectado a internet?")
    except requests.exceptions.HTTPError as e:
        logging.error("La API respondió con error: %s", e)
    return None


def a_tabla(datos: dict) -> pd.DataFrame:
    """Toma el dict de la API y arma una tabla simple con los indicadores clave."""
    # En el JSON de mindicador, cada indicador es un sub-diccionario con 'valor'.
    indicadores = ["dolar", "euro", "uf", "utm"]
    filas = []
    for nombre in indicadores:
        if nombre in datos:
            filas.append(
                {
                    "indicador": datos[nombre]["nombre"],
                    "valor": datos[nombre]["valor"],
                    "fecha": datos[nombre]["fecha"][:10],  # solo la fecha, sin hora
                }
            )
    return pd.DataFrame(filas)


def main() -> None:
    logging.info("CLASE 4 · Trayendo datos económicos de Chile desde una API")
    datos = consultar_indicadores()

    if datos is None:
        logging.warning("No se pudieron obtener datos. El pipeline NO se cae: "
                        "simplemente avisa y termina ordenado.")
        return

    df = a_tabla(datos)
    logging.info("Indicadores del %s:", datos.get("fecha", "")[:10])
    print(df.to_string(index=False))
    logging.info("Eso es todo: internet -> JSON -> dict -> DataFrame de pandas.")


if __name__ == "__main__":
    main()
