# Clase 08 — APIs avanzadas, IA local y taller de proyecto

**Unidad 3 · Integración de Datos y Automatización con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 7. **Última clase de contenido.** Para los scripts de IA necesitas **Ollama** instalado (ver abajo); sin Ollama, funcionan en **modo simulado**.

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull

```

Debe aparecer la carpeta `clases/clase-08`. Ollama es opcional pero recomendado.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: rutina, repaso y comprobar Ollama |
| 2 | **APIs avanzadas**: paginación y dos fuentes en una tabla |
| 3 | **IA local**: hablar con un modelo, clasificar y resumir |
| 4 | **Taller de proyecto**: checklist, ensayo y dudas |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_paginacion.py` | Paginación con `while` (PokeAPI) | **Sí** |
| `02_dos_fuentes.py` | Ventas de Olist + dólar de Chile (API) en una tabla | **Sí** |
| `03_ollama_hola.py` | Hablar con una IA local con `requests.post` | Solo local |
| `04_clasificar_resenas.py` | Clasificar reseñas con IA (modo simulado si no hay Ollama) | Solo local |
| `05_resumen_ejecutivo.py` | Pandas calcula, la IA redacta (modo simulado si no hay Ollama) | Solo local |
| `99_opcional_rag_local.py` | RAG básico (requiere librerías pesadas) | Opcional |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-08/material/01_paginacion.py
python clases/clase-08/material/02_dos_fuentes.py
python clases/clase-08/material/03_ollama_hola.py
python clases/clase-08/material/04_clasificar_resenas.py
python clases/clase-08/material/05_resumen_ejecutivo.py
```



## Instalar Ollama (una sola vez, con buen internet)

1. Descarga e instala desde [ollama.com](https://ollama.com).
2. Abre una terminal y descarga el modelo (≈2 GB):

```bash
ollama pull llama3.2
ollama list      # debe aparecer llama3.2
```

3. Deja la aplicación de Ollama **abierta** mientras trabajas.

Si no puedes instalarlo, no te detengas: `04` y `05` funcionan en modo simulado y lo avisan.

## Proyecto integrador

Lo de hoy alimenta tu presentación: dos fuentes → slides 3 y 4; IA → slides 8 y 9 (**Valor de negocio** y **Aprendizajes e IA**). El **taller** final prepara tu entrega y tu ensayo. Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Ejecuta `01` a `05`, de a uno (`01` y `02` necesitan internet).
3. Sin Ollama, `04` y `05` marcan "(simulado)". Revisa la checklist de entrega en `proyecto-integrador.md`.

## Qué sigue: antes de las presentaciones

El proyecto integrador es lo único que se trabaja fuera de clase:

1. **Termina tu proyecto**: que corra de punta a punta con un comando.
2. **Completa tu presentación** con el template (9 slides, 15 minutos) y ensáyala.
3. Entrega tu proyecto **como indique el docente** (Blackboard u otro).
4. **Trae tu computador cargado** y prueba tu demo antes de conectarte.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
