import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
spent = df.filter(regex='SECONDS_SPENT_ON_*', axis=1)


def save_plot(title):
    file = 'plots/' + title + '.png'
    plt.savefig(file)
    plt.clf()
    plt.cla()
    plt.close()
    return file


with open('reports/seconds_spent.md', 'w') as report:
    for week in range(1, 7):
        report.write('### Week ' + str(week) + ' \n')
        prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
        for col in df.filter(regex=prefix + '.*', axis=1).columns[:200]:
            name = col.replace(prefix, '')
            data = df[col]
            med = data.median()
            std = data.std()
            data = data[data < med + std]
            data.hist(bins=50)
            filename = save_plot(name)

            report.write('#### ' + name + ' \n')
            report.write('![](../' + filename + ') \n')
