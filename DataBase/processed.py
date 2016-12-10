import pandas as pd
import numpy as np

#read
file = pd.read_csv('E:\SSP 2016\semester2\data\DATA_Mobile\input.csv')

#split
file = pd.DataFrame(file['station\tuser\tstart\tend\tx\ty\tip'].str.split('\t').tolist(), columns="station user start end x y visitingIp".split())

# #add new column
# file['out'] = np.random.choice(range(0, 10), file.shape[0])

#delete x and y
del file['x']
del file['y']

file['start'] = pd.to_datetime(file['start'],unit='s')
file['end'] = pd.to_datetime(file['end'],unit='s')


file = file.sort(['station', 'user', 'start'])

#save
file.to_csv('E:\SSP 2016\semester2\data\DATA_Mobile\output.csv',index = False)

