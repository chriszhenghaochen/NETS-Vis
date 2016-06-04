import data

df = data.read_data('Fri', 'subset-100')
df2 = df.groupby('id').resample('15T', how='first', fill_method='pad')
# convert to string then do a thing