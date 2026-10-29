"""
99_opcional_rag_local.py  ·  Clase 8 (opcional, para curiosos)
====================================================================
OBJETIVO: tu primer RAG (Retrieval-Augmented Generation), 100% local.

La idea en una frase: en vez de que la IA "adivine" con lo que ya
sabe, primero BUSCAMOS los textos más parecidos a la pregunta dentro
de tus propios datos, y luego le pedimos a la IA que responda
USANDO esos textos como contexto. Así la respuesta está anclada a
tus datos reales, no a lo que el modelo recuerde de su entrenamiento.

Piezas, ambas corriendo en tu computador:
  1. EMBEDDINGS locales (sentence-transformers): convierten cada
     reseña en un vector de números que representa su significado.
  2. ChromaDB: una base de datos vectorial local (un archivo/carpeta
     en tu disco) que guarda esos vectores y encuentra los más
     parecidos a una pregunta nueva.
  3. Ollama: genera la respuesta final, usando las reseñas más
     parecidas como contexto.

Requisitos:
    pip install sentence-transformers chromadb
    Ollama corriendo con: ollama pull llama3.2

Cómo correrlo:
    python clases/clase-08/material/extra/99_opcional_rag_local.py
====================================================================
"""

import logging

import chromadb
import requests
from sentence_transformers import SentenceTransformer

from _datos_demo import tabla_resenas

logging.basicConfig(level=logging.INFO, format="%(message)s")

URL_OLLAMA = "http://localhost:11434/api/generate"
MODELO_CHAT = "llama3.2"
MODELO_EMBEDDINGS = "paraphrase-multilingual-MiniLM-L12-v2"  # liviano, multilingüe


def preguntar_ollama(prompt: str) -> str:
    r = requests.post(
        URL_OLLAMA,
        json={"model": MODELO_CHAT, "prompt": prompt, "stream": False},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["response"].strip()


def construir_indice(df, modelo_embeddings) -> chromadb.Collection:
    """Convierte cada reseña en un vector y lo guarda en ChromaDB local."""
    cliente = chromadb.Client()  # base vectorial en memoria, 100% local
    coleccion = cliente.get_or_create_collection("resenas_olist")

    textos = df["texto"].tolist()
    vectores = modelo_embeddings.encode(textos).tolist()

    coleccion.add(
        ids=[str(i) for i in df["id"]],
        embeddings=vectores,
        documents=textos,
        metadatas=[{"score": int(s)} for s in df["score"]],
    )
    return coleccion


def buscar_relevantes(pregunta: str, coleccion, modelo_embeddings, n: int = 3) -> list[str]:
    """Convierte la pregunta en vector, y busca las reseñas más parecidas."""
    vector_pregunta = modelo_embeddings.encode([pregunta]).tolist()
    resultado = coleccion.query(query_embeddings=vector_pregunta, n_results=n)
    return resultado["documents"][0]


def responder_con_contexto(pregunta: str, contexto: list[str]) -> str:
    """Le pide a Ollama que responda USANDO las reseñas encontradas."""
    bloque_contexto = "\n".join(f"- {c}" for c in contexto)
    prompt = (
        "Responde la siguiente pregunta usando SOLO la información de las "
        "reseñas de clientes que se muestran abajo. Sé breve y concreto.\n\n"
        f"Reseñas:\n{bloque_contexto}\n\n"
        f"Pregunta: {pregunta}"
    )
    return preguntar_ollama(prompt)


def main() -> None:
    logging.info("=== 1) Generar embeddings locales para cada reseña ===")
    modelo_embeddings = SentenceTransformer(MODELO_EMBEDDINGS)
    df = tabla_resenas()
    coleccion = construir_indice(df, modelo_embeddings)
    logging.info("Indexadas %d reseñas en ChromaDB (local, en memoria).\n", len(df))

    pregunta = "¿Qué problemas de entrega mencionan los clientes?"
    logging.info("=== 2) Buscar las reseñas más relevantes para la pregunta ===")
    logging.info("Pregunta: %s", pregunta)
    relevantes = buscar_relevantes(pregunta, coleccion, modelo_embeddings)
    for r in relevantes:
        logging.info("  · %s", r)

    logging.info("\n=== 3) Responder usando esas reseñas como contexto (RAG) ===")
    respuesta = responder_con_contexto(pregunta, relevantes)
    print(f"\nRespuesta:\n{respuesta}")

    logging.info(
        "\n✅ Nada de esto salió de tu computador: embeddings, base vectorial "
        "y modelo de lenguaje, todo local."
    )


if __name__ == "__main__":
    main()
