import data
import numpy as np

# lensum = 0
# for day in data.days:
#     df = data.read_data(day)
#     print('{}: length = {}'.format(day, len(df)))
#     lensum += len(df)
#     del df
#
# print('Average length = {}'.format(lensum / 3))

# for day in data.days:
#     print(day)
#     gi = data.read_group_info(day)
#     print('  num groups = {}'.format(len(gi)))
#     print('  num people = {}'.format(gi.sum()['size']))

ids = []
for day in data.days:
    groups = data.read_groups(day)
    ids.append(groups['id'].unique())
all_ids = np.concatenate(ids)
print('total visitors: {}'.format(len(all_ids)))

unique_ids, ids_counts = np.unique(all_ids, return_counts=True)
print('total unique visitors: {}'.format(len(unique_ids)))

counts, count_counts = np.unique(ids_counts, return_counts=True)
for count, count_count in zip(counts, count_counts):
    print('Visited {} times: {}'.format(count, count_count))