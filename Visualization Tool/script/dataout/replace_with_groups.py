"""
Creates a data file with a single trajectory for each group.
"""

import data
import pandas as pd
import os


for day in data.days:
    group_ids = data.read_group_typical_ids(day)
    for type_ in ['2', 'key-points']:
        print('-- {} {} --'.format(day, type_))
        print('Reading...')
        df = data.read_data(day, type_)

        print('Munging...')
        # get the list of all the columns...
        cols = df.columns
        # replace 'id' with 'group_id', so that when saving it'll be in the same position
        id_index = cols.searchsorted('id')
        save_cols = cols.values.copy()
        save_cols[id_index] = 'group_id'

        # filter ids that aren't 'typical ids'
        df = df[df['id'].isin(group_ids['id'])]
        # add the group information
        df2 = pd.merge(df, group_ids, on='id', how='left')

        print('Saving...')
        output_path = os.path.join(data.data_in_path, 'park-movement-groups-{}-{}.csv'.format(day, type_))
        # save the data without saving the id column, but using the group_id column in it's place
        df2.to_csv(output_path, columns=save_cols, index=False)
