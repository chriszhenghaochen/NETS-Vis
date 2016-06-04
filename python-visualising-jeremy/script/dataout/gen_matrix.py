import data
import os
import pandas as pd


def get_visit_matrix(day=None, groupby='place_id', df=None, timespan=False, use_groups=False) -> pd.DataFrame:
    if df is None:
        df = data.read_visited_key_points(day, ['category'], grouped=use_groups)
    if use_groups:
        id_ = 'group_id'
    else:
        id_ = 'id'
    # entry and exit details seem inconsistent, so filter them out
    df = df[df.category != 'Entry/Exit']
    # Group by id and place_id, then count occurrences or sum total time
    if timespan:
        df2 = df.groupby([id_, groupby])['timespan'].sum()
    else:
        df2 = df.groupby([id_, groupby]).size()
    # Rearrange into a matrix where the place_ids are the columns
    df2 = df2.unstack(groupby).fillna(0).astype('int64')
    return df2


def main():
    dir = os.path.join(data.data_out_path, 'matrices/')
    # make the directory if it doesn't exist
    os.makedirs(dir, exist_ok=True)

    for day in data.days:
        for use_groups in [True, False]:
            df = data.read_visited_key_points(day, ['category'], grouped=use_groups)
            for timespan in [True, False]:
                for groupby in ['place_id', 'category']:
                    print('{}: {}, timespan={}, grouped={}'.format(day, groupby, timespan, use_groups))

                    m = get_visit_matrix(day, groupby, df=df, timespan=timespan, use_groups=use_groups)

                    if timespan:
                        path = 'timespans_'
                    else:
                        path = 'freqs_'
                    path += day
                    if groupby == 'category':
                        path = 'category_' + path
                    if use_groups:
                        path += '_grouped'
                    path += '.csv'

                    full_path = os.path.join(dir, path)
                    m.to_csv(full_path)


if __name__ == '__main__':
    main()