import pandas as pd

df = pd.DataFrame({
    "ciudad": ["Quito", "Guayaquil", "Cuenca", "Ambato"],
    "ventas": [1200, 850, 430, 990]
})

## mask = (df["ventas"] > 800) | (df["ciudad"] == "Cuenca")
## print(df[mask])

##mask2 = (df["ventas"] > 800) or (df["ciudad"] == "Cuenca")