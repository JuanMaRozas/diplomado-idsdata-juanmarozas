# Clase 08 — El proyecto integrador de principio a fin

**Unidad 3 · Integración de Datos y Automatización con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Proyecto de ejemplo:** [`material/proyecto-ejemplo/`](material/proyecto-ejemplo/).
- **Material extra (opcional):** APIs por partes e IA local, en [`material/extra/`](material/extra/) y [`teoria_extra.html`](teoria_extra.html).

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
| 3 | **Recorrido por el código**: `pipeline.py`, `extraer.py`, `transformar.py`, `cargar.py`, `config.yaml` y tests |
| 4 | **Demo en vivo** y resultados |
| 5 | **La presentación modelo**: 9 slides con el template y la rúbrica |
| 6 | **Tu presentación**: checklist, preguntas que te harán y ensayo |

## El proyecto de ejemplo

Un pipeline que **pronostica la demanda semanal** con datos de Olist y el dólar de Chile (API, con respaldo si no hay internet).

| Archivo | Qué hace |
|---|---|
| `pipeline.py` | Corre todo, en orden |
| `src/extraer.py` | Lee los CSV de Olist y pide el dólar a la API |
| `src/transformar.py` | Limpia, combina, resume por semana y pronostica |
| `src/cargar.py` | Guarda en SQLite sin duplicar |
| `config.yaml` | Rutas y parámetros fuera del código |
| `tests/test_pipeline.py` | 4 pruebas con `pytest` |

Para correrlo (desde la carpeta del proyecto, con `(.venv)` activo):

```bash
cd clases/clase-08/material/proyecto-ejemplo
pip install -r requirements.txt
python pipeline.py
pytest tests -v
```

Es de **referencia**: léelo y córrelo, pero **no lo copies**. Más detalle en su [`README.md`](material/proyecto-ejemplo/README.md).

## Material extra (opcional)

Los scripts de APIs por partes (paginación y dos fuentes) y de IA local con Ollama **no se ven en clase**; quedan en [`material/extra/`](material/extra/) para quien quiera profundizar (necesitan `pip install -r clases/clase-08/material/extra/requirements.txt`; los de IA usan Ollama o su modo simulado). Su presentación es [`teoria_extra.html`](teoria_extra.html).

## Proyecto integrador

La presentación modelo de hoy te muestra qué va en cada slide del template (problema, datos, arquitectura, demo, resultados, calidad, valor de negocio y aprendizajes e IA). Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Entra a `proyecto-ejemplo`, instala sus librerías y ejecuta `python pipeline.py` y `pytest tests -v`.
3. Revisa la checklist de entrega en `proyecto-integrador.md` y anota tus dudas.

## Qué sigue: antes de las presentaciones

El proyecto integrador es lo único que se trabaja fuera de clase:

1. **Termina tu proyecto**: que corra de punta a punta con un comando.
2. **Completa tu presentación** con el template (9 slides, 15 minutos) y ensáyala.
3. Entrega tu proyecto **como indique el docente** (Blackboard u otro).
4. **Trae tu computador cargado** y prueba tu demo antes de conectarte.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
