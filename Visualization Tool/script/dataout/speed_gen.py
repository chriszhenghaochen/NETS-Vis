import pandas as pd
import numpy as np
import data

df = data.read_data('Fri')

i = 0
for name, group in df.groupby('id'):
    t_diff = group.Timestamp.diff().fillna(0) / np.timedelta64(1, 's')
    x_diff = group.X.diff().fillna(0)
    y_diff = group.Y.diff().fillna(0)
    diffs = np.hypot(x_diff, y_diff)
    dist = diffs.cumsum()
    speed = (diffs / t_diff).fillna(0)
    df2 = pd.DataFrame({'Timestamp': group.Timestamp, 'dist': dist, 'speed': speed})
    df2.to_csv("dist_speed_{}.csv".format(name), index=False)
    i += 1
    # if i > 10:
    #     break
