import data
import numpy as np
import random
import gc
import os


def main():
    all_ids = set()
    for day in data.days:
        ids = data.read_data(day)['id'].unique()
        all_ids.update(ids)

    for day in data.days:
        df = data.read_data(day)
        # subset amount
        for s in [10, 30, 100, 300]:
            subset_ids = random.sample(all_ids, len(all_ids) // s)
            df2 = df[df.id.isin(subset_ids)]
            file_name = 'park-movement-{}-subset-{}.csv'.format(day, s)
            full_path = os.path.join(data.data_in_path, file_name)
            df2.to_csv(full_path, index=False)
        # explicitly free up some memory
        df = None
        df2 = None
        gc.collect()

if __name__ == '__main__':
    main()