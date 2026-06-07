"""
DPL1046 · Clase 1 · Script 2 · 02_glob_inventario.py
---------------------------------------------------------------------------
Objetivo pedagógico: automatizar la lectura de VARIOS archivos con glob.
En vez de leer una tabla a mano, recorremos las 9 CSV de Olist y armamos
un 'inventario' del dataset: filas, columnas, memoria y % de nulos.

Esta es la mentalidad del ingeniero de datos: antes de transformar nada,
hay que CONOCER lo que se tiene. Este inventario es el embrión del reporte
de calidad que automatizaremos en la Clase 4.
---------------------------------------------------------------------------
"""
from glob import glob
from pathlib import Path

import pandas as pd

DATA = Path("data/raw")


def main() -> None:
    archivos = sorted(glob(str(DATA / "*.csv")))
    if not archivos:
        raise SystemExit(
            f"No se encontraron CSV en {DATA.resolve()}. "
            "Ejecuta primero:  python download_olist.py"
        )

    print(f"==> {len(archivos)} archivos encontrados en {DATA.resolve()}\n")

    filas_inventario = []
    for ruta in archivos:
        df = pd.read_csv(ruta)
        nulos_pct = round(df.isna().mean().mean() * 100, 1)  # % nulos promedio
        filas_inventario.append(
            {
                "archivo": Path(ruta).name,
                "filas": df.shape[0],
                "columnas": df.shape[1],
                "memoria_MB": round(df.memory_usage(deep=True).sum() / 1e6, 1),
                "nulos_%": nulos_pct,
            }
        )

    inventario = (
        pd.DataFrame(filas_inventario)
        .sort_values("filas", ascending=False)
        .reset_index(drop=True)
    )

    print("INVENTARIO DEL DATASET OLIST")
    print(inventario.to_string(index=False))

    print(
        f"\n--> Total de filas en el dataset: "
        f"{inventario['filas'].sum():,}"
    )

    # Guardamos el inventario como entregable inicial del proyecto
    salida = Path("data/inventario_dataset.csv")
    inventario.to_csv(salida, index=False)
    print(f"--> Inventario guardado en: {salida.resolve()}")


if __name__ == "__main__":
    main()
