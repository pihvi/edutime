import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

plt.interactive(False)

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
df.to_csv('./data/sigite2014-difficulty-data-csv.csv')
print('Shape:', df.shape)
print('Columns:', df.columns)
# df.boxplot()
# scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.show()
