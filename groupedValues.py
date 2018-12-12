import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sym
import numpy
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

medTimeContainer = []
medDifContainer = []
medEduContainer = []

avgTimeContainer = []
avgDifContainer = []
avgEduContainer = []


with open('reports/seconds_spent.md', 'w') as report:
    for week in range(1, max_weeks - 1):                #plussa muutettu miinukseksi yhdistelmäplottia varten
        report.write('### Week ' + str(week) + ' \n')
        prefix = 'SECONDS_SPENT_ON_viikko0' + str(week) + '_'
        for col in df.filter(regex=prefix + '.*', axis=1).columns[:max_assigments]:
            name = col.replace(prefix, '')
            data = df[col]
            timeContainer = data
            med = data.median()
            medTimeContainer.append(med)
            avg = data.mean()
            avgTimeContainer.append(avg)
            #std = data.std()
            #data = data[data < med + std]
            #data.hist(bins=50)
            #plt.axvline(med, color='red', linestyle='dashed', linewidth=2)
            #filename = save_plot(name)

            
            
            data = df['DIFFICULTY_viikko0' + str(week) + '_' + name]
            med = data.median()
            medDifContainer.append(med)
            data.hist(bins=5)
            avg = data.mean()
            avgDifContainer.append(avg)
            #filename2 = save_plot(name + '_difficulty')
            difContainer = data

            data = df['EDUCATIONAL_VALUE_viikko0' + str(week) + '_' + name]
            med = data.median()
            medEduContainer.append(med)
            data.hist(bins=5)
            avg = data.mean()
            avgEduContainer.append(avg)
            #filename3 = save_plot(name + '_eduvalue')
            eduContainer = data

##            plt.plot(eduContainer, timeContainer,'o')
##            filename4 = save_plot(name + '_timeeduvalue')
##
##            plt.plot(difContainer, timeContainer,'o')
##            filename5 = save_plot(name + '_timedifvalue')

            # report.write('#### ' + name + ' \n')
            # report.write('times | difficulty | educational value \n')
            # report.write('--- | --- | --- \n')
            # report.write('![](../' + filename + ') | ![](../' + filename2 + ') | ![](../' + filename3 + ') \n')
##print (avgTimeContainer)
##p = len(medTimeContainer)
##print (p)
###print (medDifContainer)
##
##print (medEduContainer)
##p = len(medEduContainer)
##print (p)

avgTimeContainer = np.array(avgTimeContainer, dtype=float) #transform your data in a numpy array of floats 
avgEduContainer = np.array(avgEduContainer, dtype=float) #so the curve_fit can work
avgDifContainer = np.array(avgDifContainer, dtype=float)

x = avgTimeContainer
y = avgEduContainer
z = avgDifContainer
"""
create a function to fit with your data. a, b, c and d are the coefficients
that curve_fit will calculate for you. 
In this part you need to guess and/or use mathematical knowledge to find
a function that resembles your data
"""
def func(x, a, b, c, d, e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e 
    
#def func(x, a, b, c):
    #return a * np.log(b * x) + c

"""
make the curve_fit
"""
popt, pcov = curve_fit(func, x, y)
popt2, pcov2 = curve_fit(func, x, z)

"""
Use sympy to generate the latex sintax of the function
"""
##xs = sym.Symbol('\lambda')    
##tex = sym.latex(func(xs,*popt)).replace('$', '')
##plt.title(r'$f(\lambda)= %s$' %(tex),fontsize=16)

"""
Print the coefficients and plot the funcion.
"""

#plt.plot(x, func(x, popt[0], popt[1], popt[2]), label="Fitted Curve")
#plt.plot(x, popt[0]*x**3 + popt[1]*x**2 + popt[2]*x + popt[3], label="Fitted Curve") 

#plt.legend(loc='upper left')

            
##plt.xlabel('Smarts')
##plt.ylabel('Probability')
##plt.title('Histogram of IQ')
##plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
##plt.axis([40, 160, 0, 0.03])
##plt.grid(True)
##
##plt.plot(medTimeContainer, medEduContainer, 'or')
##plt.ylim(0,5)
##plt.plot(medTimeContainer, medDifContainer, 'o')
##plt.ylim(0,5)

newTime = np.array(sorted(x))
plt.plot(avgTimeContainer, avgEduContainer, 'or', label="Educational value")
plt.ylim(0,5)
plt.plot(avgTimeContainer, avgDifContainer, 'o', label="Difficulty value")
plt.ylim(0,5)
plt.plot(newTime, func(newTime, *popt), 'g--', label="Fitted Curve", linewidth=4.0)  # same as line above \/
plt.plot(newTime, func(newTime, *popt2), 'y--', label="Fitted Curve", linewidth=4.0)  # same as line above \/
plt.legend()
##filename6 = save_plot('_medtimeeduvalue')

print("Mean squared error educational value: %.2f" % mean_squared_error(avgEduContainer, func(newTime, *popt)))
print("Mean squared error difficulty value: %.2f" % mean_squared_error(avgDifContainer, func(newTime, *popt2)))

edu5 = func(300, *popt)
print("Expected educational value at 5 min", edu5)
dif5 = func(300, *popt2)
print("Expected difficulty value at 5 min", dif5)
edu25 = func(1500, *popt)
print("Expected educational value at 25 min", edu25)
dif25 = func(1500, *popt2)
print("Expected difficulty value at 25 min", dif25)
edu60 = func(3600, *popt)
print("Expected educational value at 60 min", edu60)
dif60 = func(3600, *popt2)
print("Expected difficulty value at 60 min", dif60)

plt.plot([300, 300], [0, edu5], 'b--', linewidth=4.0)
plt.plot([0, 300], [edu5, edu5], 'b--', linewidth=4.0)
plt.plot([0, 300], [dif5, dif5], 'b--', linewidth=4.0)

plt.plot([1500, 1500], [0, edu25], 'b--', linewidth=4.0)
plt.plot([0, 1500], [edu25, edu25], 'b--', linewidth=4.0)
plt.plot([0, 1500], [dif25, dif25], 'b--', linewidth=4.0)

plt.plot([3600, 3600], [0, edu60], 'b--', linewidth=4.0)
plt.plot([0, 3600], [edu60, edu60], 'b--', linewidth=4.0)
plt.plot([0, 3600], [dif60, dif60], 'b--', linewidth=4.0)
plt.show()
