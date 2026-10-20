# Clase 03 — Las 4 estructuras de Python y tu proyecto integrador

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 2: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). **No hay que instalar nada nuevo.**

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull
```

Debe aparecer la carpeta `clases/clase-03`. Si el botón ▶ de VS Code no funciona, usa el comando en la terminal.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: repaso de `03a_leer_datos.py` |
| 2 | **Las 4 estructuras**, una por una, con su código línea por línea: lista, tupla, set y diccionario |
| 3 | **Tu proyecto integrador**: rúbrica, formato de la presentación, template y tu primera ficha (en parejas) |
| 4 | Cierre y qué sigue |

## Scripts de la clase

| Script | Estructura | Qué muestra |
|---|---|---|
| `01_listas.py` | Lista `[ ]` | Los estados de una orden, en orden; posiciones; `append`; `for` |
| `02_tuplas.py` | Tupla `( )` | La "huella" de una orden (id, estado), que no se puede modificar |
| `03_sets.py` | Set `{ }` | Estados distintos y órdenes sin reseña (768) |
| `04_diccionarios.py` | Diccionario `{ : }` | Traducir estados y describir una orden |
| `05_ficha_proyecto.py` | Las 4 juntas | La ficha de tu proyecto: tema, integrantes, tablas y entregas |
| `99_opcional_estructuras_avanzado.py` | — | Versión "profesional" de las 4 estructuras (opcional) |

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-03/material/01_listas.py
python clases/clase-03/material/02_tuplas.py
python clases/clase-03/material/03_sets.py
python clases/clase-03/material/04_diccionarios.py
python clases/clase-03/material/05_ficha_proyecto.py
```

## Proyecto integrador

- Reglas, 10 temas, rúbrica y entregas: [`proyecto-integrador.md`](../../proyecto-integrador.md).
- **Template de la presentación** (editable): [`material/template_presentacion_proyecto.pptx`](material/template_presentacion_proyecto.pptx). Es solo de formato: cada slide indica qué debe ir y cuánto tiempo (15 min en total).
- Se trabaja **en parejas**.

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Ejecuta `01` a `04`, de a uno, y compara con el "Debes ver" de la presentación.
3. Anota tus dudas: las revisamos al inicio de la Clase 4.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase. Lo único que se evalúa es el **proyecto integrador** (Clase 9). Con tu pareja, ve pensando el tema; lo afinamos en clase.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
