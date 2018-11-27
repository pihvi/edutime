import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')

spentViikko01 = df.filter(regex='SECONDS_SPENT_ON_viikko01_*')
spentViikko01.mean()
print(spentViikko01.mean())
spentViikko01.mean().hist()
plt.show()
easyViikko01 = spentViikko01.mean().lt(500)
print(easyViikko01)
mediumViikko01 = spentViikko01.mean().between(500,1500)
print(mediumViikko01)
hardViikko01 = spentViikko01.mean().gt(1500)
print(hardViikko01)


spentViikko02 = df.filter(regex='SECONDS_SPENT_ON_viikko02_*')
spentViikko02.mean()
#print(spentViikko02.mean())

spentViikko03 = df.filter(regex='SECONDS_SPENT_ON_viikko03_*')
spentViikko03.mean()
#print(spentViikko03.mean())

spentViikko04 = df.filter(regex='SECONDS_SPENT_ON_viikko04_*')
spentViikko04.mean()
#print(spentViikko04.mean())

spentViikko05 = df.filter(regex='SECONDS_SPENT_ON_viikko05_*')
spentViikko05.mean()
#print(spentViikko05.mean())

spentViikko06 = df.filter(regex='SECONDS_SPENT_ON_viikko06_*')
spentViikko06.mean()
#print(spentViikko06.mean())