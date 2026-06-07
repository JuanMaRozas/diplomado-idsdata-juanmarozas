# Clase 01 — Python en la Industria Real: por qué domina el dato

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

- **Teoría:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

---

## Qué harás hoy

1. Dejar tu **entorno local** listo (VS Code + Python 3.12 + entorno virtual).
2. Tener el **dataset del curso** (Olist) en `data/raw/`.
3. Correr tus **dos primeros scripts**.
4. (Espejo cloud) Subir el dataset crudo a **AWS S3**.

## Paso a paso

> **Importante:** trabaja siempre dentro del repositorio que clonaste. El dataset va en `data/raw/` **en la raíz del repo**. Los scripts encuentran esa carpeta solos, sin importar desde dónde los ejecutes.

```bash
# Entorno (desde la raíz del repo)
cd ~/diplomado-idsdata-juanmarozas
bash clases/clase-01/material/setup_local.sh
source .venv/bin/activate          # Windows: .venv\Scripts\activate
```

### Conseguir el dataset Olist — elige UNA vía

**Vía A — rápida (recomendada en clase).** Descarga `olist_raw.zip` desde **Blackboard**, muévelo a la raíz del repo y descomprímelo ahí:
```bash
cd ~/diplomado-idsdata-juanmarozas      # raíz del repo
mv ~/Downloads/olist_raw.zip .          # traer el zip desde Descargas
unzip -o olist_raw.zip                  # crea data/raw/ con las 9 CSV
ls data/raw/                            # verifica: deben aparecer las 9 tablas
```

**Vía B — reproducible (tarea).** Con tu token de Kaggle configurado (ver instrucciones dentro de `download_olist.py`):
```bash
python clases/clase-01/material/download_olist.py   # descarga las 9 tablas a data/raw/
```

### Correr tus primeros scripts

```bash
python clases/clase-01/material/01_leer_csv.py        # totales por tipo de pago y top vendedores
python clases/clase-01/material/02_glob_inventario.py # inventario de las 9 tablas del dataset
```

### Espejo cloud (opcional)

```bash
aws configure
export ALUMNO="tu-nombre"
bash clases/clase-01/material/aws/aws_setup_s3.sh     # crea tu bucket y sube data/raw/ a la zona raw/
```

## Tarea para la próxima clase

Elige **tu propio dataset** (distinto a Olist) que cumpla los criterios de "dataset rico" vistos en clase y tenga **al menos 2 fuentes/tablas**. Justifícalo en el README de tu propio repositorio. Será el dataset de tu **proyecto integrador**.

> **Seguridad:** nunca subas a Git tu `kaggle.json`, credenciales de AWS ni la carpeta `data/`.
