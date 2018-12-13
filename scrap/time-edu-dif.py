import pandas as pd

df = pd.read_csv('../data/sigite2014-difficulty-data.csv', sep=';')
key = 'SECONDS_SPENT_ON'
names = list(map(lambda x: x.replace(key, ''), filter(lambda x: x.startswith(key), df.columns)))
time_edu_dif = []


def extract_time_edu_dif(row):
    for name in names:
        time = row['SECONDS_SPENT_ON' + name]
        education = row['EDUCATIONAL_VALUE' + name]
        difficulty = row['DIFFICULTY' + name]
        time_edu_dif.append([time, education, difficulty])


df.apply(extract_time_edu_dif, axis=1)
df2 = pd.DataFrame(time_edu_dif, columns=['time', 'education', 'difficulty'])
df2.to_csv('../data/time_edu_dif.csv')
