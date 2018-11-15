import pandas as pd

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
print('Shape:', df.shape)
print('Columns:', df.columns)
