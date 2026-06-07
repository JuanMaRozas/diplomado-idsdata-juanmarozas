#!/usr/bin/env bash
# =============================================================================
# DPL1046 · Clase 1 · ESPEJO CLOUD (AWS) · aws_setup_s3.sh
# -----------------------------------------------------------------------------
# Crea el "data lake" del curso en S3 y sube las 9 CSV de Olist a la zona raw/.
# Replica en la nube exactamente lo que hicimos en local con data/raw/.
#
# Arquitectura objetivo del curso (se construye a lo largo del diplomado):
#   S3 (raw -> staging -> curated)  ->  Glue (ETL)  ->  Athena (SQL)  ->  QuickSight
#   Hoy (Clase 1): solo creamos el bucket y subimos la zona raw/.
#
# Requisitos:
#   - AWS CLI instalado y configurado:  aws configure   (Access Key, region, etc.)
#   - Haber ejecutado antes:  python download_olist.py   (deja data/raw/*.csv)
#
# Uso:
#   bash aws_setup_s3.sh
# =============================================================================
set -euo pipefail

# --- Parámetros (edítalos si quieres) ----------------------------------------
ALUMNO="${ALUMNO:-tu-nombre}"                 # ej: export ALUMNO="jrozas"
REGION="${AWS_REGION:-us-east-1}"
BUCKET="dpl1046-${ALUMNO}-datalake"           # los nombres de bucket son ÚNICOS globalmente
ORIGEN="data/raw"

echo "==> Bucket destino : s3://${BUCKET}"
echo "==> Region         : ${REGION}"

# --- 1. Crear el bucket (idempotente) ----------------------------------------
if aws s3api head-bucket --bucket "${BUCKET}" 2>/dev/null; then
  echo "==> El bucket ya existe, se reutiliza."
else
  echo "==> Creando bucket..."
  if [ "${REGION}" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "${BUCKET}" --region "${REGION}"
  else
    aws s3api create-bucket --bucket "${BUCKET}" --region "${REGION}" \
      --create-bucket-configuration LocationConstraint="${REGION}"
  fi
  # Buena práctica: bloquear acceso público
  aws s3api put-public-access-block --bucket "${BUCKET}" \
    --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
fi

# --- 2. Subir las CSV a la zona raw/ -----------------------------------------
# Cada tabla en su "carpeta" para que Glue/Athena las detecte como tablas separadas.
echo "==> Subiendo CSV a la zona raw/ ..."
for csv in "${ORIGEN}"/*.csv; do
  nombre="$(basename "${csv}" .csv)"
  aws s3 cp "${csv}" "s3://${BUCKET}/raw/${nombre}/${nombre}.csv"
  echo "    + raw/${nombre}/"
done

echo ""
echo "==> Contenido del data lake:"
aws s3 ls "s3://${BUCKET}/raw/" --recursive --human-readable --summarize | tail -n 15

echo ""
echo "================================================================"
echo " Zona raw/ lista en s3://${BUCKET}/raw/"
echo " En la Clase 3 catalogaremos estas tablas con AWS Glue Crawler"
echo " y las consultaremos con SQL desde Athena."
echo "================================================================"
