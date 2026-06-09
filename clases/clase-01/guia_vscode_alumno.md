# Guía 1 de 2 — VS Code: instala y conoce tu entorno de trabajo

**DPL1046 · Haz esto ANTES de la Clase 1.**
Tiempo estimado: 15–20 min.

Cuando termines esta guía tendrás VS Code listo. Luego, en clase, continuarás con la **[Guía 2 → GitHub y tu entorno](guia_github_alumno.md)** donde clonarás el repositorio, crearás el entorno Python y correrás tus primeros scripts.

---

## ¿Qué es VS Code?

VS Code (Visual Studio Code) es el editor que usaremos todo el curso. Es gratuito, funciona en Mac, Windows y Linux, y reúne en una sola ventana el editor de código, la terminal y la integración con Git y Python.

---

## Paso 1 · Instala VS Code

1. Descarga desde **https://code.visualstudio.com** (detecta tu sistema automáticamente).
2. Instala:
   - **Windows:** en el paso *"Tareas adicionales"* marca **"Agregar al PATH"** y **"Abrir con Code"**.
   - **macOS:** arrastra a *Aplicaciones*. Luego abre VS Code → `Cmd + Shift + P` → escribe `Shell Command: Install 'code' command in PATH` → Enter.

Verifica en la terminal:
```bash
code --version    # debe mostrar un número de versión
```

---

## Paso 2 · Instala Python 3.12

Descarga desde **https://www.python.org/downloads/** e instala.
- **Windows:** marca la casilla **"Add Python to PATH"** antes de continuar (importante).

Verifica:
```bash
python --version    # debe decir 3.10 o superior
```

---

## Paso 3 · Instala las extensiones esenciales

En VS Code → ícono de **Extensiones** en la barra izquierda (o `Ctrl/Cmd + Shift + X`) → instala:

| Extensión | Por qué |
|---|---|
| **Python** (Microsoft) | Autocompletado, errores y soporte de intérprete |
| **Jupyter** (Microsoft) | Soporte de notebooks si los necesitas |
| **GitLens** (GitKraken) | Ver el historial de Git directo en el editor |
| **Data Wrangler** (Microsoft) | Ver archivos CSV como tabla antes de escribir código |
| **GitHub Copilot** (GitHub) | IA para explicar, completar y mejorar código |
| **Rainbow CSV** (mechatroner) | Colorea las columnas del CSV para leerlo más fácil |

> **Data Wrangler y GitHub Copilot** son las más importantes del curso. Asegúrate de instalarlas.

### Activar GitHub Copilot
Después de instalar la extensión, inicia sesión con tu cuenta de GitHub cuando lo pida. Con la cuenta gratuita ya tienes acceso al chat y al autocompletado.

---

## Paso 4 · Conoce la interfaz

```
┌──────────────────────────────────────────────────┐
│  Barra de actividad (izquierda)                  │
│  ├── 📁 Explorador      → archivos del proyecto  │
│  ├── 🔍 Búsqueda        → buscar en el código    │
│  ├── 🔀 Source Control  → Git (commits, cambios) │
│  └── 🧩 Extensiones    → instalar plugins        │
│                                                  │
│  Editor (centro)        → donde escribes código  │
│                                                  │
│  Terminal integrada (abajo)                      │
│  → Ctrl/Cmd + J   o   Ver → Terminal             │
└──────────────────────────────────────────────────┘
```

> **Source Control** solo aparece cuando abres una carpeta que tiene un repositorio Git. Lo verás en clase cuando clones el repo.

Las tres cosas que más usarás:
- **Explorador** — navegar y abrir archivos del proyecto.
- **Terminal integrada** — correr comandos sin salir de VS Code.
- **Paleta de comandos** (`Ctrl/Cmd + Shift + P`) — acceso rápido a cualquier función.

---

## Paso 5 · Abre una carpeta (no un archivo)

VS Code trabaja con **carpetas de proyecto**, no con archivos sueltos. La forma correcta de abrir el repositorio del curso será:

```bash
cd ~/diplomado-idsdata-juanmarozas    # en clase, después de clonar
code .                                 # el punto = "abre esta carpeta"
```

Cuando VS Code pregunte *"¿Confías en los autores de esta carpeta?"*, di **Sí**.

---

## Atajos clave

| Atajo | Acción |
|---|---|
| `Ctrl/Cmd + Shift + P` | Paleta de comandos |
| `Ctrl/Cmd + J` | Abrir/cerrar terminal |
| `Ctrl/Cmd + S` | Guardar |
| `Ctrl/Cmd + Z` | Deshacer |
| `Ctrl/Cmd + Shift + X` | Extensiones |
| `Ctrl/Cmd + =` / `-` | Aumentar / reducir tamaño de fuente |

---

## Problemas típicos

| Problema | Solución |
|---|---|
| `code .` no hace nada (macOS) | Instala el comando de shell (paso 1) y reinicia la terminal |
| `code .` no funciona (Windows) | Reinstala VS Code marcando "Agregar al PATH" |
| Python no se encuentra | Reinstala marcando "Add Python to PATH" |
| Source Control no aparece | Normal — aparece al abrir una carpeta con Git (lo harás en clase) |

---

## ¿Listo?

Tienes VS Code y Python instalados. En clase harás la **[Guía 2 → GitHub y tu entorno](guia_github_alumno.md)**: crear tu cuenta de GitHub, clonar el repo, crear el entorno virtual e instalar las librerías.
