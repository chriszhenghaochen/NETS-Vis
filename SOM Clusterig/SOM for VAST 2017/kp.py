import pandas as pd

file = pd.read_csv('key points_1.csv')

x = file['x'].values
x1 = 100 - x

file['x'] = x1

# y = file['y'].values
# y1 = 100 - y
#
# file['y'] = y1

file.to_csv('key points.csv',index = False)
