import pandas as pd

df = pd.DataFrame({
    "ciudad": ["Quito", "Guayaquil", "Cuenca", "Ambato", "Loja"],
    "ventas": [1200, 850, 430, 990, 310],
    "categoria": ["A", "B", "C", "A", "C"]
})

mask = (df["ventas"] > 800) & (df["categoria"] == "A")
print(df[mask])

print(df.query("ventas > 800 and categoria == 'A'"))

print(df.query("ventas > 400 and categoria != 'C' and ciudad != 'Ambato'"))

limite = 800
print(df.query("ventas > @limite"))

print(df.query("ventas > 800 or ciudad == 'Cuenca'"))