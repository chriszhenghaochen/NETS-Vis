import pandas as pd
import os
import data

def main():
    for day in data.days:
        df = data.read_data(day)
        first = df.groupby('id').first()
        last = df.groupby('id').last()
        df2 = pd.concat([first[['X', 'Y']], last[['X', 'Y']]], axis=1,
                        keys=['first X', 'first Y', 'last X', 'last Y'])

        save_path = os.path.join(data.data_in_path, 'park-movement-{}-end-points.csv'.format(day))
        df2.to_csv(save_path)



if __name__ == '__main__':
    main()