# Clase 02 — Estructuras de Datos y Control de Flujo con Foco Industrial

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa directamente desde la Clase 1: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). Lo único nuevo es `pytest`.

**Ritmo de la clase:** vamos paso a paso. Cada paso tiene un comando y un "Debes ver"; si tu pantalla se ve distinta, avisa. Nadie queda atrás: todo lo de hoy está en este repo.

---

## Antes de la clase (10 minutos, opcional pero recomendado)

Si tu internet es lento, adelanta esto en casa:

```bash
cd ~/diplomado-idsdata-juanmarozas      # o la ruta donde dejaste el repo
git pull
source .venv/bin/activate               # Mac
source .venv/Scripts/activate           # Windows (Git Bash)
pip install -r clases/clase-02/material/requirements.txt
python clases/clase-02/material/00_verificar_entorno.py
```

Si el último comando termina con **TODO LISTO**, estás al día. Si algo dice **FALTA**, el mismo mensaje te indica cómo arreglarlo; si no puedes, no te preocupes: lo resolvemos al inicio de la clase.

## Qué haremos hoy (3 horas)

El primer bloque es **exclusivo para dejar el entorno listo y validado**: preparar un entorno es lento y tiene dificultades, pero el objetivo es que todos tengamos las mismas herramientas, sin importar el computador o sistema operativo. Es una etapa clave de buenas prácticas para trabajar en equipo. Levanta la mano y pregunta: para eso estamos.

| Minutos | Qué hacemos |
|---|---|
| 0 – 50 | **Entorno listo y validado** (bloque exclusivo; se extiende el tiempo que haga falta) |
| 50 – 95 | Las 4 estructuras nativas (list, tuple, set, dict) y comprehensions, una por una |
| 95 – 105 | Descanso |
| 105 – 140 | Control de flujo y errores: validador de pagos con `try/except` y logging |
| 140 – 170 | Taller: refactorizar con IA y proteger con `pytest` |
| 170 – 180 | Cierre y tarea |

El contenido sobre **cómo encontrar datasets ricos** (que quedó pendiente de la Clase 1) está al final de la presentación, como **anexo para leer en casa**.

## Correr los scripts, de a uno

Desde la raíz del repositorio, con el entorno activado (debes ver `(.venv)` en la terminal):

```bash
# Verificador de entorno (semáforo OK / FALTA)
python clases/clase-02/material/00_verificar_entorno.py

# Bloque 1 — las estructuras, UNA sección a la vez
python clases/clase-02/material/03_estructuras_olist.py listas
python clases/clase-02/material/03_estructuras_olist.py tuplas
python clases/clase-02/material/03_estructuras_olist.py sets
python clases/clase-02/material/03_estructuras_olist.py diccionarios
python clases/clase-02/material/03_estructuras_olist.py comprehensions
# (sin nombre de sección corre las cinco seguidas)

# Bloque 2 — validación de pagos (genera CSV de válidos/rechazados + log)
python clases/clase-02/material/04_validar_olist.py

# Bloque 3 — taller de refactorización (espagueti vs. versión limpia)
python clases/clase-02/material/05_refactor_olist.py

# Bloque 3 — los tests (deben quedar 11 en verde)
pytest -v clases/clase-02/material/test_clase2.py
```

## Qué produce cada script

| Script | Tablas Olist que usa | Qué genera |
|---|---|---|
| `00_verificar_entorno.py` | — | Semáforo: Python 3.12, entorno activo, pandas, pytest y las 9 tablas de Olist |
| `03_estructuras_olist.py` | orders, payments, reviews | Salida por consola, una sección por estructura |
| `04_validar_olist.py` | payments | `data/pagos_validos.csv`, `data/pagos_rechazados.csv`, `data/clase2_pipeline.log` |
| `05_refactor_olist.py` | reviews | Compara el espagueti con la versión refactorizada (mismo resultado) |
| `test_clase2.py` | — | 11 tests sobre las funciones puras del Script 5 |

> Los archivos generados (`pagos_*.csv`, `*.log`) viven en `data/` y **no** se suben al repo: ya están en el `.gitignore`.

## Si te quedaste atrás

1. Haz la puesta al día (`git pull`, activar entorno, `pip install`, verificador).
2. Corre cada sección con su comando, de a una, y compara con el "Debes ver" de la presentación.
3. Anota tus dudas: las revisamos al inicio de la Clase 3.

## Tarea para la próxima clase (corta)

1. Agrega **validaciones y manejo de errores** (`try/except`, siguiendo el patrón de `validar_pago`) al script de la Clase 1 (`01_leer_csv.py`).
2. Escribe al menos **2 tests adicionales con `pytest`** para alguna función de `05_refactor_olist.py` o de tu propio script.
3. Trae tus dudas para la Clase 3 (lectura de datos del mundo real: archivos, APIs y fuentes locales).

> **Seguridad:** nunca subas a Git tu carpeta `data/`.
