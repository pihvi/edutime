import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# plt.interactive(False)

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
