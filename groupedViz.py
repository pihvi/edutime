import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
spent = df.filter(regex='SECONDS_SPENT_ON_*', axis=1)


def save_plot(name):
    plt.savefig('plots/' + name + '.png')
    plt.clf()
    plt.cla()
    plt.close()


for week in range(1, 2):
    prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
    for col in df.filter(regex=prefix + '.*', axis=1).columns[:2]:
        name = col.replace(prefix, '')
        data = df[col]
        med = data.median()
        std = data.std()
        data = data[data < med + std]
        data.hist(bins=50)
        save_plot(name)
