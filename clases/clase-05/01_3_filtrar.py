import pandas as pd

df = pd.DataFrame({
    "ciudad":    ["Quito", "Guayaquil", "Cuenca", "Ambato", "Loja", "Manta"],
    "ventas":    [1200,    850,         430,      990,      310,    760],
    "categoria": ["A",     "B",         "C",      "A",      "C",    "B"],
    "activo":    [True,    True,        False,    True,     False,  True]
})

mask = (
    ((df["ciudad"] == "Quito") | (df["ventas"] > 900)) &
    (df["categoria"].isin(["A", "B"]))                 &
    (df["activo"] == True)
)
print(df[mask])

print(df.query(
    "(ciudad == 'Quito' or ventas > 900) and categoria in ['A', 'B'] and activo == True"
))