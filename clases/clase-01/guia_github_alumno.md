# Guía del alumno — GitHub, VS Code y tu entorno

**DPL1046 · Clase 1.** Sigue estos pasos para dejar tu computador listo para el curso. Hazlo de arriba hacia abajo; si te trabas en uno, avisa al profe antes de seguir.

> Tiempo estimado: 20–30 min. Lo ideal es venir con los pasos 1 a 4 ya hechos.

---

## Paso 1 · Crea tu cuenta de GitHub

1. Entra a **https://github.com** y haz clic en **Sign up**.
2. Usa un correo que revises (puede ser personal). Elige un nombre de usuario profesional —lo van a ver en tu portafolio—.
3. Confirma tu correo. ¡Listo, ya tienes cuenta!

> GitHub es donde vive el **código** del curso. Es, además, el "LinkedIn de los que programan": tu actividad ahí es portafolio.

---

## Paso 2 · Instala Git

Git es la herramienta que sincroniza el código. Revisa si ya lo tienes abriendo una terminal y escribiendo:

```bash
git --version
```

Si te muestra un número (ej. `git version 2.4x`), ya está. Si no:

- **Windows:** descarga desde **https://git-scm.com/download/win** y deja todas las opciones por defecto (esto instala también *Git Bash*, la terminal que usaremos).
- **macOS:** en la terminal escribe `git --version`; si no está, te ofrecerá instalar las *Command Line Tools*. Acepta.

---

## Paso 3 · Configura tu identidad en Git

Una sola vez, en la terminal (usa el mismo nombre y correo de GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"
```

> Esto le pone tu "firma" a cada cambio que hagas.

---

## Paso 4 · Instala VS Code y Python

1. **VS Code** (el editor): descarga desde **https://code.visualstudio.com** e instala.
2. **Python 3.12:** descarga desde **https://www.python.org/downloads/**.
   - **Windows:** en el instalador, marca la casilla **"Add Python to PATH"** (¡importante!).
3. Abre VS Code → ícono de **Extensiones** (cuadrados, barra izquierda) → instala:
   - **Python** (de Microsoft) — obligatoria.
   - **Jupyter** (de Microsoft) — recomendada.

Verifica en la terminal:
```bash
python --version   # o:  python3 --version
```

---

## Paso 5 · Clona el repositorio del curso

"Clonar" = bajar una copia del repositorio a tu computador. En la terminal, ubícate donde quieras guardarlo (ej. tu carpeta personal) y ejecuta:

```bash
git clone https://github.com/JuanMaRozas/diplomado-idsdata-juanmarozas.git
cd diplomado-idsdata-juanmarozas
```

> Si el repositorio es privado, el profe te habrá invitado o te pedirá iniciar sesión. Si da error de permisos, avísale.

---

## Paso 6 · Ábrelo en VS Code y elige el intérprete

1. En la terminal, dentro de la carpeta del repo:
   ```bash
   code .
   ```
   (el punto significa "abre esta carpeta"). También puedes usar **Archivo → Abrir carpeta**.
2. Cuando VS Code te pregunte si confías en la carpeta, di que **sí**.

---

## Paso 7 · Prepara el entorno y deja todo listo (Comienzo del Taller)

Desde la terminal **dentro del repo**:

```bash
cd ~/diplomado-idsdata-juanmarozas/clases/clase-01/material
bash setup_local.sh
```

Esto crea tu entorno virtual (`.venv`) e instala las librerías. Al terminar, actívalo:

```bash
source .venv/bin/activate          # Windows (Git Bash): source .venv/Scripts/activate
```

Verás `(.venv)` al inicio de la línea: estás dentro de tu entorno.

**En VS Code, selecciona ese entorno como intérprete:** presiona `Ctrl/Cmd + Shift + P` → escribe **"Python: Select Interpreter"** → elige el que diga **`.venv`**. Así VS Code corre tu código con las librerías del curso.

---

## Paso 8 · El dataset

Descarga **`olist_raw.zip`** desde Blackboard, muévelo a la raíz del repo y descomprímelo:

```bash
unzip -o olist_raw.zip      # crea la carpeta data/raw/ con las 9 tablas
ls data/raw/                # verifica que aparezcan los archivos .csv
```

---

## La rutina de cada clase (a partir de ahora)

Antes de cada sesión, **trae lo último** del repo:

```bash
cd diplomado-idsdata-juanmarozas
git pull
source .venv/bin/activate
```

Y listo para trabajar. 🚀

---

## Si algo falla (problemas típicos)

| Problema | Solución |
|---|---|
| `git: command not found` | No instalaste Git (paso 2). |
| `python: command not found` (Windows) | Reinstala Python marcando **"Add to PATH"**. |
| El `unzip` "no hace nada" | Asegúrate de estar en la **raíz del repo** al descomprimir. |
| VS Code no encuentra pandas | Selecciona el intérprete `.venv` (paso 7). |
| Error de permisos al clonar | El repo es privado: pídele al profe que te invite. |

> **Nunca subas a Git** tu `kaggle.json`, claves de AWS ni la carpeta `data/`. Ya está bloqueado por el `.gitignore`, pero tenlo presente.
