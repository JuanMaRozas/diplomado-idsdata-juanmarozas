"""
DPL1046 · Clase 3 · Script 5 · 05_refactor_olist.py
---------------------------------------------------------------------------
Objetivo pedagógico (TALLER): tomar un script "espagueti" que resume
reseñas de Olist, refactorizarlo con ayuda de IA, y protegerlo con tests.

Continuidad: seguimos con las tablas de Olist de la Clase 1. El espagueti
hace algo útil (resumen de reseñas por estado de orden) pero está mal
escrito. Lo dejamos en estándar de producción.

PARTE A — el espagueti (no tocar, es lo que "heredamos")
PARTE B — versión refactorizada (resultado del taller con IA)
PARTE C — funciones puras testeables (las prueba test_clase2.py)

Tablas usadas (data/raw/):
  - olist_order_reviews_dataset.csv
  - olist_orders_dataset.csv
---------------------------------------------------------------------------
"""
from pathlib import Path
import logging

import pandas as pd


def raiz_repo() -> Path:
    aqui = Path(__file__).resolve()
    for carpeta in [aqui, *aqui.parents]:
        if (carpeta / ".git").exists() or (carpeta / "clases").is_dir():
            return carpeta
    return Path.cwd()


DATA = raiz_repo() / "data" / "raw"
logging.basicConfig(level=logging.INFO, format="%(levelname)s · %(message)s")


# ═════════════════════════════════════════════════════════════════════════
# PARTE A · EL ESPAGUETI  (lo que llegó al inbox)
# ─────────────────────────────────────────────────────────────────────────
# 8 problemas a encontrar en clase antes de refactorizar:
#   1. Variables de 1 letra (r, z, x, i)
#   2. range(len(...)) + .iloc[i] en vez de iterar/vectorizar
#   3. Ifs anidados innecesarios (se combinan con &)
#   4. comparar  == True  es redundante
#   5. Número mágico (umbral) sin constante con nombre
#   6. print() en vez de logging
#   7. La función hace dos cosas (calcula E imprime)
#   8. Sin docstring ni type hints
# ═════════════════════════════════════════════════════════════════════════
def resumen(r, umbral):
    z = []
    for i in range(len(r)):
        if pd.notna(r.iloc[i]['review_score']) == True:
            if r.iloc[i]['review_score'] <= umbral:
                if pd.notna(r.iloc[i]['review_comment_message']) == True:
                    z.append(r.iloc[i]['order_id'])
    x = len(z)
    print(x)
    return x


# ═════════════════════════════════════════════════════════════════════════
# PARTE B · VERSIÓN REFACTORIZADA  (resultado del taller con IA + revisión)
# ═════════════════════════════════════════════════════════════════════════
UMBRAL_RESEÑA_BAJA = 3  # 1-3 estrellas se considera reseña negativa


def contar_resenas_negativas_con_texto(
    reviews: pd.DataFrame,
    umbral: int = UMBRAL_RESEÑA_BAJA,
) -> int:
    """
    Cuenta reseñas negativas (score <= umbral) que además traen comentario.

    Args:
        reviews: DataFrame con columnas review_score y review_comment_message.
        umbral:  Puntaje máximo para considerar una reseña como negativa.

    Returns:
        Cantidad de reseñas negativas que incluyen texto.
    """
    mask = (
        reviews["review_score"].notna()
        & (reviews["review_score"] <= umbral)
        & reviews["review_comment_message"].notna()
    )
    total = int(mask.sum())
    logging.info(f"{total:,} reseñas negativas con texto (umbral={umbral})")
    return total


# ═════════════════════════════════════════════════════════════════════════
# PARTE C · FUNCIONES PURAS TESTEABLES  (las prueba test_clase3.py)
# ─────────────────────────────────────────────────────────────────────────
# Funciones pequeñas, sin efectos secundarios, fáciles de testear.
# Son las mismas operaciones de limpieza que necesitaremos en el proyecto.
# ═════════════════════════════════════════════════════════════════════════
def clasificar_resena(score: float) -> str:
    """Clasifica una reseña por su puntaje en una categoría de negocio."""
    if pd.isna(score):
        raise ValueError("El puntaje no puede ser nulo")
    if score <= 2:
        return "negativa"
    elif score == 3:
        return "neutra"
    else:
        return "positiva"


def normalizar_estado(estado: str) -> str:
    """Normaliza el estado de una orden: minúsculas, sin espacios sobrantes."""
    if not isinstance(estado, str):
        raise TypeError(f"Esperaba str, recibí {type(estado).__name__}")
    return estado.strip().lower()


def main() -> None:
    reviews = pd.read_csv(DATA / "olist_order_reviews_dataset.csv")

    print("=" * 60)
    print(" PARTE A — espagueti (mismo resultado, código ilegible)")
    print("=" * 60)
    res_a = resumen(reviews, 3)

    print("\n" + "=" * 60)
    print(" PARTE B — refactorizado (legible, con logging y docstring)")
    print("=" * 60)
    res_b = contar_resenas_negativas_con_texto(reviews)

    # Verificación: ambas versiones deben dar el mismo número
    assert res_a == res_b, "¡Los resultados difieren! Revisar la refactorización."
    print("\n✅ El espagueti y la versión limpia dan el mismo resultado.")

    print("\n" + "=" * 60)
    print(" PARTE C — funciones puras listas para pytest")
    print("=" * 60)
    print(f"clasificar_resena(1) = {clasificar_resena(1)}")
    print(f"clasificar_resena(3) = {clasificar_resena(3)}")
    print(f"clasificar_resena(5) = {clasificar_resena(5)}")
    print(f"normalizar_estado(' Delivered ') = '{normalizar_estado(' Delivered ')}'")
    print("\nEjecuta los tests con:  pytest -v test_clase2.py")


if __name__ == "__main__":
    main()
