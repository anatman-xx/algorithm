#%%
from io import StringIO

import pandas as pd

#%%
csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'
df = pd.read_csv(StringIO(csv_data))

#%%
print(df)
print(df[1:3])
print(df['price'])
print(df[['price', 'square_feet']])
print(df[['price', 'square_feet']][1:3])
print(df[['price', 'square_feet']][1:])
