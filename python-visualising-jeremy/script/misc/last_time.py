"""
Find the last timestamp for each day.

Well, all this is doing is outputting the last line of each file
"""

import data
import os

for day in ['Fri', 'Sat', 'Sun']:
    data_path = 'park-movement-{}-{}.csv'.format(day, '2')
    full_path = os.path.join(data.data_in_path, data_path)

    last_line = ''
    with open(full_path) as f:
        for line in f:
            last_line = line
    print('-- {} --'.format(day))
    print(last_line)
    print()
