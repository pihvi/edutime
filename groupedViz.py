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


max_weeks = 6
max_assigments = 200
with open('reports/seconds_spent.md', 'w') as report:
    for week in range(1, max_weeks + 1):
        report.write('### Week ' + str(week) + ' \n')
        prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
        for col in df.filter(regex=prefix + '.*', axis=1).columns[:max_assigments]:
            name = col.replace(prefix, '')
            data = df[col]
            med = data.median()
            std = data.std()
            data = data[data < med + std]
            data.hist(bins=50)
            plt.axvline(med, color='red', linestyle='dashed', linewidth=2)
            filename = save_plot(name)

            report.write('#### ' + name + ' \n')
            report.write('![](../' + filename + ') \n')
