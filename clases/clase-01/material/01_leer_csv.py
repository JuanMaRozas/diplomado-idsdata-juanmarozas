"""
DPL1046 · Clase 1 · Script 1 · 01_leer_csv.py
---------------------------------------------------------------------------
Objetivo pedagógico: el PRIMER script del curso.
Leer un CSV real, mirar su forma, y calcular totales con groupby.

Dataset: Olist (data/raw/). Usamos dos tablas simples:
  - olist_order_payments_dataset.csv  -> formas y montos de pago
  - olist_order_items_dataset.csv     -> ítems vendidos (precio + flete)

NO hacemos joins todavía: eso llega en la Clase 4 (pandas en profundidad).
Aquí solo: leer -> inspeccionar -> agrupar -> ordenar.
---------------------------------------------------------------------------
"""
from pathlib import Path

import pandas as pd


def raiz_repo() -> Path:
    """Encuentra la raíz del repo subiendo desde este archivo.
    Así el script funciona sin importar desde qué carpeta se ejecute."""
    aqui = Path(__file__).resolve()
    for carpeta in [aqui, *aqui.parents]:
        if (carpeta / ".git").exists() or (carpeta / "clases").is_dir():
            return carpeta
    return Path.cwd()  # fallback


DATA = raiz_repo() / "data" / "raw"


def inspeccionar(df: pd.DataFrame, nombre: str) -> None:
    """Imprime una ficha rápida de un DataFrame (el reflejo que hay que adquirir)."""
    print(f"\n{'='*60}\n {nombre}\n{'='*60}")
    print(f"Filas x Columnas : {df.shape[0]:,} x {df.shape[1]}")
    print(f"Columnas         : {list(df.columns)}")
    print(f"Memoria          : {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")
    print("Primeras filas:")
    print(df.head(3).to_string(index=False))


def main() -> None:
    # ---- Pagos: ¿cuánto se paga por cada forma de pago? --------------------
    pagos = pd.read_csv(DATA / "olist_order_payments_dataset.csv")
    inspeccionar(pagos, "PAGOS (olist_order_payments_dataset)")

    total_por_tipo = (
        pagos.groupby("payment_type")["payment_value"]
        .agg(["count", "sum", "mean"])
        .sort_values("sum", ascending=False)
        .round(2)
    )
    print("\n--> Total pagado por TIPO de pago:")
    print(total_por_tipo.to_string())

    # ---- Ítems: facturación total (precio + flete) -------------------------
    items = pd.read_csv(DATA / "olist_order_items_dataset.csv")
    inspeccionar(items, "ITEMS (olist_order_items_dataset)")

    items["total"] = items["price"] + items["freight_value"]
    facturacion = items["total"].sum()
    n_ordenes = items["order_id"].nunique()

    print("\n--> Indicadores rápidos del negocio:")
    print(f"    Facturación total : R$ {facturacion:,.0f}")
    print(f"    Órdenes distintas : {n_ordenes:,}")
    print(f"    Ticket promedio   : R$ {facturacion / n_ordenes:,.1f}")

    # Top 10 vendedores por facturación (primer 'ranking' del curso)
    top_sellers = (
        items.groupby("seller_id")["total"].sum()
        .sort_values(ascending=False)
        .head(10)
        .round(0)
    )
    print("\n--> Top 10 vendedores por facturación:")
    print(top_sellers.to_string())


if __name__ == "__main__":
    main()
