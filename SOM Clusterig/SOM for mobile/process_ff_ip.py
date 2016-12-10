import pandas as pd

file = pd.read_csv('output.csv')

file = file[file['station'] == 10]

result1 = file.groupby(['user','visitingIp']).agg('count')

result1 = result1.reset_index()

result1 = result1.ix[:,0:3]

#for matrix
result1 = result1.pivot(index = 'user', columns = 'visitingIp', values = 'station')
result1 = result1.replace('NaN', 0)


result1.to_csv('ipstat1.csv')