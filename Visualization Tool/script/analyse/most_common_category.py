import data
import pandas as pd


def get_most_common(day, column, use_categories=None, ignore_categories=None) -> pd.DataFrame:
    df = data.read_visited_key_points(day, ['category'])
    if use_categories is not None:
        df = df[df.category.isin(use_categories)]
    elif ignore_categories is not None:
        df = df[~df.category.isin(ignore_categories)]
    return df.groupby('id')[column].agg(lambda x: x.value_counts().index[0])


def main():
    for day in data.days:
        print('Most popular category ({}):'.format(day))
        print(get_most_common(day, 'category', ignore_categories=['Restrooms', 'Entry/Exit']).value_counts())
        print()
    for day in data.days:
        print('Most popular attraction ({}):'.format(day))
        most_common = get_most_common(day, 'place_id', ignore_categories=['Restrooms', 'Entry/Exit']).value_counts()
        most_common = pd.DataFrame(most_common)
        most_common = most_common.reset_index()
        most_common.columns = ['place_id', 'count']
        # merge with place id to get category and name
        kp = data.read_key_points()
        most_common = pd.merge(most_common, kp.loc[:, ['place_id', 'category', 'name']], on='place_id', sort=False)
        print(most_common)
        print()


if __name__ == '__main__':
    main()