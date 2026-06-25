from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_excel(BASE_DIR / "ejemplo-walmart.xlsx", header=None)

limpio = (
    df.iloc[:, 0]
    .str.strip()
    .str.lstrip("/")
    .str.rstrip("/")
    .str.split("/", expand=True)
)

df["empresa"]   = limpio[0].str.strip()
df["formato"]   = limpio[1].str.strip()
df["direccion"] = limpio[2].str.strip()

print(df[[0, "empresa", "formato", "direccion"]].head(10))

df.to_excel(BASE_DIR / "ejemplo-walmart-limpio.xlsx", index=False)