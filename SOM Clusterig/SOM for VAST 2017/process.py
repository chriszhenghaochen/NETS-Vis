import pandas as pd

names = ['car2.csv', 'tuck2.csv', 'truck3.csv', 'truck4.csv', 'bus2.csv', 'bus3.csv']

for name in names:

    file = pd.read_csv(name)

    result1 = file.groupby(['id','gate']).agg('count')

    result1 = result1.reset_index()

    result1 = result1.ix[:,0:3]

    #for matrix
    # result1 = result1.pivot(index = 'user', columns = 'visitingIp', values = 'station')
    # result1 = result1.replace('NaN', 0)


    result1.to_csv('stat' + name + '.csv', index = False)