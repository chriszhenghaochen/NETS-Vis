import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

names = []
line = sys.stdin.readline()

lines = line.split('p')

names1 = lines[0].split(' ')
names1.remove('')
names1 = map(int, names1)

names2 = lines[1].split(' ')
names2.remove('')
names2 = map(int, names2)


file_fri_1 = pd.read_csv('C:/Users/zchen4/Desktop/data/attraction frequency/freqs_Fri.csv')
labour_file = pd.read_csv('C:/Users/zchen4/PycharmProjects/python-visualising-jeremy/datain/key points.csv')

def meanstd(names):

        result = []
        rows = []

        for i in range(len(names)):
            row = file_fri_1[file_fri_1.id == names[i]].values
            row = row.ravel()[1:72]
            rows.append(row)

        rows = np.array(rows)

        result.append(rows.mean(axis=0))
        result.append(rows.std(axis = 0))

        result = np.array(result)

        return result


result1 = meanstd(names1)
result2 = meanstd(names2)


print result1
print result2

##################-------plt-----------##################

N = 70
menMeans = result1[0]
menStd = result1[1]

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

womenMeans = result2[0]
womenStd = result2[1]
rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('Freqence')
ax.set_title('Frequence of Friday')
# ax.set_xticks(ind + width)
ax.set_xticklabels(labour_file['name'].values)

groupname1 = ''
groupname2 = ''

for i in range(len(names1)):
    groupname1 += str(names1[i])
    groupname1 += ' '

for i in range(len(names2)):
    groupname2 += str(names2[i])
    groupname2 += ' '



ax.legend((rects1[0], rects2[0]), ( groupname1, groupname2))


plt.show()