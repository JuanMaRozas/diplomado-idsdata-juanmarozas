"""
DPL1046 · Clase 8 · 03_ollama_hola.py
Hablar con una IA que corre en TU computador (Ollama), como con cualquier API.

Requisitos (una sola vez, ver README):
    1) Ollama instalado y abierto.
    2) ollama pull llama3.2

Córrelo con el botón ▶ o con:
    python clases/clase-08/material/03_ollama_hola.py
"""

import requests

URL = "http://localhost:11434/api/generate"   # Ollama escucha en tu propio computador
MODELO = "llama3.2"

pregunta = "En una sola frase, ¿qué es un DataFrame de pandas?"

try:
    respuesta = requests.post(
        URL,
        json={"model": MODELO, "prompt": pregunta, "stream": False},
        timeout=120,
    )
    respuesta.raise_for_status()
    texto = respuesta.json()["response"]
    print("Pregunta:", pregunta)
    print("Respuesta de la IA:", texto.strip())
except requests.exceptions.ConnectionError:
    print("No encontré Ollama. ¿Está abierto? Mira el README de la clase.")
except requests.exceptions.HTTPError:
    print("Ollama respondió con error. ¿Descargaste el modelo? ollama pull llama3.2")
