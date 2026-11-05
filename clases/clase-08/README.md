# Clase 08 — El proyecto integrador de principio a fin

**Unidad 3 · Integración de Datos y Automatización con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Proyecto de ejemplo:** [`material/proyecto-ejemplo/`](material/proyecto-ejemplo/).

> Continúa desde la Clase 7. **Última clase de contenido.** Hoy ves un proyecto integrador completo, script por script, y una presentación modelo.

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull
```

Debe aparecer la carpeta `clases/clase-08/material/proyecto-ejemplo`. En clase lo instalamos y lo corremos juntos.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: rutina, repaso e instalar el proyecto de ejemplo |
| 2 | **El proyecto**: problema de negocio y cómo está organizado |
| 3 | **Recorrido por el código**: `pipeline.py` (extraer, transformar y cargar) y sus tests |
| 4 | **Demo en vivo** y resultados |
| 5 | **La presentación modelo**: 9 slides con el template y la rúbrica |
| 6 | **Tu presentación**: checklist, preguntas que te harán y ensayo |

## El proyecto de ejemplo

Un pipeline que **pronostica la demanda semanal** con datos de Olist y el dólar de Chile (API, con respaldo si no hay internet).

| Archivo | Qué hace |
|---|---|
| `pipeline.py` | Todo el pipeline: extrae (CSV + API), transforma (ventas por semana y mes, pronóstico) y carga (SQLite y CSV) |
| `test_pipeline.py` | 10 pruebas con `pytest` |
| `requirements.txt` | Las librerías |

Para correrlo (desde la **raíz del repo**, con `(.venv)` activo):

```bash
pip install -r clases/clase-08/material/proyecto-ejemplo/requirements.txt
python clases/clase-08/material/proyecto-ejemplo/pipeline.py
pytest clases/clase-08/material/proyecto-ejemplo/ -v
```

Es de **referencia**: léelo y córrelo, pero **no lo copies**. Más detalle en su [`README.md`](material/proyecto-ejemplo/README.md).

## Proyecto integrador

La presentación modelo de hoy te muestra qué va en cada slide del template (problema, datos, arquitectura, demo, resultados, calidad, valor de negocio y aprendizajes e IA). Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Instala las librerías del proyecto de ejemplo, ejecútalo desde la raíz del repo y corre sus tests (ver arriba).
3. Revisa la checklist de entrega en `proyecto-integrador.md` y anota tus dudas.

## Qué sigue: antes de las presentaciones

El proyecto integrador es lo único que se trabaja fuera de clase:

1. **Termina tu proyecto**: que corra de punta a punta con un comando.
2. **Completa tu presentación** con el template (9 slides, 15 minutos) y ensáyala.
3. Entrega tu proyecto **como indique el docente** (Blackboard u otro).
4. **Trae tu computador cargado** y prueba tu demo antes de conectarte.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
