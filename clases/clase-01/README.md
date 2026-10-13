# Clase 01 — Python en la Industria Real: por qué domina el dato

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

> Este curso es **100% local**: todo lo que hacemos corre y persiste en tu propio computador. No se usa ninguna cuenta ni servicio cloud (AWS, Azure, GCP) en ningún momento del diplomado.

## Orden de trabajo (sigue este orden)

| # | Qué | Dónde | Cuándo |
|---|---|---|---|
| 1 | **Presentación de la clase** (navega con ← →, tecla `F` para pantalla completa) | [`teoria.html`](teoria.html) | En clase |
| 2 | **Taller de instalación, paso a paso (Mac y Windows)** | [`teoria_anexo_instalacion.html`](teoria_anexo_instalacion.html) | En clase, todos juntos. Puedes repetirlo en casa. |
| 3 | **Tus dos primeros scripts** | [`material/`](material/) | En clase, al terminar la instalación |
| 4 | Guía escrita 1: VS Code y Python (versión texto del taller) | [`guias/guia_1_vscode_y_python.md`](guias/guia_1_vscode_y_python.md) | Apoyo, si te quedaste atrás |
| 5 | Guía escrita 2: GitHub y tu entorno (versión texto del taller) | [`guias/guia_2_github_y_entorno.md`](guias/guia_2_github_y_entorno.md) | Apoyo, si te quedaste atrás |
| 6 | Guía escrita 3: **actualizar el material** (`git pull` y qué hacer si da error) | [`guias/guia_3_actualizar_el_material.md`](guias/guia_3_actualizar_el_material.md) | Antes de cada clase |
| 7 | Referencia rápida de Python (consulta) | [`guias/referencia_python_clase1.html`](guias/referencia_python_clase1.html) | Cuando la necesites |

## Qué harás hoy

1. Dejar tu **entorno local** listo (Git + Python 3.12 + VS Code + entorno virtual).
2. Tener el **dataset del curso** (Olist) en `data/raw/`.
3. Correr tus **dos primeros scripts**.

## Resumen de comandos del taller

> **Importante:** trabaja siempre dentro del repositorio que clonaste. El dataset va en `data/raw/` **en la raíz del repo**. Los scripts encuentran esa carpeta solos, sin importar desde dónde los ejecutes. En Windows usa **Git Bash**.

```bash
# Entorno (desde la raíz del repo)
cd ~/diplomado-idsdata-juanmarozas
bash clases/clase-01/material/setup_local.sh
source .venv/bin/activate          # Windows (Git Bash): source .venv/Scripts/activate
```

### Conseguir el dataset Olist — elige UNA vía

**Vía A — rápida (recomendada en clase).** Descarga `olist_raw.zip` desde **Blackboard**, muévelo a la raíz del repo y descomprímelo ahí:
```bash
cd ~/diplomado-idsdata-juanmarozas      # raíz del repo
mv ~/Downloads/olist_raw.zip .          # traer el zip desde Descargas
unzip -o olist_raw.zip                  # Mac: crea data/raw/ con las 9 CSV
# Windows (Git Bash, sin unzip):  python -m zipfile -e olist_raw.zip .
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

## Tarea para la próxima clase

1. **Conforma tu equipo (el tamaño se define en clase).**
2. **Elige uno de los 10 temas** del proyecto integrador (ver [`proyecto-integrador.md`](../../proyecto-integrador.md)). Todos se desarrollan sobre el dataset del curso (Olist).
3. Deja tu **entorno y el dataset listos** (lo de hoy) para arrancar la próxima clase sin demoras.
4. Antes de la próxima clase, **actualiza el material** con `git pull` (Guía 3).

> **Opcional (suma valor):** complementar el proyecto con un dataset propio o una API externa.

> **Seguridad:** nunca subas a Git tu `kaggle.json` ni la carpeta `data/`.
