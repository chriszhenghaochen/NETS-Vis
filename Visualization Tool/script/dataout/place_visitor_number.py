import data
import os

dfs = {}
for day in data.days:
    print('Working on day {}'.format(day))
    # these are done all together to reduce the maximum amount of memory python uses
    df = (
        data.read_data(day)
        # resample the data for each person into samples every 1 minute
        .set_index('Timestamp')
        .groupby('id')
        .resample('1T', how='last', label='right', closed='right', fill_method='pad')
        .reset_index()
        # count the total number of people at each time and each point
        .groupby(['Timestamp', 'X', 'Y'])
        .size()
        .reset_index(name='total')
    )
    dfs[day] = df
print('Merging...')
df = dfs['Fri'].append([dfs['Sat'], dfs['Sun']])
print('Saving...')
path = os.path.join(data.data_out_path, 'position_totals.csv')
df.to_csv(path, index=False)
print('Done!')
