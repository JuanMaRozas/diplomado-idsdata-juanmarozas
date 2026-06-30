"""
05_enriquecer_con_ia.py  ·  Clase 7 · Bloque 3 (Enriquecer con IA)
------------------------------------------------------------------
La idea central de hoy: UNA IA ES SOLO OTRA API. Le mandas una instrucción
(un "prompt") y te devuelve una respuesta. Es la API más poderosa que llamarás.

Tenemos una tabla de gastos con DESCRIPCIONES en texto libre (como las que llegan
de un banco o un ERP). Le pedimos a un modelo real (Claude, de Anthropic) que
clasifique cada gasto en una CATEGORÍA. Eso es ENRIQUECER: crear una columna
nueva que ninguna fuente traía.

⚠️ NECESITAS UNA API KEY. Va en un archivo .env en la raíz del proyecto, NUNCA en el código:
      1) Crea un archivo .env con:   ANTHROPIC_API_KEY=sk-ant-tu-llave-aquí
      2) Agrega .env a tu .gitignore (para no subirla a GitHub)
      3) Este script la lee automáticamente con python-dotenv.
   (Equivalente con OpenAI: usar el SDK 'openai' y OPENAI_API_KEY. Ver comentario.)
"""

import os
import httpx
from dotenv import load_dotenv
import pandas as pd
from loguru import logger
import anthropic

load_dotenv()

MODELO = "claude-haiku-4-5-20251001"   # modelo chico y barato, ideal para clasificar
CATEGORIAS = ["Transporte", "Tecnología", "Alimentación", "Entretenimiento",
              "Combustible", "Otros"]

# Datos de ejemplo: descripciones de gasto en texto libre.
GASTOS = [
    {"id": 1, "monto": 12990,  "descripcion": "Pago Uber viaje al aeropuerto"},
    {"id": 2, "monto": 899000, "descripcion": "Compra notebook Lenovo en Falabella"},
    {"id": 3, "monto": 8500,   "descripcion": "Almuerzo restaurant peruano centro"},
    {"id": 4, "monto": 5990,   "descripcion": "Suscripcion mensual Netflix"},
    {"id": 5, "monto": 45200,  "descripcion": "Bencina Copec estacion ruta 68"},
    {"id": 6, "monto": 23000,  "descripcion": "Mouse y teclado inalambrico PCFactory"},
    {"id": 7, "monto": 3200,   "descripcion": "Metro tarjeta bip recarga"},
    {"id": 8, "monto": 15990,  "descripcion": "Delivery pizza familiar"},
]

def clasificar(texto, cliente):
    """Le pide a la IA real que ponga UNA categoría al texto. Igual que llamar a una API."""
    prompt = (f"Clasifica este gasto en UNA sola categoría de esta lista: "
              f"{', '.join(CATEGORIAS)}.\n"
              f"Responde SOLO con la categoría, sin ninguna otra palabra.\n"
              f"Gasto: {texto}")
    respuesta = cliente.messages.create(
        model=MODELO,
        max_tokens=10,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.content[0].text.strip()

# --- Equivalente con OpenAI (para referencia) ---
# from openai import OpenAI
# cliente = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# def clasificar(texto):
#     r = cliente.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}])
#     return r.choices[0].message.content.strip()


def main():
    logger.info(f"Enriqueciendo gastos con IA real · modelo: {MODELO}")
    df = pd.DataFrame(GASTOS)

    # Creamos el cliente con la llave del .env.
    cliente = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        http_client=httpx.Client(verify=False),
    )

    # ENRIQUECER: una columna nueva, generada por la IA fila por fila.
    df["categoria"] = df["descripcion"].apply(lambda t: clasificar(t, cliente))
    logger.success(f"Clasificados {len(df)} gastos con IA.")

    print("\n=== Gastos enriquecidos con una categoría (creada por la IA) ===")
    print(df[["monto", "descripcion", "categoria"]].to_string(index=False))

    print("\n=== Gasto total por categoría (insight de negocio) ===")
    resumen = df.groupby("categoria")["monto"].sum().sort_values(ascending=False)
    print(resumen.to_string())


if __name__ == "__main__":
    main()
