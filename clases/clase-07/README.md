# Clase 07 — Del script al programa + proyecto de ejemplo

**Unidad 3 · Integración de Datos y Automatización con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 6. **Hay librerías nuevas** (`pyyaml`, `loguru`, `sqlalchemy`): necesitas internet solo para instalarlas.

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull
pip install -r clases/clase-07/material/requirements.txt
```

Debe aparecer la carpeta `clases/clase-07`. Hay librerías nuevas: `pip install` debe terminar sin errores.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: rutina, instalar librerías y repaso |
| 2 | **Funciones**: `def`, parámetros y `return` |
| 3 | **Decisiones y errores**: `if`, `for` y `try / except` |
| 4 | **Logging** y **tests con pytest** |
| 5 | **Configuración externa**: `config.yaml` |
| 6 | **Proyecto de ejemplo** (1 hora): un proyecto integrador completo |
| 7 | **Tu proyecto**: mapa de tu proyecto |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_funciones.py` | `def`, parámetros, `return`, valor por defecto | No |
| `02_errores.py` | `if/elif/else`, `for` y `try/except` | No |
| `03_logging.py` | Diario en pantalla y en `data/pipeline.log` | No |
| `utilidades.py + test_utilidades.py` | Funciones propias y 5 tests con `pytest` | No |
| `05_config.py + config.yaml` | Parámetros fuera del código | No |
| `proyecto-ejemplo/` | Proyecto integrador de referencia (pronóstico de demanda) | Opcional (API del dólar; tiene respaldo) |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-07/material/01_funciones.py
python clases/clase-07/material/02_errores.py
python clases/clase-07/material/03_logging.py
python clases/clase-07/material/05_config.py
```

Los tests se ejecutan con:

```bash
pytest clases/clase-07/material/ -v
```


## Proyecto de ejemplo

En [`material/proyecto-ejemplo/`](material/proyecto-ejemplo/) hay un proyecto integrador completo (pronóstico de demanda con Olist y el dólar de Chile). Es **de referencia**: sirve para comparar tu proyecto contra uno que cumple la rúbrica. Léelo, córrelo, pero **no lo copies**.

## Proyecto integrador

Lo de hoy llena la slide 7 (**Calidad y buenas prácticas**): funciones, errores, logging, tests y configuración (el 45% de la rúbrica). El **proyecto de ejemplo** muestra cómo se ve uno terminado. Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase" (incluye el `pip install`).
2. Ejecuta `01` a `05` y los tests, de a uno.
3. Corre el proyecto de ejemplo: `cd clases/clase-07/material/proyecto-ejemplo` y luego `python pipeline.py` y `pytest tests -v`.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase, de forma demostrativa. La Clase 8 trabaja APIs avanzadas, IA local y un taller de proyecto.

**Recomendado antes de la Clase 8:** instala **Ollama** desde [ollama.com](https://ollama.com) y descarga el modelo: `ollama pull llama3.2` (≈2 GB: hazlo en casa, con buen internet). Si no lo logras, los scripts funcionan en modo simulado.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
