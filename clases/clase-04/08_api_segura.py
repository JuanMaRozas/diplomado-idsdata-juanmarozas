"""
08_api_segura.py
================
CLASE 4 · Lectura de Datos del Mundo Real (Bloque 2: APIs seguras)
DPL1046 · Programación en Python y Manipulación de Datos · UDLA

OBJETIVO DEL SCRIPT
-------------------
Mostrar las DOS prácticas de seguridad que separan a un principiante de un
profesional cuando se consumen APIs:

    1) NUNCA escribir claves/secretos dentro del código (hardcodear).
       En su lugar: guardarlos en un archivo .env y leerlos con python-dotenv.

    2) Reintentar con "backoff" cuando la API falla de forma temporal.
       Las APIs reales se caen a veces; un buen cliente reintenta con paciencia.

Para que sea reproducible en clase, golpeamos la misma API pública chilena
(https://mindicador.cl, que NO requiere clave). La cabecera Authorization que
construimos es ILUSTRATIVA: muestra el patrón exacto que usarías con una API
que sí pide token (CMF, SII, SAP, etc.), sin exponer ningún secreto real.

ARCHIVO .env (NO se sube a GitHub; va en .gitignore)
----------------------------------------------------
    API_KEY=tu_clave_secreta_aqui

CÓMO SE EJECUTA
---------------
    python clases/clase-04/08_api_segura.py
    (requests y python-dotenv ya están instalados desde la Clase 1)
"""

import logging
import os
import time

import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

URL_API = "https://mindicador.cl/api/dolar"
TIMEOUT_SEG = 10
MAX_INTENTOS = 3   # cuántas veces reintentar antes de rendirse


# ----------------------------------------------------------------------
# 1) LEER EL SECRETO DE FORMA SEGURA (no hardcodeado)
# ----------------------------------------------------------------------
def obtener_api_key() -> str:
    """Lee la clave desde el archivo .env, jamás desde el código.

    load_dotenv() busca un archivo .env en la carpeta y carga sus variables.
    os.getenv() las lee. Si no existe, devolvemos un placeholder para la demo.
    """
    load_dotenv()  # carga las variables del .env al entorno
    clave = os.getenv("API_KEY")
    if not clave:
        logging.warning("No hay API_KEY en .env -> uso una de demostración. "
                        "En un proyecto real, esto sería un error grave.")
        clave = "DEMO-KEY-ILUSTRATIVA"
    else:
        # Nunca imprimimos la clave completa: solo confirmamos que se cargó.
        logging.info("API_KEY cargada desde .env (termina en ...%s).", clave[-4:])
    return clave


# ----------------------------------------------------------------------
# 2) PEDIR DATOS CON REINTENTOS Y BACKOFF
# ----------------------------------------------------------------------
def get_con_reintentos(url: str, headers: dict) -> requests.Response | None:
    """Hace GET reintentando con espera creciente (1 s, 2 s, 4 s...).

    'Backoff exponencial' = cada reintento espera el doble. Le da tiempo a la
    API de recuperarse en vez de bombardearla con pedidos idénticos.
    """
    espera = 1
    for intento in range(1, MAX_INTENTOS + 1):
        try:
            logging.info("Intento %s de %s ...", intento, MAX_INTENTOS)
            r = requests.get(url, headers=headers, timeout=TIMEOUT_SEG)
            r.raise_for_status()
            logging.info("Éxito en el intento %s (código %s).", intento, r.status_code)
            return r
        except requests.exceptions.RequestException as e:
            logging.warning("Falló el intento %s: %s", intento, e)
            if intento < MAX_INTENTOS:
                logging.info("Espero %s s antes de reintentar...", espera)
                time.sleep(espera)
                espera *= 2   # 1 -> 2 -> 4 ... (esto es el "backoff")
    logging.error("Se agotaron los %s intentos. Me rindo ordenadamente.",
                  MAX_INTENTOS)
    return None


def main() -> None:
    logging.info("CLASE 4 · Consumiendo una API con secretos y reintentos")

    clave = obtener_api_key()

    # Patrón estándar de autenticación por token (Bearer).
    # Con una API real que pida clave, ESTA es la forma correcta de mandarla.
    headers = {
        "Authorization": f"Bearer {clave}",
        "Accept": "application/json",
    }

    respuesta = get_con_reintentos(URL_API, headers)
    if respuesta is None:
        return

    datos = respuesta.json()
    serie = datos.get("serie", [])
    if serie:
        ultimo = serie[0]
        logging.info("Dólar al %s: $%s", ultimo["fecha"][:10], ultimo["valor"])

    logging.info("Lección: el secreto vivió en .env, NUNCA en el código. "
                 "Y el cliente sobrevivió a fallas temporales reintentando.")


if __name__ == "__main__":
    main()
