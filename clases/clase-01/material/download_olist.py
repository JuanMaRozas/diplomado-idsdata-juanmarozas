"""
DPL1046 · Clase 1 · download_olist.py
---------------------------------------------------------------------------
Descarga el dataset del curso (Olist Brazilian E-Commerce) desde Kaggle de
forma reproducible y lo deja copiado en ./data/raw/ para trabajar localmente.

Requisitos previos (una sola vez):
  1) Tener cuenta en kaggle.com
  2) Crear un API token:  Kaggle -> Settings -> "Create New Token"
     Eso descarga kaggle.json. Colocarlo en:
        macOS/Linux ->  ~/.kaggle/kaggle.json     (chmod 600)
        Windows     ->  C:\\Users\\<usuario>\\.kaggle\\kaggle.json

Uso:
  python download_olist.py
---------------------------------------------------------------------------
"""
import shutil
from pathlib import Path

import kagglehub

DATASET = "olistbr/brazilian-ecommerce"
DESTINO = Path("data/raw")


def main() -> None:
    print(f"==> Descargando '{DATASET}' desde Kaggle...")
    origen = Path(kagglehub.dataset_download(DATASET))
    print(f"    Descargado en cache: {origen}")

    DESTINO.mkdir(parents=True, exist_ok=True)
    copiados = 0
    for csv in sorted(origen.glob("*.csv")):
        destino_csv = DESTINO / csv.name
        shutil.copy2(csv, destino_csv)
        copiados += 1
        print(f"    + {csv.name}")

    print(f"\n==> Listo: {copiados} archivos CSV en {DESTINO.resolve()}")
    print("    Las 9 tablas de Olist están listas para la práctica.")


if __name__ == "__main__":
    main()
