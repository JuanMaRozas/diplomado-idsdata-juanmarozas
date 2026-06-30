"""
01_api_a_pandas.py  ·  Clase 7 · Bloque 1 (Pedir)
-------------------------------------------------
Una API casi nunca te devuelve una tabla lista: te devuelve un JSON anidado.
Nuestro trabajo es convertir ese JSON real en un DataFrame de pandas (la "tabla"
con la que sabemos trabajar desde la Clase 4).
Idea clave: el dato útil estaba ESCONDIDO dentro de la clave 'serie'.
"""
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from loguru import logger
URL = "https://mindicador.cl/api/dolar"
def pedir_dolar():
    r = requests.get(URL, timeout=10, verify=False)
    r.raise_for_status()
    return r.json()
def json_a_dataframe(datos):
    """Toma el JSON real de la API y devuelve un DataFrame limpio: fecha + valor."""
    # 1) La tabla está dentro de la clave 'serie' (una lista de diccionarios)
    df = pd.DataFrame(datos["serie"])
    # 2) La fecha viene como texto largo ("2026-06-30T03:00:00.000Z").
    #    La convertimos a fecha de verdad y nos quedamos solo con el día.
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.date
    # 3) Renombramos 'valor' para que se entienda qué indicador es
    df = df.rename(columns={"valor": "dolar_clp"})
    # 4) Ordenamos de la fecha más antigua a la más nueva
    return df.sort_values("fecha").reset_index(drop=True)
def main():
    logger.info("Pidiendo serie del dólar a la API real...")
    datos = pedir_dolar()
    df = json_a_dataframe(datos)
    logger.success(f"Convertido a tabla: {df.shape[0]} filas, {df.shape[1]} columnas")
    print("\n=== El dólar como tabla de pandas (últimos 8 días) ===")
    print(df.tail(8).to_string(index=False))
    print("\nValor más caro del período:  $", df["dolar_clp"].max(), "CLP")
    print("Valor más barato del período: $", df["dolar_clp"].min(), "CLP")
    print("Promedio del período:         $", round(df["dolar_clp"].mean(), 2), "CLP")
if __name__ == "__main__":
    main()
