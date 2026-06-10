#!/usr/bin/env bash
# DPL1046 - Clase 1 - setup_local.sh
# Uso: bash clases/clase-01/material/setup_local.sh (desde la raiz del repo)

# Encontrar la raiz del repo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
while [ "$REPO_ROOT" != "/" ]; do
  if [ -d "$REPO_ROOT/.git" ] || [ -d "$REPO_ROOT/clases" ]; then
    break
  fi
  REPO_ROOT="$(dirname "$REPO_ROOT")"
done

echo "==> Raiz del repo : $REPO_ROOT"

# 1/4 Verificar Python
echo "==> 1/4  Verificando Python (se requiere 3.10+)"
PYBIN="$(command -v python3.12 || command -v python3 || command -v python)"
"$PYBIN" --version

# 2/4 Crear .venv en la raiz del repo
VENV_PATH="$REPO_ROOT/.venv"
echo "==> 2/4  Creando entorno virtual en $VENV_PATH"
"$PYBIN" -m venv "$VENV_PATH"

if [ -f "$VENV_PATH/bin/activate" ]; then
  source "$VENV_PATH/bin/activate"
else
  source "$VENV_PATH/Scripts/activate"
fi

# 3/4 Instalar dependencias
echo "==> 3/4  Instalando dependencias"
python -m pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.txt"

# 4/4 Validar
echo "==> 4/4  Validando"
python -c "import pandas, numpy; print('OK -> pandas', pandas.__version__)"

echo ""
echo "================================================"
echo " Entorno listo en: $VENV_PATH"
echo " Activa con:"
echo "   Mac/Linux -> source .venv/bin/activate"
echo "   Windows   -> source .venv/Scripts/activate"
echo "================================================"
