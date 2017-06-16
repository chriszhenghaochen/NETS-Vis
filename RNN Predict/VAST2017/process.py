import pandas as pd
import numpy as np

dataO = np.zeros(shape=(1,240))

########################file process######################
file = pd.read_csv('out.csv')
dates = pd.read_csv('dates.csv').values
dates = dates.ravel()

#file = file[file['station'] == 10]

ip = pd.read_csv('key points.csv')['name'].values

ip = ip.ravel()

dict = {}
dict1 = {}

for index, item in enumerate(ip):
    dict[item] = index + 1

# print(dict)

user = file['id'].values
user3 = np.unique(user)

for index, item in enumerate(user3):
    dict1[item] = index

# print(dict1)

ipv = file['gate'].values
ipv2 = []

for i in ipv:
    ipv2.append(dict[i])

# print(ipv2)

user2 = []

for i in user:
    user2.append(dict1[i])

# print(ipv2)

file['gate'] = ipv2
file['id'] = user2

file = file[['id', 'time', 'gate']]

file['time'] = pd.to_datetime(file['time'])



file = file.sort(['id','time'])
val = file.values

starttime = ' 00:00:00'

for date in dates:

    start = date + starttime

    print(start)
    #####################time processing###############


    record = []
    target = []
    # dictStart = dict()
    dictEnd = {}
    # dictIP = dict()

    times = pd.date_range(start, periods=240, freq='5min')
    times = np.array(times)

    datStart = times[0]
    datEnd = times[len(times) - 1]

    #filter
    for i in range(0,len(val)):
        if (val[i][1] < datEnd and val[i][1] > datStart):
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
            if r[2] in dictEnd[r[0]]:
                dictEnd[r[0]][r[2]].append(r[1])
            else:
                dictEnd[r[0]][r[2]] = [r[1]]
        else:
            dictEnd[r[0]] = {}
            dictEnd[r[0]][r[2]] = [r[1]]

    #sort
    for key, value in dictEnd.items():
            for key1, value1 in value.items():
                value1 = value1.sort(reverse = True)
                #print(value1)
    print("OK done!")
    # print(dictEnd)
    count = 0
    for i in range(0, len(times)):
        for key, value in dictEnd.items():
            for key1, value1 in value.items():

                for v in value1:
                    if v <= times[i]:
                       data[key][i] = key1
                       count+=1
                       # print(count)
                       break;



    print("raw data done")
    #print(data.shape)

    # if(data.shape != '(2,)'):
    #     data = data.reshape(data, (-1, 2))

    dataO = np.append(dataO, data, axis=0)
    #print(dataO)

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


output = pd.DataFrame(dataO)
print("data done")

print(count)
print(len(ip))



output.to_csv("rnn32.csv", index = True, header = True)
print("all done")