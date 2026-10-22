# Clase 04 — Leer datos del mundo real: archivos, APIs y secretos

**Unidad 2 · Manipulación y Transformación de Datos con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 3: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). **Hay una librería nueva: `pyarrow`** (para Parquet).

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull
pip install -r clases/clase-04/material/requirements.txt
```

Debe aparecer la carpeta `clases/clase-04` y el `pip` debe terminar sin errores.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: instalar `pyarrow` y repaso de estructuras |
| 2 | **Archivos**: CSV, Excel, JSON y Parquet, un script por formato |
| 3 | **Una API pública real** (mindicador.cl): pedir datos a internet y convertirlos en tabla |
| 4 | **Secretos y datos personales**: `.env`, hashing y masking |
| 5 | **Tu proyecto**: dónde cae lo de hoy en tu presentación, y qué sigue |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_csv.py` | Leer un CSV completo y de forma "liviana" (`usecols`, `nrows`) | No |
| `02_excel.py` | Crear y leer un Excel con 2 hojas | No |
| `03_json.py` | JSON anidado: diccionarios y listas dentro de otros → tabla | No |
| `04_parquet.py` | Guardar y leer Parquet, y comparar tamaño con CSV | No |
| `05_api.py` | Pedir indicadores (dólar, UF...) a una API pública | **Sí** |
| `06_secretos_env.py` | Guardar una clave en `.env` y leerla sin escribirla en el código | Sí (opcional) |
| `07_proteger_pii.py` | Hashing de un RUT y masking de un email | No |
| `99_opcional_*.py` | Versiones completas ("profesionales") de los mismos temas | Algunos |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-04/material/01_csv.py
python clases/clase-04/material/02_excel.py
python clases/clase-04/material/03_json.py
python clases/clase-04/material/04_parquet.py
python clases/clase-04/material/05_api.py
python clases/clase-04/material/06_secretos_env.py
python clases/clase-04/material/07_proteger_pii.py
```

## Crear tu archivo `.env` (para el script 06)

```bash
# En la raíz del repo, con Git Bash (Windows) o Terminal (Mac):
echo "API_KEY=clave_de_ejemplo_1234" > .env
```

El `.env` **nunca se sube a Git** (está en `.gitignore`). Comprueba con `git status` que no aparece. Si ya tenías un `.env`, no lo borres: agrégale esa línea.

## Proyecto integrador

Lo de hoy alimenta tu presentación: los formatos y fuentes → slide 3 (**Los datos**); Parquet y la API → slide 4 (**Arquitectura**); `.env` y PII → slide 7 (**Buenas prácticas**). Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Ejecuta `01` a `07`, de a uno. Solo `05` y `06` necesitan internet.
3. Compara con el "Debes ver" de la presentación y anota tus dudas.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase. Lo único que se evalúa es el **proyecto integrador** (Clase 9). Con tu pareja, vayan afinando el tema, las tablas y las fuentes; lo trabajamos en clase.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
