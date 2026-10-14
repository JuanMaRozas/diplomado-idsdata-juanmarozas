# Guía 3 de 3 — Actualizar el material del curso

**DPL1046 · Hazla antes de cada clase (toma 1 minuto).**

El material del curso se va completando y corrigiendo durante el diplomado. Tu copia local **no se actualiza sola**: tienes que pedirle a Git que traiga lo nuevo.

> Usa **Terminal** (Mac) o **Git Bash** (Windows). Los comandos son iguales.

---

## 0. ¿Dónde quedó mi carpeta? (y cómo moverla)

Al clonar, Git crea la carpeta `diplomado-idsdata-juanmarozas` **en la carpeta donde estaba la terminal**. Si seguiste el anexo, está en tu carpeta personal (`~`).

**Ver dónde está** (estando dentro de la carpeta del curso):

```bash
pwd
```

| | Mac | Windows (Git Bash) |
|---|---|---|
| `pwd` muestra | `/Users/tunombre/diplomado-idsdata-juanmarozas` | `/c/Users/tunombre/diplomado-idsdata-juanmarozas` |
| Equivale a | la misma ruta | `C:\Users\tunombre\diplomado-idsdata-juanmarozas` |
| Verla como carpeta | `open .` | `explorer .` |
| Abrirla en VS Code | `code .` | `code .` |

**Si no sabes dónde la dejaste**, búscala (Mac y Git Bash):

```bash
find ~ -maxdepth 4 -type d -name "diplomado-idsdata-juanmarozas" 2>/dev/null
```

Te muestra la ruta exacta. Entra con `cd` y esa ruta.

### Si quieres moverla a otra carpeta

Git no se entera de dónde vive la carpeta: **`git pull` funciona igual en cualquier lugar**. Lo que sí cambia al mover es el entorno virtual (`.venv`), que guarda rutas fijas y deja de funcionar. Sigue estos pasos:

1. Cierra VS Code y todas las terminales.
2. Mueve la carpeta (ejemplo: a una carpeta `cursos` dentro de tu carpeta personal):

```bash
mkdir -p ~/cursos
mv ~/diplomado-idsdata-juanmarozas ~/cursos/
```

3. Entra a la nueva ubicación y **vuelve a crear el entorno** (tarda unos minutos; los datos de `data/` no se pierden porque van dentro de la carpeta):

```bash
cd ~/cursos/diplomado-idsdata-juanmarozas
rm -rf .venv
bash clases/clase-01/material/setup_local.sh
```

4. Ábrela de nuevo y activa el entorno:

```bash
code .
source .venv/bin/activate              # Mac
source .venv/Scripts/activate          # Windows (Git Bash)
```

5. Desde ahora actualizas **desde la nueva ruta**:

```bash
cd ~/cursos/diplomado-idsdata-juanmarozas
git pull
```

> **Consejos:** no la muevas a una carpeta sincronizada (OneDrive, iCloud, Google Drive): sincronizan miles de archivos del `.venv` y pueden dar errores. Si en Windows `~/Documents` está dentro de OneDrive, evítala. Lo más simple es dejarla donde quedó al clonar.

---

## La rutina normal (casi siempre basta con esto)

```bash
cd ~/diplomado-idsdata-juanmarozas      # o la ruta donde la dejaste (ver sección 0)
git pull
```

Verás algo como `Updating ... Fast-forward` con la lista de archivos nuevos, o `Already up to date.` si no había nada nuevo. Luego activa tu entorno:

```bash
source .venv/bin/activate              # Mac
source .venv/Scripts/activate          # Windows (Git Bash)
```

Si el material nuevo trae librerías nuevas (el README de la clase lo avisa), instálalas con el entorno activo:

```bash
pip install -r clases/clase-0N/material/requirements.txt     # cambia N por el número de la clase
```

---

## Si `git pull` da un error

### Error: "Your local changes to the following files would be overwritten by merge"

Significa que **modificaste (o un script modificó) un archivo del curso** y el material nuevo también lo cambia. Git no quiere pisar tu cambio. Tienes dos salidas:

**A) Guardar tus cambios y actualizar** (si quieres conservar lo que hiciste):

```bash
git stash          # guarda tus cambios en un "cajón"
git pull           # actualiza
git stash pop      # los vuelve a poner (si avisa de conflicto, sigue con la opción B)
```

**B) Descartar tus cambios en los archivos del curso** (si no te importa perderlos):

```bash
git restore .      # deja los archivos del curso como estaban
git pull
```

Esto **no borra** tus archivos propios que Git no conoce (por ejemplo, lo que tengas en `mis_trabajos/` o tu carpeta `data/`).

### Error: "You have divergent branches and need to specify how to reconcile them"

```bash
git config pull.rebase false
git pull
```

### Último recurso: dejar tu copia idéntica a la del curso

Solo si lo anterior no funcionó. **Descarta todos tus cambios en los archivos del curso.**

```bash
git fetch origin
git reset --hard origin/main
```

---

## Cómo evitar conflictos

- **No edites los archivos del curso.** Si quieres modificar un script, cópialo a una carpeta `mis_trabajos/` (créala en la raíz del repo; Git la ignora) y trabaja ahí:

  ```bash
  mkdir -p mis_trabajos
  cp clases/clase-01/material/01_leer_csv.py mis_trabajos/
  ```

- **Tu proyecto integrador va en su propia carpeta**, fuera del repositorio del curso (o en `mis_trabajos/`). No se sube a este repositorio.
- Los **datos** (`data/`) y tu entorno (`.venv/`) ya están protegidos: Git no los toca.

---

## Comprobar que quedó al día

```bash
git status
```

Debe decir `Your branch is up to date with 'origin/main'`. Para ver qué cambió la última vez:

```bash
git log -3 --oneline
```

---

## Problemas típicos

| Problema | Solución |
|---|---|
| `git: command not found` | Estás en PowerShell/CMD (Windows): abre **Git Bash**. Si sigue, repite la instalación de Git (Guía 2 / anexo de instalación). |
| `fatal: not a git repository` | No estás dentro de la carpeta del curso: `cd ~/diplomado-idsdata-juanmarozas` |
| `Could not resolve host: github.com` | Sin internet. Revisa tu conexión y vuelve a intentar. |
| Falta un archivo que el profe mostró | Probablemente no hiciste `git pull`. Hazlo y revisa de nuevo. |
| `error: ... index.lock: File exists` | Quedó un `git` abierto: ciérralo. Si no hay ninguno, borra el archivo `.git/index.lock` y reintenta. |
