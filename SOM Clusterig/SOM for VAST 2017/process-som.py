import pandas as pd

file = pd.read_csv('input.csv')

result1 = file.groupby(['id','gate']).agg('count')

result1 = result1.reset_index()

result1 = result1.ix[:,0:3]
#result1['Timestamp'] = result1['Timestamp'].values.astype('int')

result1 = result1.pivot(index = 'id', columns = 'gate', values = 'Timestamp')
result1 = result1.replace('NaN', 0)
result1 = result1.astype('int')

result1.to_csv('som.csv')