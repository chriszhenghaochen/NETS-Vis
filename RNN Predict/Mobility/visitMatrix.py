## for plot visit among time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

start = '2015-12-17 10:00:00'
duration = 360
frequency = '1min'

# stat = [10264, 10159, 10065]
# stat = [100, 10001, 10006, 10010, 10014, 10022, 10023, 10027,  1003, 10038, 10041]
stat = [10022]
#stat = pd.read_csv("station.csv").values.ravel()
print(stat)
plotdict = {}

for s in stat:
    plotdict[s] = []

########################file process######################
file = pd.read_csv('output.csv')

#file = file[file['station'] == 10]

ip = pd.read_csv("station.csv").values

ip = ip.ravel()

dict = {}
dict1 = {}

for index, item in enumerate(ip):
    dict[item] = index

# print(dict)

user = file['user'].values
user3 = np.unique(user)

for index, item in enumerate(user3):
    dict1[item] = index

# # print(dict1)
#
# ipv = file['station'].values
# ipv2 = []
#
# for i in ipv:
#     ipv2.append(dict[i])

# print(ipv2)

user2 = []

for i in user:
    user2.append(dict1[i])

# print(ipv2)

# file['station'] = ipv2
file['user'] = user2

file = file[['user', 'start', 'end', 'station']]

file['end'] = pd.to_datetime(file['end'])
file['start'] = pd.to_datetime(file['start'])


file = file.sort(['user','end'])



#####################time processing###############

val = file.values
record = []
target = []
# dictStart = dict()
dictEnd = {}
# dictIP = dict()

times = pd.date_range(start, periods=duration, freq=frequency)
times = np.array(times)

datStart = times[0]
datEnd = times[len(times) - 1]

#filter
for i in range(0,len(val)):
    if (val[i][3] in stat) and ((val[i][1] < datEnd and val[i][1] > datStart) or (val[i][2] < datEnd and val[i][2] > datStart)):
        record.append(val[i])

    #record.append(val[i])

user = np.asarray(user)
user = np.unique(user)
record = np.asarray(record)



newFile = pd.DataFrame(record)

#nomilization of user
dict3 = {}
user3 = newFile[0].values
user2 = np.unique(user3)
user = []
for index, item in enumerate(user2):
    dict3[item] = index

for i in user3:
    user.append(dict3[i])

newFile[0] = user
# newFile.sort([0])
record = newFile.values

# print(record)

data = np.zeros(shape=(len(user2),len(times)))


for r in record:
    if r[3] in dictEnd:
        if r[0] in dictEnd[r[3]]:
            dictEnd[r[3]][r[0]].append([r[1], r[2]])
        else:
            dictEnd[r[3]][r[0]] = [[r[1], r[2]]]
    else:
        dictEnd[r[3]] = {}
        dictEnd[r[3]][r[0]] = [[r[1], r[2]]]

print("OK done!")
# print(dictEnd)

for i in range(0, len(times)):
    for key, value in dictEnd.items():
        count = 0
        for key1, value1 in value.items():
            for v in value1:
                if v[0] <= times[i] and v[1] >= times[i]:
                  count += 1
                  break;

        plotdict[key].append(count)



print("raw data done")


#plot
label = []
T = np.asarray(range(len(times)))
xnew = np.linspace(T.min(), T.max(), 1200)

for key, value in plotdict.items():
    power_smooth = spline(T, value, xnew)
    plt.plot(xnew, power_smooth)
    # plt.plot(times, value)
    label.append(key)

# for key, value in plotdict.items():
#     plt.plot(times, value)


tick_locs = [xnew[0], xnew[int(len(xnew)/3)], xnew[int(len(xnew)/3*2)], xnew[int(len(xnew) - 1)]]
tick_lbls = ([times[0], times[int(len(times)/3)], times[int(len(times)/3*2)], times[int(len(times) - 1)]])
plt.xticks(tick_locs, tick_lbls)

plt.legend(label, loc='upper left')
plt.show()