"""
DPL1046 · Clase 2 · Script 0 · 00_verificar_entorno.py
---------------------------------------------------------------------------
Objetivo: un "semáforo" para saber, en 10 segundos, si tu entorno está listo
para trabajar. Revisa lo mismo que revisamos a mano al partir cada clase.

Cómo correrlo (desde la raíz del repo, con el entorno activo):
    python clases/clase-02/material/00_verificar_entorno.py

Cada línea muestra:  OK  = listo  ·  FALTA = hay que arreglarlo
y, si falta algo, te dice QUÉ HACER. Usa solo la biblioteca estándar de
Python, así que corre incluso si todavía no instalaste nada.
---------------------------------------------------------------------------
"""
import importlib
import sys
from pathlib import Path

TABLAS_OLIST = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]


def raiz_repo() -> Path:
    """Sube desde este archivo hasta encontrar la raíz del repo."""
    aqui = Path(__file__).resolve()
    for carpeta in [aqui, *aqui.parents]:
        if (carpeta / ".git").exists() or (carpeta / "clases").is_dir():
            return carpeta
    return Path.cwd()


def version_de(nombre: str) -> str | None:
    """Versión del paquete si se puede importar, o None si no está."""
    try:
        modulo = importlib.import_module(nombre)
    except ImportError:
        return None
    return getattr(modulo, "__version__", "instalado")


def main() -> int:
    raiz = raiz_repo()
    problemas: list[str] = []

    def linea(ok: bool, texto: str, arreglo: str = "") -> None:
        marca = "OK   " if ok else "FALTA"
        print(f"  [{marca}] {texto}")
        if not ok:
            print(f"          -> {arreglo}")
            problemas.append(texto)

    print("=" * 62)
    print(" Verificador de entorno · DPL1046")
    print("=" * 62)
    print(f"  Carpeta del curso: {raiz}\n")

    # 1. Versión de Python
    v = sys.version_info
    linea(
        (v.major, v.minor) == (3, 12),
        f"Python {v.major}.{v.minor}.{v.micro}  (se necesita 3.12.x)",
        "Activa el entorno del curso (paso 2) o revisa la instalación de "
        "Python 3.12 en el anexo de la Clase 1.",
    )

    # 2. Entorno virtual activo
    en_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    linea(
        en_venv,
        "Entorno virtual (.venv) activado",
        "Mac: source .venv/bin/activate   ·   "
        "Windows (Git Bash): source .venv/Scripts/activate",
    )

    # 3. Librerías
    for paquete, para in (("pandas", "Clase 1 en adelante"),
                          ("pytest", "tests de hoy")):
        ver = version_de(paquete)
        linea(
            ver is not None,
            f"{paquete} instalado ({ver or 'no encontrado'}) · {para}",
            "pip install -r clases/clase-02/material/requirements.txt"
            if paquete == "pytest"
            else "bash clases/clase-01/material/setup_local.sh",
        )

    # 4. Dataset
    raw = raiz / "data" / "raw"
    faltan = [t for t in TABLAS_OLIST if not (raw / t).exists()]
    linea(
        not faltan,
        f"Dataset Olist en data/raw/ ({len(TABLAS_OLIST) - len(faltan)} de "
        f"{len(TABLAS_OLIST)} tablas)",
        "Descarga olist_raw.zip desde Blackboard, ponlo en la raíz del repo "
        "y descomprímelo (guía 2 de la Clase 1, sección del dataset). "
        f"Faltan: {', '.join(faltan[:3])}{'...' if len(faltan) > 3 else ''}",
    )

    # Resultado
    print("\n" + "=" * 62)
    if problemas:
        print(f" Faltan {len(problemas)} cosa(s). Arregla de arriba hacia abajo")
        print(" y vuelve a correr este script hasta ver todo en OK.")
    else:
        print(" TODO LISTO. Puedes seguir con la clase.")
    print("=" * 62)
    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main())
