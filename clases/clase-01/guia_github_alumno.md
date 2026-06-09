# Guía 2 de 2 — GitHub, Git y tu entorno Python

**DPL1046 · Esta guía se hace EN CLASE durante el taller.**
Prerequisito: tener VS Code y Python instalados ([Guía 1 → VS Code](guia_vscode_alumno.md)).

Tiempo estimado: 25–35 min en clase.

---

## Paso 1 · Crea tu cuenta de GitHub

1. Entra a **https://github.com** → **Sign up**.
2. Usa un correo que revises. Elige un nombre de usuario profesional — es tu portafolio.
3. Confirma tu correo.

> GitHub es donde vive el **código** del curso. Piénsalo como el Google Drive del código, pero con historial completo de cambios.

---

## Paso 2 · Instala y configura Git

Git es la herramienta que sincroniza el código entre tu computador y GitHub.

**¿Ya lo tienes?**
```bash
git --version    # si muestra un número, ya está instalado
```

**Si no:**
- **Windows:** descarga desde **https://git-scm.com/download/win** y deja las opciones por defecto. Esto instala también *Git Bash*.
- **macOS:** escribe `git --version` en la terminal; si no está, acepta instalar las *Command Line Tools*.

**Configura tu identidad** (una sola vez, con el mismo correo de GitHub):
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"
```

---

## Paso 3 · Clona el repositorio del curso

"Clonar" = descargar una copia del repositorio a tu computador. Desde la terminal:

```bash
cd ~                          # ve a tu carpeta personal
git clone https://github.com/JuanMaRozas/diplomado-idsdata-juanmarozas.git
cd diplomado-idsdata-juanmarozas
```

Ahora tienes el código del curso en tu máquina.

---

## Paso 4 · Ábrelo en VS Code

```bash
code .    # abre la carpeta del repo en VS Code
```

Cuando VS Code pregunte si confías en la carpeta, di **Sí**. Deberías ver la estructura del proyecto en el explorador de la izquierda y el ícono de **Source Control** activado en la barra.

---

## Paso 5 · Crea el entorno virtual e instala las librerías

Desde la terminal integrada de VS Code (o la terminal externa), **dentro de la carpeta `material`**:

```bash
cd clases/clase-01/material
bash setup_local.sh
```

Este script:
1. Verifica que tienes Python 3.10 o superior.
2. Crea una carpeta `.venv` — el entorno virtual del curso.
3. Instala todas las librerías del curso (pandas, boto3, etc.).

Al terminar, activa el entorno:
```bash
source .venv/bin/activate              # Mac / Linux
source .venv/Scripts/activate          # Windows (Git Bash)
```

Verás `(.venv)` al inicio de la línea de la terminal. Eso significa que estás dentro del entorno.

> Para salir del entorno cuando termines de trabajar: `deactivate`

---

## Paso 6 · Selecciona el intérprete en VS Code

Ahora que el entorno existe, dile a VS Code que lo use:

1. `Ctrl/Cmd + Shift + P` → escribe **Python: Select Interpreter** → Enter.
2. Elige la opción que diga **`.venv`** (dentro de la carpeta del proyecto).

Verás el intérprete activo en la barra inferior de VS Code. A partir de ahí, todos tus scripts usan las librerías del curso automáticamente.

---

## Paso 7 · Descarga e instala el dataset

Descarga **`olist_raw.zip`** desde **Blackboard**, muévelo a la **raíz del repo** y descomprime:

```bash
cd ~/diplomado-idsdata-juanmarozas     # asegúrate de estar en la raíz
mv ~/Downloads/olist_raw.zip .         # mueve el zip aquí
unzip -o olist_raw.zip                 # crea data/raw/ con las 9 tablas
ls data/raw/                           # verifica que aparecen los .csv
```

> Los datos **no van a GitHub** — el `.gitignore` los bloquea. Es una buena práctica: código en el repo, datos en otro lado.

---

## Paso 8 · Corre tus primeros scripts

Con el entorno activo y el dataset en su lugar:

```bash
cd ~/diplomado-idsdata-juanmarozas
python clases/clase-01/material/01_leer_csv.py        # totales por tipo de pago
python clases/clase-01/material/02_glob_inventario.py  # inventario de las 9 tablas
```

Los scripts encuentran los datos solos, sin importar desde qué carpeta los corras.

---

## La rutina antes de cada clase

```bash
cd ~/diplomado-idsdata-juanmarozas
git pull                        # trae el material nuevo
source .venv/bin/activate       # activa el entorno
```

> **Rol de cada herramienta — para que no haya confusión:**
> - **GitHub** → solo para *bajar* material del curso (`git pull`). No necesitas subir nada.
> - **Blackboard** → donde entregas tu trabajo y descargas los datasets.
> - **Tu computador** → donde programas, pruebas y construyes el proyecto.

---

## Problemas típicos

| Problema | Solución |
|---|---|
| `git: command not found` | No instalaste Git (paso 2) |
| Error de permisos al clonar | El repo puede ser privado; avísale al profe |
| `bash setup_local.sh` → `requirements.txt not found` | Debes estar dentro de `clases/clase-01/material/` |
| `.venv` no aparece al seleccionar intérprete | El `setup_local.sh` no terminó bien; vuelve a correrlo |
| `unzip` no crea `data/raw/` | Asegúrate de ejecutar el `unzip` en la **raíz del repo** |
| `No module named pandas` | El intérprete activo no es `.venv`; revisa el paso 6 |
