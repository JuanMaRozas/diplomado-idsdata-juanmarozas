"""
03_combinar_fuentes.py  ·  Clase 7 · Bloque 2 (Combinar y guardar)
------------------------------------------------------------------
El valor real aparece cuando JUNTAMOS varias fuentes. Aquí pedimos DOS
indicadores reales (dólar y UF) y los combinamos en una sola tabla, emparejados
por fecha (un 'merge', como en la Clase 4).

⭐ BUENA PRÁCTICA: este script NO vuelve a escribir cómo pedir a la API.
   Importa las funciones desde el módulo 'indicadores.py'. Reutilizamos código
   en vez de copiarlo. Esto es posible gracias al `if __name__ == "__main__"`
   que protege la demo de ese módulo (ver 06_reutilizar.py).
"""

import pandas as pd
from loguru import logger
from indicadores import pedir_indicador, a_tabla    # <- REUTILIZAMOS el módulo


def main():
    logger.info("Pidiendo indicador 1: dólar...")
    dolar = a_tabla(pedir_indicador("dolar"), "dolar_clp")

    logger.info("Pidiendo indicador 2: UF...")
    uf = a_tabla(pedir_indicador("uf"), "uf_clp")

    # MERGE: emparejamos por la columna 'fecha' (solo fechas que estén en ambas)
    logger.info("Combinando ambas fuentes por fecha (merge)...")
    combinado = pd.merge(dolar, uf, on="fecha", how="inner").sort_values("fecha")

    # Una columna nueva que SOLO existe gracias a tener las dos fuentes juntas:
    combinado["uf_en_dolares"] = (combinado["uf_clp"] / combinado["dolar_clp"]).round(2)

    logger.success(f"Tabla combinada: {combinado.shape[0]} filas, {combinado.shape[1]} columnas")
    print("\n=== Dólar + UF combinados por fecha (últimos 8 días) ===")
    print(combinado.tail(8).to_string(index=False))


if __name__ == "__main__":
    main()
