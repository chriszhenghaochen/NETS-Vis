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
category = labour_file['category']
category.head()

def meanstd(names):

        result = []
        rows = []
        sum = []

        for i in range(len(names)):
            row = file_fri_1[file_fri_1.id == names[i]].values
            row = row.ravel()[1:72]
            rows.append(row)

        rows = np.array(rows)

        #1 thrill
        thrillrows1 = rows[:,:8]
        thrillrows2 = rows[:,66:67]

        thrillrows = np.concatenate((thrillrows1, thrillrows2), axis=1)

        sum.append(np.sum(thrillrows, axis= 1))

        #2 kidle
        KiddieRides = rows[:,8:19]

        sum.append(np.sum( KiddieRides, axis= 1))

        #3 RidesforEveryone
        RidesforEveryone = rows[:,19:31]

        sum.append(np.sum(RidesforEveryone, axis= 1))

        #4 ShowsEntertainment
        ShowsEntertainment1 = rows[:,31:32]
        ShowsEntertainment2 = rows[:,59:60]
        ShowsEntertainment3 = rows[:,61:63]

        ShowsEntertainment = np.concatenate((ShowsEntertainment1, ShowsEntertainment2), axis=1)
        ShowsEntertainment = np.concatenate((ShowsEntertainment, ShowsEntertainment3), axis=1)

        sum.append(np.sum(ShowsEntertainment, axis= 1))

        #5 BeerGardens
        BeerGardens = rows[:,32:34]
        sum.append(np.sum(BeerGardens, axis= 1))

        #6 food
        food1 = rows[:,34:39]
        food2 = rows[:,52:59]

        food = np.concatenate((food1, food2), axis=1)

        sum.append(np.sum(food, axis= 1))

        #7 shopping
        shopping = rows[:,39:48]

        sum.append(np.sum(shopping, axis= 1))

        #8 RestRoom
        restroom1 = rows[:,48:52]
        restroom2 = rows[:,63:66]

        restroom = np.concatenate((restroom1,restroom2),axis=1)

        sum.append(np.sum(restroom, axis=1))

        #9 Information & Assistance
        InformationAssistance = rows[:,60:61]

        sum.append(np.sum(InformationAssistance, axis=1))

        #10 Outdoor Area
        outdoorArea = rows[:,67:70]

        sum.append(np.sum(outdoorArea, axis=1))

        #11 Entry/Exit

        entryexit = rows[:,70:73]

        sum.append(np.sum(entryexit, axis=1))
        sum = np.array(sum)

        print sum

        result.append(sum.mean(axis = 1))
        result.append(sum.std(axis = 1))

        result = np.array(result)

        return result


result1 = meanstd(names1)
result2 = meanstd(names2)

print result1
print result2
##################-------plt-----------##################


N = 11
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
ax.set_xticklabels(np.unique(category))

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