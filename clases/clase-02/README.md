# Clase 02 — Entorno listo y primeros pasos en Python

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa directamente desde la Clase 1: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). Lo único nuevo es `pytest`.

**No necesitas saber Python.** Esta clase lo explica desde cero, leyendo cada línea de lo que ejecutamos. Vamos paso a paso; cada paso tiene un comando y un "Debes ver". Nadie queda atrás: todo lo de hoy está en este repo.

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

## Qué haremos hoy

| Bloque | Qué hacemos |
|---|---|
| 1 | **Entorno listo y validado** (el tiempo que haga falta) |
| 2 | Teoría: qué es cada cosa de tu *stack* y cómo mirar GitHub en la web |
| 3 | Cómo **leer un script** y cómo **ejecutarlo** en VS Code, línea por línea |
| 4 | Cierre y tarea corta |

> Las cuatro estructuras de Python (lista, tupla, set y diccionario) se ven en la [Clase 3](../clase-03/).

## Scripts de la clase

| Script | Qué hace |
|---|---|
| `00_verificar_entorno.py` | "Semáforo" del entorno: Python 3.12, `.venv`, pandas, pytest y las 9 tablas de Olist. Dice **OK** o **FALTA** y cómo arreglarlo. |
| `03a_leer_datos.py` | Tu primer script: lee dos tablas de Olist y muestra cuántas filas tiene cada una (99441 y 99224). |

## Cómo ejecutar un script en VS Code

1. Abre el archivo (Explorador → `clases` → `clase-02` → `material`).
2. Haz clic en el botón **▶** (arriba a la derecha). **Guarda** antes (Cmd+S / Ctrl+S) si cambiaste algo.
3. Si no aparece el botón, usa el comando en la terminal, con `(.venv)` activo y en la raíz del repo:

```bash
python clases/clase-02/material/03a_leer_datos.py
```

> Si ves `((.venv) )` o dos entornos (`.venv` y `.venv-1`), usa solo `.venv`: no lo actives dos veces.

## Otros scripts de esta carpeta (opcionales, para más adelante)

| Script | Para qué |
|---|---|
| `04_validar_olist.py` | Validar pagos con `if`, `try/except` y logging |
| `05_refactor_olist.py` y `test_clase2.py` | Refactorizar código con IA y probarlo con `pytest` |

No son parte de la tarea. La versión "profesional" de las 4 estructuras está en la carpeta de la Clase 3.

## Si te quedaste atrás

1. Haz los pasos de "Antes de la clase".
2. Ejecuta `03a_leer_datos.py` con el botón ▶.
3. Compara con el "Debes ver" de la presentación y anota tus dudas.

## Tarea para la próxima clase (corta)

1. Antes de la clase: entra a la carpeta del repo, activa el entorno y haz `git pull`.
2. Ejecuta de nuevo `00_verificar_entorno.py` y `03a_leer_datos.py`.
3. Cambia algo en `03a`: lee también `olist_customers_dataset.csv` y muestra cuántas filas tiene. Guarda y ejecuta.
4. Ve pensando con quién harás el **proyecto integrador**: será en **parejas**.

> **Seguridad:** nunca subas a Git tu carpeta `data/`.
