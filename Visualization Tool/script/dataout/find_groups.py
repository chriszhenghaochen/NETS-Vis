import script.analyse.trajectory_distance as td
from pprint import pprint
import itertools
import pandas as pd
import data
import os
import time
from datetime import timedelta

outdir = os.path.join(data.data_out_path, 'groups/')
os.makedirs(outdir, exist_ok=True)

cutoff = 300
for day in data.days:
    t0 = time.clock()
    print('Day {}'.format(day))
    td.initialise(day=day)
    # the first id of each group
    groups = []
    ids = td.all_ids
    total = len(ids)
    group_df = pd.DataFrame(index=ids, columns=['group_id'])
    for i, id in enumerate(ids):
        print('\r{}/{}'.format(i, total), end='')
        xy = td.df2.loc[:, id]
        # as the ids are roughly grouped in the correct groups already,
        # we check the first few most recently added groups first,
        # which will be at the end
        for id2 in itertools.islice(reversed(groups), 30):
            # check against the first id
            xy2 = td.df2.loc[:, id2]
            # calling the private method here because this way we can short circuit and be a little faster
            dist = td._get_trajectory_distance(xy, xy2)
            if dist < cutoff:
                group_df.loc[id, 'group_id'] = group_df.loc[id2, 'group_id']
                break
        else:  # if we didn't find a loop
            group_df.loc[id, 'group_id'] = len(groups)
            groups.append(id)
    print('\nDone!')
    print('Saving')
    file_path = os.path.join(outdir, 'groups-{}.csv'.format(day))
    group_df.to_csv(file_path, index_label='id')
    t1 = time.clock()
    print('Took {}'.format(timedelta(seconds=t1-t0)))
    print()