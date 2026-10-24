# Clase 05 — Pandas desde cero: leer, explorar, filtrar y limpiar

**Unidad 2 · Manipulación y Transformación de Datos con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 4: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). **No hay librerías nuevas** (necesitas `pyarrow` y `requests` de la Clase 4) y los scripts de pandas **no necesitan internet**. Hoy se suma el bloque de **secretos y datos personales**, que antes estaba en la Clase 4.

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull

```

Debe aparecer la carpeta `clases/clase-05`. Hoy no hay librerías nuevas.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: rutina y repaso |
| 2 | **La tabla de pandas**: DataFrame, columnas y tipos de dato |
| 3 | **Elegir y filtrar**: columnas, condiciones y orden |
| 4 | **Columnas nuevas y fechas** |
| 5 | **Limpiar**: vacíos y filas repetidas |
| 6 | **Juntarlo todo** para responder una pregunta |
| 7 | **Secretos y datos personales**: `.env`, hashing y masking |
| 8 | **Tu proyecto**: dónde cae lo de hoy en tu presentación |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_dataframe.py` | DataFrame, Series, `shape`, `dtypes`, `value_counts` | No |
| `02_seleccionar_filtrar.py` | Elegir columnas, filtrar filas, ordenar | No |
| `03_columnas_nuevas.py` | Columnas calculadas, fechas con `to_datetime`, `.dt` | No |
| `04_limpiar.py` | `isna`, `dropna`, `duplicated`, `drop_duplicates`, `fillna` | No |
| `05_juntar_todo.py` | Leer → limpiar → crear → responder: días de entrega | No |
| `06_secretos_env.py` | Guardar una clave en `.env` y leerla sin escribirla en el código | Sí (opcional) |
| `07_proteger_pii.py` | Hashing de un RUT y masking de un email | No |
| `99_opcional_*.py` | Versiones completas ("profesionales") de secretos y PII | Algunos |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-05/material/01_dataframe.py
python clases/clase-05/material/02_seleccionar_filtrar.py
python clases/clase-05/material/03_columnas_nuevas.py
python clases/clase-05/material/04_limpiar.py
python clases/clase-05/material/05_juntar_todo.py
python clases/clase-05/material/06_secretos_env.py
python clases/clase-05/material/07_proteger_pii.py
```

## Crear tu archivo `.env` (para el script 06)

```bash
# En la raíz del repo, con Git Bash (Windows) o Terminal (Mac):
echo "API_KEY=clave_de_ejemplo_1234" > .env
```

El `.env` **nunca se sube a Git** (está en `.gitignore`). Comprueba con `git status` que no aparece. Si ya tenías un `.env`, no lo borres: agrégale esa línea.



## Proyecto integrador

Lo de hoy alimenta tu presentación: tamaño y calidad de tus tablas → slide 3 (**Los datos**); filtros y columnas nuevas → slides 4 y 6 (**Arquitectura** y **Resultados**); limpieza → slides 3 y 7; `.env` y datos personales → slide 7 (**Buenas prácticas**). Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Ejecuta `01` a `07`, de a uno. Solo `06` usa internet (opcional).
3. Compara con el "Debes ver" de la presentación y anota tus dudas.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase, de forma demostrativa. Con la tabla limpia, la Clase 6 resume y combina (`groupby`, `merge`) y guarda en una base de datos.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
