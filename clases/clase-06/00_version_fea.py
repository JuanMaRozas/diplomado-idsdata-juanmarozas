"""
00_version_fea.py
==================================================================
El "ANTES": un script que FUNCIONA pero está feo.
Todo amontonado, con print(), valores fijos pegados en el código
("hardcodeados"), sin funciones y sin forma de saber qué pasó si falla.

Funciona hoy. El problema es mantenerlo, reutilizarlo y confiar en él.
Lo vamos a comparar con 01_de_script_a_programa.py (el "DESPUÉS").

    python 00_version_fea.py
==================================================================
"""
import pandas as pd
from _datos_demo import generar_pedidos

# todo de corrido, sin funciones, con print y números pegados al código
df = generar_pedidos(200)
print("cargue datos")  # ¿a qué hora? ¿cuántas filas? no se sabe
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["price"])
print("limpie")
df["es_caro"] = df["price"] > 100   # 100 pegado aquí; cambiarlo obliga a tocar el código
r = df.groupby("categoria")["price"].mean().round(2)
print(r)
print("listo")
