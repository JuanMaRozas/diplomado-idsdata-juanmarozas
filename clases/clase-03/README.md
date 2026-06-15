# Clase 3 — Estructuras de Datos y Control de Flujo con Foco Industrial

**DPL1046 · Diplomado en Ingeniería de Datos con Python · UDLA**
Unidad 1 · Martes 16-06-2026 · 19:15–22:30 (ZOOM) · PhD. Juan Manuel Rozas

> Antes de la clase: `git pull` para tener la última versión del material.

---

## Qué hacemos hoy

Seguimos con el **dataset Olist** de las Clases 1 y 2. Hoy bajamos un nivel desde "leer tablas con pandas" hacia **qué estructura de Python conviene para cada tarea** y **cómo validar datos** sin que el pipeline muera ante el primer error.

Tres bloques de una hora, con pausas de 10 minutos:

| Bloque | Horario | Tema | Script |
|---|---|---|---|
| 1 | 19:15–20:15 | Estructuras de datos: list, tuple, set, dict + comprehensions | `03_estructuras_olist.py` |
| — | 20:15–20:25 | Pausa | — |
| 2 | 20:25–21:25 | Control de flujo, validación, try/except, logging | `04_validar_olist.py` |
| — | 21:25–21:35 | Pausa | — |
| 3 | 21:35–22:30 | Taller: refactorizar con IA + tests con pytest | `05_refactor_olist.py` + `test_clase3.py` |

---

## Requisitos previos

El dataset Olist debe estar en `data/raw/` (igual que en las clases anteriores). Si aún no lo tienes:

```bash
# Opción rápida (en clase): descomprime el zip de Blackboard
unzip olist_raw.zip          # crea data/raw/*.csv

# Opción reproducible (con token Kaggle)
python download_olist.py
```

Necesitas `pandas` y `pytest`:

```bash
pip install pandas pytest
```

---

## Cómo ejecutar los scripts

Desde la raíz del repositorio:

```bash
# Bloque 1 — estructuras de datos sobre Olist
python clases/clase-03/03_estructuras_olist.py

# Bloque 2 — validación de pagos (genera CSV de válidos/rechazados + log)
python clases/clase-03/04_validar_olist.py

# Bloque 3 — refactorización del resumen de reseñas
python clases/clase-03/05_refactor_olist.py

# Bloque 3 — los tests (deben quedar 11 en verde)
pytest -v clases/clase-03/test_clase3.py
```

---

## Qué produce cada script

| Script | Tablas Olist que usa | Qué genera |
|---|---|---|
| `03_estructuras_olist.py` | orders, payments, reviews | Salida por consola: las 4 estructuras aplicadas al dataset |
| `04_validar_olist.py` | payments | `data/pagos_validos.csv`, `data/pagos_rechazados.csv`, `data/clase3_pipeline.log` |
| `05_refactor_olist.py` | reviews | Compara el espagueti con la versión refactorizada (mismo resultado) |
| `test_clase3.py` | — | 11 tests sobre las funciones puras del Script 5 |

> Los archivos generados (`pagos_*.csv`, `*.log`) viven en `data/` y **no** se suben al repo: ya están en el `.gitignore`.

---

## Conceptos de la clase

- **Estructuras nativas:** cuándo usar `list`, `tuple`, `set`, `dict` y por qué la elección afecta el rendimiento.
- **Comprehensions:** filtrar y transformar en una línea, de forma legible.
- **Patrón ETL:** leer → validar → separar, aislando filas malas con `continue`.
- **Manejo de errores:** `try/except/finally`, excepciones específicas, errores recuperables vs fatales.
- **Logging:** por qué reemplaza a `print()` en producción.
- **Refactorización con IA:** vibe coding supervisado — entender y verificar lo que genera la IA.
- **pytest:** tests como documentación ejecutable que protege el pipeline.

---

## Conexión con el proyecto integrador

Las funciones de validación y limpieza de hoy son las que usarás en el **entregable de la Unidad 1**: un script que lee el dataset, valida su calidad y genera un reporte. Los scripts de esta clase son la base de ese entregable.
