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
| 3 | Cómo leer un script y cómo ejecutarlo en VS Code, un archivo a la vez |
| 4 | Las 4 estructuras de Python, una por una: lista, tupla, set y diccionario |
| 5 | Comparación, cierre y tarea |

El contenido sobre **cómo encontrar datasets ricos** (que quedó pendiente de la Clase 1) está al final de la presentación, como **anexo para leer en casa**.

## Los scripts de hoy: `03a` a `03e`

Hoy hay **5 scripts cortos, uno por tema**. Cada uno se abre, se lee y se ejecuta por separado:

| Script | Tema | Ejemplo con Olist |
|---|---|---|
| `03a_leer_datos.py` | `import`, variables, leer tablas | Cargar `orders` y `reviews` |
| `03b_listas.py` | **Lista** `[ ]`: ordenada, modificable | Los estados de una orden |
| `03c_tuplas.py` | **Tupla** `( )`: ordenada, no modificable | La "huella" (id, estado) |
| `03d_sets.py` | **Set** `{ }`: sin repetidos, sin orden | Estados distintos; órdenes sin reseña |
| `03e_diccionarios.py` | **Diccionario** `{ clave: valor }` | Traducir estados; una orden como dict |

**Cómo ejecutar un script** (están en `clases/clase-02/material/`):

1. Ábrelo en VS Code (doble clic en el Explorador).
2. Haz clic en el botón **▶** de arriba a la derecha. El resultado aparece en la terminal de abajo.

Si el botón no aparece, escribe el comando en la terminal (en la raíz del repo, con `(.venv)` activo):

```bash
python clases/clase-02/material/03a_leer_datos.py
```

Para **probar cosas**: cambia algo en el script (por ejemplo, agrega un estado a la lista), **guarda** (Cmd+S en Mac, Ctrl+S en Windows) y vuelve a ejecutar.

## Resto de los scripts

| Script | Para qué |
|---|---|
| `00_verificar_entorno.py` | Semáforo OK / FALTA: Python 3.12, entorno activo, pandas, pytest y las 9 tablas de Olist |
| `07_estructuras_avanzado_opcional.py` | *Opcional.* Las mismas estructuras, escritas como programa "profesional" (con funciones). Se puede correr por sección: `python clases/clase-02/material/07_estructuras_avanzado_opcional.py listas` |
| `04_validar_olist.py` | *Se verá en la Clase 3.* Validar pagos con `if`, `try/except` y logging |
| `05_refactor_olist.py` y `test_clase2.py` | *Se verán en las próximas clases.* Refactorizar con IA y probar con `pytest` |

> Los archivos generados (`pagos_*.csv`, `*.log`) viven en `data/` y **no** se suben al repo: ya están en el `.gitignore`.

## Si te quedaste atrás

1. Haz la puesta al día (`git pull`, activar entorno, `pip install`, verificador).
2. Ejecuta `03a` y luego `03b`, `03c`, `03d` y `03e`, de a uno, comparando con el "Debes ver" de la presentación.
3. Anota tus dudas: las revisamos al inicio de la Clase 3.

## Tarea para la próxima clase (corta)

1. Ejecuta de nuevo **03a a 03e** en tu computador, de a uno, y **cambia algo** en cada script (agrega un estado, una traducción...), guarda y vuelve a ejecutar. Anota qué pasó.
2. Escribe con tus palabras: ¿cuándo usarías una lista, una tupla, un set y un diccionario?
3. Trae tus dudas para la Clase 3 (lectura de datos del mundo real: archivos, APIs y fuentes locales).

> **Seguridad:** nunca subas a Git tu carpeta `data/`.
