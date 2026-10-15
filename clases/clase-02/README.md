# Clase 02 — Estructuras de Datos, paso a paso

**Unidad 1 · Fundamentos de Programación en Python para el Trabajo con Datos**

- **Presentación:** abre [`teoria.html`](teoria.html) en el navegador (navega con ← →, tecla `F` para pantalla completa).
- **Práctica:** los scripts están en [`material/`](material/).

> Continúa directamente desde la Clase 1: mismo entorno (`.venv`), mismo dataset (Olist en `data/raw/`). Lo único nuevo es `pytest`.

**No necesitas saber Python.** Esta clase lo explica desde cero, leyendo cada línea de lo que ejecutamos. Vamos paso a paso; cada paso tiene un comando y un "Debes ver". Si tu pantalla se ve distinta, avisa. Nadie queda atrás: todo lo de hoy está en este repo.

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

El primer bloque es **exclusivo para dejar el entorno listo y validado**: preparar un entorno es lento y tiene dificultades, pero el objetivo es que todos tengamos las mismas herramientas, sin importar el computador o sistema operativo. Es una etapa clave de buenas prácticas para trabajar en equipo. Levanta la mano y pregunta: para eso estamos.

| Bloque | Qué hacemos |
|---|---|
| 1 | **Entorno listo y validado** (se extiende el tiempo que haga falta) |
| 2 | Teoría: qué es cada cosa de tu stack (Git, GitHub, Python, `.venv`, pip, VS Code) y cómo mirar el repo en la web |
| 3 | Cómo leer un script y cómo correr **solo una parte** en VS Code |
| 4 | Las 4 estructuras de Python, una por una: lista, tupla, set y diccionario |
| 5 | Comparación, cierre y tarea |

El contenido sobre **cómo encontrar datasets ricos** (que quedó pendiente de la Clase 1) está al final de la presentación, como **anexo para leer en casa**.

## El script de hoy: `03_estructuras_paso_a_paso.py`

Está dividido en **PASOS** (PASO 0 al PASO 4). Puedes correrlo de dos formas:

**A) Solo una parte, desde VS Code** (la que usamos en clase):

1. Abre `clases/clase-02/material/03_estructuras_paso_a_paso.py`.
2. Selecciona con el mouse las líneas de **un** paso.
3. Presiona **Shift + Enter**. Se abre una consola con `>>>` y aparece el resultado.

Corre siempre primero el **PASO 0**, porque carga los datos. Para salir de la consola: `exit()`.

**B) Completo, desde la terminal** (en la raíz del repo, con `(.venv)` activo):

```bash
python clases/clase-02/material/03_estructuras_paso_a_paso.py
```

| Paso | Qué es | Ejemplo con Olist |
|---|---|---|
| 0 | Preparación: `import`, variables, leer tablas | Cargar `orders` y `reviews` |
| 1 | **Lista** `[ ]`: ordenada, modificable | Los estados de una orden |
| 2 | **Tupla** `( )`: ordenada, no modificable | La "huella" (id, estado) |
| 3 | **Set** `{ }`: sin repetidos, sin orden | Estados distintos; órdenes sin reseña |
| 4 | **Diccionario** `{ clave: valor }` | Traducir estados; una orden como dict |

## Resto de los scripts

| Script | Para qué |
|---|---|
| `00_verificar_entorno.py` | Semáforo OK / FALTA: Python 3.12, entorno activo, pandas, pytest y las 9 tablas de Olist |
| `03_estructuras_olist.py` | *Opcional.* Las mismas estructuras, escritas como programa "profesional" (con funciones). Se puede correr por sección: `... 03_estructuras_olist.py listas` |
| `04_validar_olist.py` | *Se verá en la Clase 3.* Validar pagos con `if`, `try/except` y logging |
| `05_refactor_olist.py` y `test_clase2.py` | *Se verán en las próximas clases.* Refactorizar con IA y probar con `pytest` |

> Los archivos generados (`pagos_*.csv`, `*.log`) viven en `data/` y **no** se suben al repo: ya están en el `.gitignore`.

## Si te quedaste atrás

1. Haz la puesta al día (`git pull`, activar entorno, `pip install`, verificador).
2. Corre el PASO 0 y luego cada paso, de a uno, comparando con el "Debes ver" de la presentación.
3. Anota tus dudas: las revisamos al inicio de la Clase 3.

## Tarea para la próxima clase (corta)

1. Repite el **PASO 0 al PASO 4** en tu computador, de a uno, y **cambia algo** en cada paso (agrega un estado, una traducción...). Anota qué pasó.
2. Escribe con tus palabras: ¿cuándo usarías una lista, una tupla, un set y un diccionario?
3. Trae tus dudas para la Clase 3 (lectura de datos del mundo real: archivos, APIs y fuentes locales).

> **Seguridad:** nunca subas a Git tu carpeta `data/`.
