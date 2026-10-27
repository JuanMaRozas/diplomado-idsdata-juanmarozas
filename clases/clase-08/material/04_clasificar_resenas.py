"""
DPL1046 · Clase 8 · 04_clasificar_resenas.py
Enriquecer una tabla con IA: clasificar reseñas como positivas o negativas.

Si Ollama no está disponible, el script usa una regla simple (marcada como
"simulado") para que igual puedas seguir la clase.

Córrelo con el botón ▶ o con:
    python clases/clase-08/material/04_clasificar_resenas.py
"""

import requests
import pandas as pd

URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"


def clasificar(texto, puntaje):
    """Devuelve 'positiva' o 'negativa' para una reseña."""
    prompt = (
        "Clasifica esta reseña de un cliente como positiva o negativa. "
        "Responde SOLO con una palabra: positiva o negativa.\n"
        "Reseña: " + texto
    )
    try:
        respuesta = requests.post(
            URL, json={"model": MODELO, "prompt": prompt, "stream": False}, timeout=120
        )
        respuesta.raise_for_status()
        palabra = respuesta.json()["response"].strip().lower()
        return "negativa" if "neg" in palabra else "positiva"
    except requests.exceptions.RequestException:
        # Plan B: una regla simple, solo para poder seguir la clase
        return "positiva (simulado)" if puntaje >= 4 else "negativa (simulado)"


# 1) Tomar 8 reseñas que tengan comentario
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
con_texto = reviews.dropna(subset=["review_comment_message"])
muestra = con_texto[["review_score", "review_comment_message"]].head(8).copy()

# 2) Crear la columna nueva: una llamada a la IA por cada fila
muestra["sentimiento"] = muestra.apply(
    lambda fila: clasificar(fila["review_comment_message"], fila["review_score"]), axis=1
)

# 3) Mostrar el resultado
print(muestra[["review_score", "sentimiento"]])
print(muestra["sentimiento"].value_counts())
