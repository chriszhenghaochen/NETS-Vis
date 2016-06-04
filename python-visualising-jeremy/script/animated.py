import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import data
from datetime import datetime


def get_positions_at(df, time) -> pd.DataFrame:
    return df.groupby('id', sort=False).apply(get_position_at, time=time)


# def get_position_at(path, time):
#     row1 = path[path.Timestamp < time].tail(1)
#     row2 = path[path.Timestamp >= time].head(1)
#     if row1.empty or row2.empty:
#         return pd.Series({'X': pd.NaN, 'Y': pd.NaN})
#     t1 = row1.iloc[0, 0]
#     t2 = row2.iloc[0, 0]
#     timedelta_total = t2 - t1
#     timedelta_total = t2 - t1
#     timedelta = time - t1
#     p1 = row1.loc[:, ['X', 'Y']].values[0]
#     p2 = row2.loc[:, ['X', 'Y']].values[0]
#     p3 = p1 + (p2 - p1) * (timedelta / timedelta_total)
#     return pd.Series({'X': p3[0], 'Y': p3[1]})

def get_position_at(path, time):
    index2 = path.index.union([time])
    return path.reindex(index2).interpolate('time').loc[time]


def animate(i):
    line
    return line,

def main():
    df = data.read_data('Fri', 'subset-100').set_index('Timestamp')
    time = pd.Timestamp(datetime(2014, 6, 6, 12))
    df2 = get_positions_at(df, time)

    im = data.read_image('Grey')
    fig, ax = plt.subplots()
    plt.imshow(im, extent=[0, 100, 0, 100])
    plt.plot()
    plt.show()
    ani = animation.FuncAnimation(fig, animate, blit=False, interval=10,
                              repeat=False)
    # ani = animation.FuncAnimation(fig, animate, blit=False,
    #    interval=10, repeat=True)


if __name__ == '__main__':
    main()