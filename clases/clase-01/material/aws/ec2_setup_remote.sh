#!/usr/bin/env bash
# =============================================================================
# DPL1046 · Clase 1 · ESPEJO CLOUD (AWS) · ec2_setup_remote.sh
# -----------------------------------------------------------------------------
# Prepara una instancia EC2 (Amazon Linux 2023 / Ubuntu) como ENTORNO REMOTO
# de desarrollo. Idea: el código y los datos viven en AWS, tu notebook solo
# actúa de pantalla a través de VS Code "Remote - SSH".
#
#   Tu PC  ->  VS Code Remote SSH  ->  EC2 (Python + venv + dataset)
#
# Este script se ejecuta DENTRO de la instancia (vía SSH o como user-data).
# NO es obligatorio para la clase: el curso es local-first. Es el "espejo cloud".
#
# Uso (conectado por SSH a la EC2):
#   bash ec2_setup_remote.sh
# =============================================================================
set -euo pipefail

echo "==> Detectando gestor de paquetes..."
if command -v dnf >/dev/null 2>&1; then
  PKG="sudo dnf -y"            # Amazon Linux 2023 / Fedora
elif command -v apt-get >/dev/null 2>&1; then
  PKG="sudo apt-get -y"        # Ubuntu / Debian
  sudo apt-get update -y
else
  echo "Gestor de paquetes no soportado." ; exit 1
fi

echo "==> Instalando Python, pip, git y herramientas base..."
${PKG} install python3 python3-pip git unzip 2>/dev/null || ${PKG} install python3 python3-pip git unzip

echo "==> Instalando AWS CLI (si no está presente)..."
if ! command -v aws >/dev/null 2>&1; then
  curl -sSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
  unzip -q awscliv2.zip && sudo ./aws/install
  rm -rf awscliv2.zip aws
fi

echo "==> Clonando estructura de proyecto del curso..."
PROYECTO="${HOME}/dpl1046"
mkdir -p "${PROYECTO}" && cd "${PROYECTO}"

echo "==> Creando entorno virtual e instalando dependencias..."
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy boto3 kagglehub python-dotenv openpyxl

echo ""
echo "================================================================"
echo " EC2 lista como entorno remoto."
echo " Recomendado: usar un IAM Role en la instancia (NO claves en el código)"
echo " para que boto3 acceda a S3 con el principio de mínimo privilegio."
echo " Desde tu PC:  VS Code -> Remote-SSH -> conectar a esta instancia."
echo "================================================================"
