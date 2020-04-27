import pandas as pd

df1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
}).set_index(['key'])
df1
df2 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'B': ['B0', 'B1', 'B2']
}).set_index(['key'])
df2
df_out = df1.join(df2)
print(df_out)
