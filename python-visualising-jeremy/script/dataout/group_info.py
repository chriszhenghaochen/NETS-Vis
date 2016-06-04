import data
import os

for day in data.days:
    print(day)
    group_typical_id = data.read_group_typical_ids(day)
    id_groups = data.read_groups(day)
    group_info = group_typical_id.set_index('group_id')
    # group_info.columns = ['typical_id']
    sizes = id_groups['group_id'].value_counts()
    group_info['size'] = sizes
    out_file = os.path.join(data.data_out_path, 'groups/group-info-{}.csv'.format(day))
    group_info.to_csv(out_file)