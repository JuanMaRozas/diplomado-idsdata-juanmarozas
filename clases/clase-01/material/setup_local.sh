#!/usr/bin/env bash
# DPL1046 - Clase 1 - setup_local.sh
# Uso: bash clases/clase-01/material/setup_local.sh
# El .venv se crea siempre en la raíz del repo, sin importar desde dónde se corra.

set -e

# ── 0. Encontrar la raíz del repo ──────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
while [ "$REPO_ROOT" != "/" ]; do
  if [ -d "$REPO_ROOT/.git" ] || [ -d "$REPO_ROOT/clases" ]; then
    break
  fi
  REPO_ROOT="$(dirname "$REPO_ROOT")"
done
echo "==> Raíz del repo : $REPO_ROOT"

# ── 1/4. Verificar Python 3.12 ─────────────────────────────────────────────
echo "==> 1/4  Buscando Python 3.12..."

PYBIN=""

# Buscar python3.12 directo (macOS/Linux) o via py launcher (Windows)
if command -v python3.12 &>/dev/null; then
  PYBIN="python3.12"
elif command -v py &>/dev/null && py -3.12 --version &>/dev/null 2>&1; then
  PYBIN="py -3.12"
fi

# Si no encontramos 3.12 por nombre, verificar si el python por defecto ES 3.12
if [ -z "$PYBIN" ]; then
  for candidate in python3 python; do
    if command -v "$candidate" &>/dev/null; then
      VER=$("$candidate" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null)
      if [ "$VER" = "3.12" ]; then
        PYBIN="$candidate"
        break
      fi
    fi
  done
fi

# Si después de todo no hay 3.12, salir con mensaje claro
if [ -z "$PYBIN" ]; then
  echo ""
  echo "ERROR: No se encontró Python 3.12 en este sistema."
  echo ""
  echo "  Puedes tener otras versiones instaladas — no necesitas desinstalarlas."
  echo "  Solo agrega la 3.12 desde:"
  echo "  https://www.python.org/downloads/release/python-3129/"
  echo ""
  echo "  En Windows: asegúrate de marcar 'Add python.exe to PATH' al instalar."
  echo ""
  exit 1
fi

echo "==> Usando: $($PYBIN --version)"

# ── 2/4. Crear .venv en la raíz del repo ───────────────────────────────────
VENV_PATH="$REPO_ROOT/.venv"
echo "==> 2/4  Creando entorno virtual en $VENV_PATH"
$PYBIN -m venv "$VENV_PATH"

# Activar (bin/ en Mac/Linux, Scripts/ en Windows/Git Bash)
if [ -f "$VENV_PATH/bin/activate" ]; then
  source "$VENV_PATH/bin/activate"
elif [ -f "$VENV_PATH/Scripts/activate" ]; then
  source "$VENV_PATH/Scripts/activate"
else
  echo "ERROR: No se pudo activar el entorno virtual. Archivo activate no encontrado."
  exit 1
fi

# ── 3/4. Instalar dependencias ─────────────────────────────────────────────
echo "==> 3/4  Instalando dependencias"
python -m pip install --upgrade pip --quiet
pip install -r "$SCRIPT_DIR/requirements.txt"

# ── 4/4. Validar ───────────────────────────────────────────────────────────
echo "==> 4/4  Validando instalación"
python -c "import pandas, numpy; print('OK -> pandas', pandas.__version__)"

echo ""
echo "================================================"
echo " Entorno listo en: $VENV_PATH"
echo " Activa con:"
echo "   Mac/Linux -> source .venv/bin/activate"
echo "   Windows   -> source .venv/Scripts/activate"
echo "================================================"
