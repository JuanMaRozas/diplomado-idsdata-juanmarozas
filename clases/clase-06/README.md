# Clase 06 — Resumir, combinar y guardar: groupby, merge y SQLite

**Unidad 2 · Manipulación y Transformación de Datos con Python**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa desde la Clase 5: mismo entorno y dataset. **No hay librerías nuevas**: SQLite viene con Python. Los scripts **no necesitan internet**.

---

## Antes de la clase

```bash
cd ~/diplomado-idsdata-juanmarozas
source .venv/bin/activate               # Mac   (Windows: source .venv/Scripts/activate)
git pull

```

Debe aparecer la carpeta `clases/clase-06`. Hoy no hay librerías nuevas.

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Puesta al día**: rutina y repaso de la Clase 5 |
| 2 | **Resumir**: `groupby` |
| 3 | **Combinar**: `merge` |
| 4 | **Una pregunta completa**: tres tablas, un resultado |
| 5 | **Guardar**: SQLite, SQL y cargas que no duplican |
| 6 | **Tu proyecto**: mapa y avance de la Unidad 2 |

## Scripts de la clase

| Script | Qué muestra | ¿Internet? |
|---|---|---|
| `01_groupby.py` | `groupby` con `size`, `sum`, `agg` y orden | No |
| `02_merge.py` | Unir dos tablas con `merge` (`on`, `how`) | No |
| `03_pregunta_completa.py` | Ventas por estado: 3 tablas, `merge` y `groupby`; guarda un CSV | No |
| `04_pandas_a_sqlite.py` | Guardar en SQLite (`to_sql`) y consultar con SQL | No |

**Para casa (opcional):** `99_opcional_carga_repetible.py` muestra cargas que no duplican (`append` vs `replace`). No se ve en clase.

## Cómo ejecutar un script

Abre el archivo y haz clic en **▶** (guarda antes con Cmd+S / Ctrl+S), o desde la raíz del repo, con `(.venv)` activo:

```bash
python clases/clase-06/material/01_groupby.py
python clases/clase-06/material/02_merge.py
python clases/clase-06/material/03_pregunta_completa.py
python clases/clase-06/material/04_pandas_a_sqlite.py
```



## Proyecto integrador

Lo de hoy alimenta tu presentación: `groupby` → slide 6 (**Resultados**); `merge` → slides 3 y 4; SQLite → slide 4 (**Arquitectura**); carga idempotente → slide 7 (**Buenas prácticas**). Ver [`proyecto-integrador.md`](../../proyecto-integrador.md).

## Si te quedaste atrás

1. Repite el bloque "Antes de la clase".
2. Ejecuta `01` a `04`, de a uno. Ninguno necesita internet.
3. Compara con el "Debes ver" de la presentación y anota tus dudas.

## Qué sigue

No hay tareas entre clases: todo se trabaja en clase, de forma demostrativa. La Clase 7 convierte un script en un programa: funciones, errores, logging y pruebas.

> **Seguridad:** nunca subas a Git tu carpeta `data/` ni tu archivo `.env`.
