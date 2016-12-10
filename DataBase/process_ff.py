import pandas as pd

file = pd.read_csv('output.csv')

result1 = file.groupby(['station', 'user']).agg('count')

result1 = result1.reset_index()

result1 = result1.ix[:,0:3]

#for matrix
# result1 = result1.pivot(index = 'user', columns = 'station', values = 'start')
# result1 = result1.replace('NaN', 0)


result1.to_csv('statf1.csv', index = False)