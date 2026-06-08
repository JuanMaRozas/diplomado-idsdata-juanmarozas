# Guía del alumno — VS Code: descarga y primeros pasos

**DPL1046 · Clase 1.** Deja VS Code listo antes de la clase. Al terminar esta guía estarás en condiciones de seguir con la **[Guía de GitHub y tu entorno](guia_github_alumno.md)**.

---

## ¿Qué es VS Code?

VS Code (Visual Studio Code) es el editor de código que usaremos todo el curso. Es gratuito, funciona en Mac, Windows y Linux, y tiene integración directa con Python, Git y la terminal — todo en una sola ventana.

---

## Paso 1 · Descarga e instala VS Code

1. Entra a **https://code.visualstudio.com**
2. Haz clic en el botón de descarga (detecta tu sistema automáticamente).
3. Instala normalmente:
   - **Windows:** ejecuta el `.exe`. En el paso *"Tareas adicionales"*, marca **"Agregar al PATH"** y **"Abrir con Code"** (facilita la vida).
   - **macOS:** arrastra el ícono a la carpeta *Aplicaciones*. Luego abre VS Code y ejecuta: `Cmd + Shift + P` → escribe `Shell Command: Install 'code' command in PATH` → Enter.

Verifica que quedó bien abriendo una terminal y escribiendo:
```bash
code --version   # debe mostrar un número de versión
```

---

## Paso 2 · Instala las extensiones esenciales

Abre VS Code → haz clic en el ícono de **Extensiones** (cuadrados en la barra izquierda, o `Ctrl/Cmd + Shift + X`) → busca e instala:

| Extensión | Para qué sirve |
|---|---|
| **Python** (Microsoft) | Soporte completo de Python: autocompletado, errores, intérprete |
| **Jupyter** (Microsoft) | Correr notebooks `.ipynb` si los necesitas |
| **GitLens** (GitKraken) | Ver el historial de Git directamente en el editor |

Con estas tres tienes todo lo que necesitas para el curso.

---

## Paso 3 · Conoce la interfaz (5 min)

```
┌─────────────────────────────────────────────┐
│  Barra de actividad (izquierda)             │
│  ├── 📁 Explorador de archivos              │
│  ├── 🔍 Búsqueda                            │
│  ├── 🔀 Control de versiones (Git)          │
│  └── 🧩 Extensiones                         │
│                                             │
│  Editor (centro) — donde escribes código    │
│                                             │
│  Terminal integrada (abajo)                 │
│  → Ctrl/Cmd + ñ   o   Ver → Terminal        │
└─────────────────────────────────────────────┘
```

Las tres cosas que más usarás:

- **Explorador** — ver y abrir archivos del proyecto.
- **Terminal integrada** — correr scripts sin salir de VS Code.
- **Paleta de comandos** (`Ctrl/Cmd + Shift + P`) — el acceso rápido a todo.

---

## Paso 4 · Abre una carpeta de proyecto

VS Code trabaja con **carpetas**, no con archivos sueltos. Siempre abre la raíz del proyecto:

```bash
# Desde la terminal, parado en la carpeta del repo:
code .
```

O usa **Archivo → Abrir carpeta** y navega hasta ella.

> Cuando VS Code te pregunte *"¿Confías en los autores de esta carpeta?"*, di que **sí**.

---

## Paso 5 · Selecciona el intérprete de Python

Después de crear el entorno virtual (lo harás en la guía de GitHub), necesitas decirle a VS Code cuál Python usar:

1. `Ctrl/Cmd + Shift + P` → escribe **Python: Select Interpreter** → Enter.
2. Elige la opción que diga **`.venv`** (la que está dentro de la carpeta del proyecto).

Verás el intérprete seleccionado en la barra inferior izquierda. A partir de ahí, al correr cualquier script usa automáticamente las librerías del curso.

---

## Paso 6 · Corre tu primer script

Con una carpeta abierta y el intérprete seleccionado:

- **Opción A** — botón ▶ en la esquina superior derecha del archivo `.py`.
- **Opción B** — terminal integrada:
  ```bash
  python clases/clase-01/material/01_leer_csv.py
  ```

La salida aparece directamente en la terminal de abajo.

---

## Atajos que usarás todo el tiempo

| Atajo | Acción |
|---|---|
| `Ctrl/Cmd + Shift + P` | Paleta de comandos (acceso a todo) |
| `Ctrl/Cmd + ñ` | Abrir/cerrar terminal integrada |
| `Ctrl/Cmd + \`` | Nueva terminal |
| `Ctrl/Cmd + S` | Guardar archivo |
| `Ctrl/Cmd + Z` | Deshacer |
| `F5` | Correr script en modo debug |
| `Ctrl/Cmd + Shift + X` | Extensiones |

---

## ¿Algo no funciona?

| Problema | Solución |
|---|---|
| `code .` no abre VS Code | Reinstala el comando de shell (paso 1, macOS) o verifica el PATH (Windows) |
| No aparece `.venv` al seleccionar intérprete | El entorno virtual aún no fue creado; ve a la guía de GitHub |
| La terminal muestra un Python distinto | Selecciona el intérprete `.venv` (paso 5) |
| Autocompletado no funciona | Verifica que la extensión **Python** de Microsoft está instalada |

---

## Siguiente paso

Con VS Code listo, continúa con la **[Guía de GitHub, Git y tu entorno](guia_github_alumno.md)** para clonar el repositorio del curso, crear el entorno virtual y dejar todo listo para la clase.
