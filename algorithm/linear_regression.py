#%%
from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

#%%
csv_data = 'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n'
df = pd.read_csv(StringIO(csv_data))

#%%
regr = linear_model.LinearRegression()
regr.fit(df['square_feet'].values.reshape(-1, 1), df['price'])

#%%
a, b = regr.coef_, regr.intercept_

#%%
plt.scatter(df['square_feet'], df['price'])
plt.plot(df['square_feet'], regr.predict(df['square_feet'].values.reshape(-1, 1)))
plt.show()
