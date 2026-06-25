import pandas as pd
mod = __import__('03_validacion')
# tabla con un precio negativo a propósito
df = pd.DataFrame({'order_id':['o1','o2'],
                   'price':[100.0, -5.0],
                   'rating':[3, 4]})
mod.validar(df)