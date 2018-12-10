import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')


def save_plot(title):
    file = 'plots/' + title + '.png'
    plt.savefig(file)
    plt.clf()
    plt.cla()
    plt.close()
    return file


max_weeks = 6
max_assigments = 200

eduContainer = []
difContainer = []
timeContainer = []

with open('reports/seconds_spent.md', 'w') as report:
    for week in range(1, max_weeks + 1):
        report.write('### Week ' + str(week) + ' \n')
        prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
        for col in df.filter(regex=prefix + '.*', axis=1).columns[:max_assigments]:
            name = col.replace(prefix, '')
            data = df[col]
            timeContainer = data
            #med = data.median()
            #std = data.std()
            #data = data[data < med + std]
            #data.hist(bins=50)
            #plt.axvline(med, color='red', linestyle='dashed', linewidth=2)
            #filename = save_plot(name)

            
            
            data = df['DIFFICULTY_viikko0' + str(week) + '_' + name]
            data.hist(bins=5)
            #filename2 = save_plot(name + '_difficulty')
            difContainer = data

            data = df['EDUCATIONAL_VALUE_viikko0' + str(week) + '_' + name]
            data.hist(bins=5)
            #filename3 = save_plot(name + '_eduvalue')
            eduContainer = data

            plt.plot(eduContainer, timeContainer,'o')
            filename4 = save_plot(name + '_timeeduvalue')

            plt.plot(difContainer, timeContainer,'o')
            filename5 = save_plot(name + '_timedifvalue')

            # report.write('#### ' + name + ' \n')
            # report.write('times | difficulty | educational value \n')
            # report.write('--- | --- | --- \n')
            # report.write('![](../' + filename + ') | ![](../' + filename2 + ') | ![](../' + filename3 + ') \n')
