# for getting Matrix matrix for time period
import pandas as pd
import numpy as np

start = '2015-12-17 17:00:00'
duration = 300
frequency = '1min'

########################file process######################
file = pd.read_csv('output.csv')
file['end'] = pd.to_datetime(file['end'])
file['start'] = pd.to_datetime(file['start'])

#####################time processing###############

val = file.values
record = []

times = pd.date_range(start, periods=duration, freq=frequency)
times = np.array(times)

datStart = times[0]
datEnd = times[len(times) - 1]

print("filter start")
#filter
for i in range(0,len(val)):
    if (val[i][2] < datEnd and val[i][2] > datStart) or (val[i][3] < datEnd and val[i][3] > datStart):
        record.append(val[i])

print("Matrix Generating")
file = pd.DataFrame(record, columns=[0,1,2,3,4])


result1 = file.groupby([0, 1]).agg('count')

result1 = result1.reset_index()

result1 = result1.ix[:,0:2]

val = result1.values
result1 = pd.DataFrame(val, columns=['station', 'user', 'start'])
#for matrix
# result1 = result1.pivot(index = 'user', columns = 'station', values = 'start')
# result1 = result1.replace('NaN', 0)


result1.to_csv('visitMatrix2.csv', index = False)
result1.to_csv('../../Documents/code/NesTS-Vis/visitMatrix2.csv', index = False)




