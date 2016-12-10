"""
Script to select a person from each group that most represents that group.

Basically looks for the person with the least distance to each other person.

I guess instead of writing to a separate file, I could just sort the ids within each group.
Only problem there is that the order is easily lost with pandas operations
"""

import data
import itertools
import pandas as pd
import numpy as np
import script.analyse.trajectory_distance as td
import os
import time
from datetime import timedelta

outdir = os.path.join(data.data_out_path, 'groups/')
os.makedirs(outdir, exist_ok=True)

for day in data.days:
    print('-- {} --'.format(day))
    t0 = time.clock()
    td.initialise(day)
    groups = data.read_groups(day)
    group_ids = groups['group_id'].unique()
    n_groups = len(group_ids)
    typical_group_people = pd.DataFrame(index=group_ids, columns=['id'])
    for group_id, group_df in groups.groupby('group_id'):
        print('\r{}/{}'.format(group_id, n_groups), end='')
        # if there's just one person in this group, then we can just take them alone
        # if there's 2 people in a group, we can arbitrarily pick one. I pick the first one.
        if len(group_df) <= 2:
            typical_group_people.loc[group_id, 'id'] = group_df.iloc[0]['id']
        else:
            n_ids = len(group_df)
            dists = np.zeros([n_ids, n_ids])
            for i1, i2 in itertools.combinations(range(n_ids), 2):
                # In the 1D and 2D case, squaring numbers is the better way to get the middle point
                dist = td.get_distances(group_df.iloc[i1]['id'], group_df.iloc[i2]['id']) ** 2
                dists[i1, i2] = dist
                dists[i2, i1] = dist
            # sum along one axis to get the distance of one path to the others.
            best_index = dists.sum(0).argmin()
            typical_group_people.loc[group_id, 'id'] = group_df.iloc[best_index]['id']
    print('\nDone!')
    print('Saving')
    file_path = os.path.join(outdir, 'group-typical-id-{}.csv'.format(day))
    typical_group_people.to_csv(file_path, index_label='group_id')
    t1 = time.clock()
    print('Took {}'.format(timedelta(seconds=t1-t0)))
    print()
