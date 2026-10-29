# Clase 07 — Del script al programa

**Unidad 3 · Integración de Datos y Automatización con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 6. **Hay librerías nuevas** (`pyyaml`, `loguru`, `sqlalchemy`, `pytest`): necesitas internet solo para instalarlas.

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
| 5 | **Tu proyecto**: taller con tus funciones y tus tests |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_funciones.py` | `def`, parámetros, `return`, valor por defecto | No |
| `02_errores.py` | `if/elif/else`, `for` y `try/except` | No |
| `03_logging.py` | Diario en pantalla y en `data/pipeline.log` | No |
| `utilidades.py + test_utilidades.py` | Funciones propias y 5 tests con `pytest` | No |
| `99_opcional_config.py + config.yaml` | (Opcional, para casa) Parámetros fuera del código | No |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-07/material/01_funciones.py
python clases/clase-07/material/02_errores.py
python clases/clase-07/material/03_logging.py
```

Los tests se ejecutan con:

```bash
pytest clases/clase-07/material/ -v
```


## Proyecto integrador

Lo de hoy llena la slide 7 (**Calidad y buenas prácticas**): funciones, errores, logging y tests (parte del 45% de la rúbrica). En el taller de hoy aplicas lo aprendido a tu ficha. El **proyecto de ejemplo completo** lo vemos en la Clase 8. Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase" (incluye el `pip install`).
2. Ejecuta `01` a `03` y los tests, de a uno.
3. Anota tus dudas: las revisamos al inicio de la próxima clase.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase, de forma demostrativa. La **Clase 8** muestra un proyecto integrador completo, de principio a fin, con su presentación modelo. Antes de venir, haz `git pull`.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
