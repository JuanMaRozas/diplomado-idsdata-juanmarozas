"""
06_leer_formatos.py
====================
CLASE 4 · Lectura de Datos del Mundo Real (Bloque 1: Archivos)
DPL1046 · Programación en Python y Manipulación de Datos · UDLA

OBJETIVO DEL SCRIPT
-------------------
Mostrar, con casos concretos, cómo se leen los CUATRO formatos de archivo
que un ingeniero de datos encuentra todos los días en la industria:

    1) CSV     -> el formato más común (texto plano separado por comas)
    2) Excel   -> reportes corporativos, casi siempre con varias hojas
    3) JSON    -> respuestas de APIs y sistemas web (datos "anidados")
    4) Parquet -> el formato preferido en la nube (comprimido y rápido)

Está pensado para un curso 100% principiante: cada sección imprime en
pantalla QUÉ está haciendo y POR QUÉ, para que se vea el resultado en vivo.

CÓMO SE EJECUTA
---------------
    python clases/clase-04/06_leer_formatos.py

El script es AUTOSUFICIENTE: si no encuentra el dataset Olist, igual corre,
porque crea sus propios archivos de demostración (Excel y JSON) en la
carpeta data/demo/. Si Olist está en data/raw/, además lo usa para el CSV
avanzado y para convertirlo a Parquet.
"""

import json
import logging
from pathlib import Path

import pandas as pd

# ----------------------------------------------------------------------
# Configuración de logging (igual que en la Clase 3: dejar rastro, no print)
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

# Carpetas del proyecto. Path() permite armar rutas sin preocuparse del SO.
RAIZ = Path(__file__).resolve().parents[2]   # sube de clase-04 -> clases -> raíz
DATA_RAW = RAIZ / "data" / "raw"             # aquí vive el dataset Olist
DATA_DEMO = RAIZ / "data" / "demo"           # aquí creamos archivos de ejemplo
DATA_DEMO.mkdir(parents=True, exist_ok=True)


# ======================================================================
# 1) CSV AVANZADO
# ======================================================================
def leer_csv_avanzado() -> None:
    """Lee un CSV controlando encoding, separador, tipos y columnas.

    La mayoría aprende read_csv() "pelado". En la industria, un CSV real
    casi nunca viene limpio: trae acentos (encoding), a veces usa ';' en
    vez de ',', y conviene leer solo las columnas que se necesitan.
    """
    logging.info("=" * 60)
    logging.info("1) CSV AVANZADO con pandas.read_csv()")

    ruta = DATA_RAW / "olist_order_payments_dataset.csv"
    if not ruta.exists():
        logging.warning("No se encontró Olist (%s). Uso un CSV de ejemplo.", ruta)
        # Creamos un CSV chiquito a mano para que el script corra igual.
        ruta = DATA_DEMO / "pagos_demo.csv"
        ruta.write_text(
            "order_id,payment_type,payment_value\n"
            "abc,credit_card,150.0\n"
            "def,boleto,89.9\n",
            encoding="utf-8",
        )

    # Parámetros clave de read_csv (los que más se usan en la vida real):
    df = pd.read_csv(
        ruta,
        sep=",",            # separador de columnas (a veces es ';' en Chile/Excel)
        encoding="utf-8",   # cómo están codificados los acentos y la ñ
        usecols=None,       # podríamos pasar ["col1","col2"] para leer menos
        nrows=None,         # podríamos pasar 1000 para "espiar" un archivo enorme
    )
    logging.info("Leídas %s filas y %s columnas.", f"{len(df):,}", df.shape[1])
    logging.info("Primeras columnas: %s", list(df.columns)[:5])
    # head() muestra las primeras filas: el primer gesto al abrir cualquier dato.
    print(df.head(3).to_string(index=False))


# ======================================================================
# 2) EXCEL CON VARIAS HOJAS
# ======================================================================
def leer_excel_multihoja() -> None:
    """Crea un Excel con 2 hojas y luego lo lee hoja por hoja.

    Los reportes de gerencia casi siempre llegan en Excel con MUCHAS hojas
    (una por mes, una por sucursal...). Hay que saber elegir la hoja.
    """
    logging.info("=" * 60)
    logging.info("2) EXCEL con múltiples hojas (openpyxl por detrás)")

    ruta = DATA_DEMO / "reporte_demo.xlsx"

    # --- Creamos el Excel de ejemplo (esto simula el reporte que nos mandan) ---
    ventas = pd.DataFrame(
        {"region": ["RM", "Biobío", "Valpo"], "ventas": [1200, 800, 950]}
    )
    clientes = pd.DataFrame(
        {"region": ["RM", "Biobío", "Valpo"], "clientes": [45, 30, 38]}
    )
    with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
        ventas.to_excel(writer, sheet_name="Ventas", index=False)
        clientes.to_excel(writer, sheet_name="Clientes", index=False)
    logging.info("Excel de ejemplo creado en %s con 2 hojas.", ruta.name)

    # --- Ahora lo LEEMOS, que es lo que haríamos con un reporte real ---
    # Paso A: averiguar qué hojas tiene (no asumir).
    hojas = pd.ExcelFile(ruta).sheet_names
    logging.info("Hojas disponibles: %s", hojas)

    # Paso B: leer una hoja específica por su nombre.
    df_ventas = pd.read_excel(ruta, sheet_name="Ventas")
    logging.info("Hoja 'Ventas' -> %s filas.", len(df_ventas))
    print(df_ventas.to_string(index=False))


# ======================================================================
# 3) JSON ANIDADO (como el que devuelve una API)
# ======================================================================
def leer_json_anidado() -> None:
    """Parsea un JSON con estructura anidada y lo aplana a una tabla.

    Las APIs no devuelven tablas: devuelven JSON, que son diccionarios y
    listas anidadas (cajas dentro de cajas). El truco es json_normalize().
    """
    logging.info("=" * 60)
    logging.info("3) JSON ANIDADO -> tabla con pd.json_normalize()")

    # Simulamos la respuesta de una API (un dict de Python = un JSON).
    respuesta_api = {
        "empresa": "Amisoft",
        "proyectos": [
            {"cliente": "Minera Norte", "sector": "minería", "monto": 50000},
            {"cliente": "Retail Sur", "sector": "retail", "monto": 32000},
        ],
    }

    # Guardamos y volvemos a leer el JSON, para mostrar el ciclo completo.
    ruta = DATA_DEMO / "api_demo.json"
    ruta.write_text(json.dumps(respuesta_api, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    datos = json.loads(ruta.read_text(encoding="utf-8"))

    # json_normalize "aplana" la lista anidada en una tabla ordenada.
    df = pd.json_normalize(datos["proyectos"])
    logging.info("JSON anidado convertido a tabla de %s filas.", len(df))
    print(df.to_string(index=False))


# ======================================================================
# 4) PARQUET (el formato del cloud)
# ======================================================================
def demostrar_parquet() -> None:
    """Escribe y lee Parquet, y compara su tamaño contra CSV.

    Parquet es columnar y comprimido: pesa mucho menos y se lee mucho más
    rápido que un CSV. Por eso AWS/Azure/GCP lo prefieren.
    """
    logging.info("=" * 60)
    logging.info("4) PARQUET vs CSV (tamaño y velocidad)")

    # Tomamos una tabla cualquiera (Olist si está; si no, una de ejemplo).
    ruta_csv = DATA_RAW / "olist_order_payments_dataset.csv"
    if ruta_csv.exists():
        df = pd.read_csv(ruta_csv)
    else:
        # Datos parecidos a los reales: columnas de texto que se repiten mucho.
        # Ahí es donde Parquet comprime y le gana al CSV con claridad.
        n = 100_000
        df = pd.DataFrame(
            {
                "order_id": [f"ord_{i}" for i in range(n)],
                "payment_type": ["credit_card", "boleto", "voucher", "debit_card"]
                * (n // 4),
                "payment_value": [99.9, 150.0, 32.5, 12.0] * (n // 4),
            }
        )

    csv_out = DATA_DEMO / "tabla.csv"
    pq_out = DATA_DEMO / "tabla.parquet"
    df.to_csv(csv_out, index=False)
    try:
        df.to_parquet(pq_out, index=False)   # requiere pyarrow instalado
    except Exception as e:  # noqa: BLE001  (en clase: explicar el mensaje)
        logging.error("No se pudo escribir Parquet: %s", e)
        logging.error("Instala el motor con: pip install pyarrow")
        return

    mb = 1024 * 1024
    logging.info("CSV     pesa %.2f MB", csv_out.stat().st_size / mb)
    logging.info("Parquet pesa %.2f MB", pq_out.stat().st_size / mb)

    # Y se lee igual de fácil que un CSV:
    df_leido = pd.read_parquet(pq_out)
    logging.info("Parquet releído -> %s filas. Mismo dato, menos peso.",
                 f"{len(df_leido):,}")


# ======================================================================
# PROGRAMA PRINCIPAL
# ======================================================================
def main() -> None:
    logging.info("CLASE 4 · Leyendo el mundo real en 4 formatos")
    leer_csv_avanzado()
    leer_excel_multihoja()
    leer_json_anidado()
    demostrar_parquet()
    logging.info("=" * 60)
    logging.info("Listo. Un mismo ingeniero, cuatro formatos, una sola idea: "
                 "todo termina en un DataFrame de pandas.")


if __name__ == "__main__":
    main()
