# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
plt.scatter(np.arange(10), np.arange(10))

# %%
a=pd.DataFrame([[1, 455.818],
[2, 952.307],
[3, 1429.19],
[4, 1893.02],
[5, 2313.17],
[6, 2718.31],
[7, 3136.49],
[8, 3527.48],
[9, 3936.22],
[10, 4285.14],
[11, 4560.75],
[12, 4904],
[13, 5110.3],
[14, 5351.94],
[15, 5453.44],
[16, 5573.69]], columns=['threads', 'hashes'])

# %%
a['per thread'] = a['hashes'] / a['threads']

# %%
plt.close()
plt.scatter(a['threads'], a['per thread'])
plt.scatter(a['threads'], a['hashes'])
plt.show()
