#!/usr/bin/env bash
# =============================================================================
# DPL1046 · Clase 1 · setup_local.sh
# Crea el entorno de trabajo LOCAL del curso (venv + dependencias).
# Funciona en macOS y Linux. En Windows usar Git Bash o WSL.
# Uso:   bash clases/clase-01/material/setup_local.sh   (desde la raíz del repo)
# =============================================================================
set -eu
# pipefail no está disponible en todos los shells de Windows (Git Bash)
# set -euo pipefail  ← solo macOS/Linux

# --- Encontrar la raíz del repo y el directorio del script ------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Subir hasta encontrar la raíz del repo (.git o carpeta clases/)
REPO_ROOT="$SCRIPT_DIR"
while [ "$REPO_ROOT" != "/" ]; do
  if [ -d "$REPO_ROOT/.git" ] || [ -d "$REPO_ROOT/clases" ]; then
    break
  fi
  REPO_ROOT="$(dirname "$REPO_ROOT")"
done

echo "==> Raíz del repo : $REPO_ROOT"
echo "==> Directorio del script : $SCRIPT_DIR"

# --- 1/4 Verificar Python ---------------------------------------------------
echo "==> 1/4  Verificando versión de Python (se requiere 3.10+, ideal 3.12)"
PYBIN="$(command -v python3.12 || command -v python3 || command -v python)"
"$PYBIN" --version

# --- 2/4 Crear .venv en la RAÍZ del repo ------------------------------------
VENV_PATH="$REPO_ROOT/.venv"
echo "==> 2/4  Creando entorno virtual en $VENV_PATH"
"$PYBIN" -m venv "$VENV_PATH"

# Activar
if [ -f "$VENV_PATH/bin/activate" ]; then
  source "$VENV_PATH/bin/activate"
else
  source "$VENV_PATH/Scripts/activate"
fi

# --- 3/4 Instalar dependencias ----------------------------------------------
echo "==> 3/4  Actualizando pip e instalando dependencias"
python -m pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.txt"

# --- 4/4 Validar ------------------------------------------------------------
echo "==> 4/4  Validando la instalación"
python -c "import pandas, numpy, boto3, kagglehub; print('OK -> pandas', pandas.__version__)"

echo ""
echo "================================================================"
echo " Entorno listo en: $VENV_PATH"
echo " Para activarlo en cada sesión:"
echo "   macOS/Linux  ->  source .venv/bin/activate"
echo "   Windows      ->  .venv\\Scripts\\activate"
echo "================================================================"
