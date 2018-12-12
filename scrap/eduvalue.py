import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('./data/sigite2014-difficulty-data.csv', sep=';')
spent = df.filter(regex='SECONDS_SPENT_ON_*', axis=1)
studentSpentW1 = []
studentEduW1 = []
studentSpentW2 = []
studentEduW2 = []
studentSpentW3 = []
studentEduW3 = []
studentSpentW4 = []
studentEduW4 = []
studentSpentW5 = []
studentEduW5 = []
studentSpentW6 = []
studentEduW6 = []
for week in range(1, 7):
    prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
    prefix2 = 'EDUCATIONAL_VALUE_viikko0' + str(week) + '_'
    for col in df.filter(regex=prefix + '.*', axis=1).columns:
        name = col.replace(prefix, '')
        if week == 1:
                studentSpentW1 = df[col]
        if week == 2:
                studentSpentW2 = df[col]
        if week == 3:
                studentSpentW3 = df[col]
        if week == 4:
                studentSpentW4 = df[col]
        if week == 5:
                studentSpentW5 = df[col]
        if week == 6:
                studentSpentW6 = df[col]
        #print(df[col])
    for col in df.filter(regex=prefix2 + '.*', axis=1).columns:
        name = col.replace(prefix2, '')
        if week == 1:
                studentEduW1 = df[col]
        if week == 2:
                studentEduW2 = df[col]
        if week == 3:
                studentEduW3 = df[col]
        if week == 4:
                studentEduW4 = df[col]
        if week == 5:
                studentEduW5 = df[col]
        if week == 6:
                studentEduW6 = df[col]
        
students = []
for i in range(len(studentEduW1)):
        if(studentEduW1[i] > 2):
                students.append(i)

timeUsed =[]
for i in range(len(students)):
        timeUsed.append(studentSpentW1[students[i]])

#print(timeUsed)
#plt.plot(timeUsed)
plt.plot(studentSpentW1, studentEduW1, 'o')
plt.show()