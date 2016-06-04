import pandas as pd
import numpy as np
import data
import matplotlib.pyplot as plt


def main():
    day = 'Fri'

    df = data.read_data_with_timespans(day)

    key_points = method1(df)
    scatter_on_image(key_points, 0.0001)
    key_points.to_csv('key points.csv')


def method1(df):
    df2 = df[df.timespan > 15]
    sums = df2.groupby(['X', 'Y'])['timespan'].sum()
    return sums #[sums > 15000]


def scatter_on_image(df, scale=0.1):
    im = data.read_image()
    (x, y) = zip(*df.index.values)
    plt.imshow(im, extent=[0, 100, 0, 100])
    plt.scatter(x, y, s=scale * df.values, color='red')
    plt.scatter(x, y, color='blue', marker='x')
    plt.axis([0, 100, 0, 100])


if __name__ == '__main__':
    main()
