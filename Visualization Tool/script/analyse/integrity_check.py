"""
Script to check for some anomalies in the data

At the moment, this just checks to make sure that nobody 'teleports' around the park
"""

import data
import os
import zipfile


def find_teleporters():
    for day in data.days:
        print('-- {} --'.format(day))
        # for testing use a smaller subset of the data
        df = data.read_data(day)
        for name, group in df.groupby('id'):
            x, y = group.loc[:, ['X', 'Y']].diff().abs().max()
            if x > 3 or y > 3:
                print('id {}, x = {}, y = {}'.format(name, x, y))


def check_for_sunday_weirdness():
    data_path = 'park-movement-Sun-2.csv'
    full_path = os.path.join(data.data_in_path, data_path)
    # these two are specific to the machine at my desk
    original_path = 'C:/Users/jswanson/Documents/vast_to_student/data/MC1 Data June 2015 V3/park-movement-Sun.csv'
    zipped_path = 'C:/Users/jswanson/Documents/vast_to_student/data/MC1 Data June 2015 V3.zip'

    print('{sep} Edited Data {sep}'.format(sep='-'*10))
    with open(full_path, 'r') as f:
        for i, line in enumerate(f):
            if line.count(',') != 4:
                print('{}: {}'.format(i, line), end='')

    print('{sep} Original Data {sep}'.format(sep='-'*10))
    if os.path.exists(original_path):
        with open(original_path, 'r') as f:
            for i, line in enumerate(f):
                if line.count(',') != 4:
                    print('{}: {}'.format(i, line), end='')
    else:
        print("Can't find original data.")

    print('{sep} Data from zip {sep}'.format(sep='-'*10))
    if os.path.exists(zipped_path):
        with zipfile.ZipFile(zipped_path) as z:
            with z.open('park-movement-Sun.csv', 'r') as f:
                for i, line in enumerate(f):
                    if line.count(b',') != 4:
                        print('{}: {}'.format(i, line), end='')
    else:
        print("Can't find zipped data.")


def fix_sunday_weirdness():
    in_name = 'park-movement-Sun-2.csv'
    out_name = 'park-movement-Sun-3.csv'
    in_path = os.path.join(data.data_in_path, in_name)
    out_path = os.path.join(data.data_in_path, out_name)

    with open(in_path, 'r') as in_f, open(out_path, 'w') as out_f:
        for line in in_f:
            if line.count(',') == 4:
                out_f.write(line)
            else:
                print('skipped line {}'.format(line))
    print('Done! Now you need to rename/remove the file')


def main():
    # fix_sunday_weirdness()
    check_for_sunday_weirdness()


if __name__ == '__main__':
    main()