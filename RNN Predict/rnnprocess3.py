import pandas as pd
import numpy as np

start = '2015-12-17 10:00:00'

########################file process######################
file = pd.read_csv('output.csv')

#file = file[file['station'] == 10]

ip = pd.read_csv("station.csv").values

ip = ip.ravel()

dict = {}
dict1 = {}

for index, item in enumerate(ip):
    dict[item] = index + 1

# print(dict)

user = file['user'].values
user3 = np.unique(user)

for index, item in enumerate(user3):
    dict1[item] = index

# print(dict1)

ipv = file['station'].values
ipv2 = []

for i in ipv:
    ipv2.append(dict[i])

# print(ipv2)

user2 = []

for i in user:
    user2.append(dict1[i])

# print(ipv2)

file['station'] = ipv2
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

times = pd.date_range(start, periods=60, freq='1min')
times = np.array(times)

datStart = times[0]
datEnd = times[len(times) - 1]

#filter
for i in range(0,len(val)):
    if (val[i][1] < datEnd and val[i][1] > datStart) or (val[i][2] < datEnd and val[i][2] > datStart):
        record.append(val[i])


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
    if r[0] in dictEnd:
        if r[3] in dictEnd[r[0]]:
            dictEnd[r[0]][r[3]].append([r[1], r[2]])
        else:
            dictEnd[r[0]][r[3]] = [[r[1], r[2]]]
    else:
        dictEnd[r[0]] = {}
        dictEnd[r[0]][r[3]] = [[r[1], r[2]]]

print("OK done!")
# print(dictEnd)
count = 0
for i in range(0, len(times)):
    for key, value in dictEnd.items():
        for key1, value1 in value.items():
            for v in value1:
                if v[0] <= times[i] and v[1] >= times[i]:
                   data[key][i] = key1
                   count+=1
                   # print(count)
                   break;



print("raw data done")

#this step is doge be careful
# for row in data:
#     if(row[len(row)-1] == 0):
#         for i in reversed(range(len(row))):
#             if row[i] != 0:
#                 row[len(row) - 1] = row[i]
#                 break;
            #this step is doge be careful
            # if i == 0:
            #     row[0] = 102

#this step is doge be careful
# data = data[np.all(data != 102, axis=1)]


output = pd.DataFrame(data)
print("data done")

print(count)
print(len(ip))



output.to_csv("rnn3.csv", index = True, header = True)
print("all done")


