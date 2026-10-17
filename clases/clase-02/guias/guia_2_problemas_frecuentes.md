# Guía 2 de 3 — Problemas frecuentes y cómo resolverlos

**DPL1046 · Consúltala cuando algo no funcione.**

Estos son los problemas **reales** que aparecieron al preparar el entorno. Busca el tuyo por el mensaje que ves.

> Usa **Terminal** (Mac) o **Git Bash** (Windows).

---

## 1. Windows: "Instalé Python, pero Git Bash no lo encuentra"

**Qué ves:** `which python python3 py` responde `no python in (...)`, o `python --version` no funciona.

**Por qué:** al instalar Python no se marcó la casilla *Add python.exe to PATH*, así que Git Bash no sabe dónde está.

**Comprueba que sí está instalado:**

```bash
ls /c/Users/$USERNAME/AppData/Local/Programs/Python/
```

Debes ver una carpeta `Python312`.

**Solución (una sola vez):** copia y pega **todo** en una línea:

```bash
echo 'export PATH="$(cygpath "$LOCALAPPDATA")/Programs/Python/Python312:$(cygpath "$LOCALAPPDATA")/Programs/Python/Python312/Scripts:$PATH"' >> ~/.bashrc && source ~/.bashrc
python --version
```

Debe decir `Python 3.12.x`. Si no, cierra y abre de nuevo la terminal (o VS Code).

---

## 2. `setup_local.sh` se detiene en "1/4 Buscando Python 3.12..." sin mensaje

**Por qué:** en Windows, `python3` puede apuntar a un acceso directo de la Microsoft Store. El script ya fue corregido: primero haz `git pull`.

**Plan B, a mano:**

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r clases/clase-01/material/requirements.txt
```

---

## 3. Mac: `zsh: command not found: python`

**Por qué:** el entorno **no está activo** (no ves `(.venv)`). Fuera del entorno, en Mac el comando se llama `python3.12`.

**Solución:** activa el entorno y vuelve a intentar:

```bash
source .venv/bin/activate
python --version
```

Alternativa sin activar: `.venv/bin/python archivo.py`.

---

## 4. Veo dos carpetas: `.venv` y `.venv-1`

**Por qué:** el entorno se creó dos veces.

**Solución:** usa **solo** `.venv`. Si quieres, borra el otro:

```bash
rm -rf .venv-1
```

No actives los dos a la vez.

---

## 5. VS Code: no aparece `Python: Select Interpreter` o el botón ▶

**Por qué:** falta la extensión **Python** (de Microsoft), o no tienes un archivo `.py` abierto.

**Solución:**

1. En VS Code, abre la pestaña de extensiones (cuadritos a la izquierda), busca **Python** (Microsoft) e instálala.
2. Abre un archivo `.py`.
3. Abajo a la derecha elige el intérprete que dice **`.venv`**. (También con `Ctrl+Shift+P` / `Cmd+Shift+P` → *Python: Select Interpreter*).

**Plan B, siempre disponible:** ejecutar desde la terminal con `python ruta/al/archivo.py`.

---

## 6. "¿Cómo llego a una carpeta que está en el Escritorio de Windows?"

En Git Bash:

```bash
cd ~/Desktop/nombre-de-la-carpeta
```

Si tu Escritorio está sincronizado con OneDrive:

```bash
cd ~/OneDrive/Desktop/nombre-de-la-carpeta
```

(a veces la carpeta se llama `Escritorio`). **Atajo:** en el Explorador de Windows, clic derecho sobre la carpeta → **Open Git Bash here**.

---

## 7. Git me pide mi nombre y correo

`git pull` normalmente **no** lo pide. Solo si Git lo exige (por ejemplo, al hacer `commit`), escribe estos **dos comandos separados**, con tus datos y entre comillas simples:

```bash
git config --global user.name 'Tu Nombre'
git config --global user.email 'tu_correo@ejemplo.com'
git config --global --list
```

> Un error típico es pegar solo la línea `user.email=...` que muestra `--list`: da `command not found`. El comando siempre **empieza con `git config`**.

---

## ¿Sigue sin funcionar?

Anota **el comando que escribiste** y **el mensaje de error completo** (copia o captura de pantalla), y compártelos en clase o por mensaje. Con eso lo resolvemos rápido.
