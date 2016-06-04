import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import data


def get_key_points(day):
    df = data.read_data_with_timespans(day)
    df = df[df.timespan >= 30]
    kp = data.read_key_points()
    merged = pd.merge(df, kp, how='inner', on=['X', 'Y'], sort=False)
    return merged


def main():
    for day in data.days:
        merged = get_key_points(day).sort_values(by=['id', 'Timestamp'])
        save_path = os.path.join(data.data_in_path, 'key_points_{}.csv'.format(day))
        merged.to_csv(save_path, columns=['Timestamp', 'id', 'place_id', 'timespan'], index=False)

if __name__ == '__main__':
    main()