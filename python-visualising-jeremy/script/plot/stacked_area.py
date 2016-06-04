import data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

kp = data.read_key_points()

pos = data.read_position_totals()

join_column = 'place_id'
# join_column = 'category'
ts = pd.date_range('2014-06-06 08:00:00', '2014-06-08 23:55:00', freq='1T')
# change x and y coordinates to place ids
rides = (
    pd.merge(pos, kp.loc[:, ['X', 'Y', join_column]], on=['X', 'Y'], how='left', sort=False)
    .drop(['X', 'Y'], 1)
)

# total amount of minutes spends at a destination across the whole day (approximately)
ride_totals = (
    rides.dropna()
    .groupby(join_column)
    .sum()
    .sort_values('total', ascending=False)
)

cutoff = ride_totals.iloc[17]['total']  # the 18th most ride is at index 17
cutoff_ids = ride_totals[ride_totals['total'] >= cutoff].index
cutoff_ids = np.append(cutoff_ids, [0, -1])

rides = rides.fillna(-1)
# join places below cut-off into one group
rides.loc[~rides[join_column].isin(cutoff_ids), join_column] = 0

df2 = (
    rides.groupby([join_column, 'Timestamp'])
    .sum()
    .unstack(0)
    .reindex(ts)
    .fillna(0)
    .loc[:, 'total']
    # order by the sorted ideas
    .loc[:, cutoff_ids]
)

palette = data.palette20
plt.stackplot(ts, df2.transpose(), linewidth=0, colors=palette)

# creating the legend
legend_df = pd.DataFrame(data=df2.columns, columns=['place_id'])
legend_df = pd.merge(legend_df, kp, on='place_id', how='left')
legend_df.loc[legend_df['place_id'] == 0, 'name'] = 'Other Attractions'
legend_df.loc[legend_df['place_id'] == -1, 'name'] = 'On Path'
# reverse the order (which is what this weird snippet does)
legend_df = legend_df.iloc[::-1]

plt.legend([mpatches.Patch(color=palette[i]) for i in legend_df.index],
           legend_df['name'],
           loc='upper left',
           prop={'size': 8})

plt.show()
