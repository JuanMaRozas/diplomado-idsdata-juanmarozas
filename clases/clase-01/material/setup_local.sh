#!/usr/bin/env bash
# =============================================================================
# DPL1046 · Clase 1 · setup_local.sh
# Crea el entorno de trabajo LOCAL del curso (venv + dependencias).
# Funciona en macOS y Linux. En Windows usar Git Bash o WSL.
# Uso:   bash setup_local.sh
# =============================================================================
set -euo pipefail

echo "==> 1/4  Verificando versión de Python (se requiere 3.10+, ideal 3.12)"
PYBIN="$(command -v python3.12 || command -v python3 || command -v python)"
"$PYBIN" --version

echo "==> 2/4  Creando entorno virtual en ./.venv"
"$PYBIN" -m venv .venv

# Activación (la ruta cambia según el sistema operativo)
if [ -f ".venv/bin/activate" ]; then
  # macOS / Linux
  # shellcheck disable=SC1091
  source .venv/bin/activate
else
  # Windows (Git Bash)
  # shellcheck disable=SC1091
  source .venv/Scripts/activate
fi

echo "==> 3/4  Actualizando pip e instalando dependencias"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "==> 4/4  Validando la instalación"
python -c "import pandas, numpy, boto3, kagglehub; print('OK -> pandas', pandas.__version__)"

echo ""
echo "================================================================"
echo " Entorno listo."
echo " Para activarlo en cada sesión:"
echo "   macOS/Linux  ->  source .venv/bin/activate"
echo "   Windows      ->  .venv\\Scripts\\activate"
echo "================================================================"
