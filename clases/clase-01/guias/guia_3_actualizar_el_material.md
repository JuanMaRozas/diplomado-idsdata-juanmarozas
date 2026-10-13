# Guía 3 de 3 — Actualizar el material del curso

**DPL1046 · Hazla antes de cada clase (toma 1 minuto).**

El material del curso se va completando y corrigiendo durante el diplomado. Tu copia local **no se actualiza sola**: tienes que pedirle a Git que traiga lo nuevo.

> Usa **Terminal** (Mac) o **Git Bash** (Windows). Los comandos son iguales.

---

## La rutina normal (casi siempre basta con esto)

```bash
cd ~/diplomado-idsdata-juanmarozas
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
