import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# plt.interactive(False)

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
print('Shape:', df.shape)
print('Columns:', df.columns)
# df.boxplot()
# scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
spent = df.filter(regex='SECONDS_SPENT_ON_*', axis=1)
print('Shape:', spent.shape)
print('Columns:', spent.columns)

figure = plt.gcf()  # get current figure
figure.set_size_inches(100, 100)
matplotlib.rc('font', size=4)
plt.axis('off')

spent.hist()
plt.savefig('seconds_spent', dpi=600)
# plt.show()
