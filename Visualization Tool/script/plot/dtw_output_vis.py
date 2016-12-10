import data
import matplotlib.pyplot as plt

df1 = data.read_dist_speed('2672')
df2 = data.read_dist_speed('4343')
dtw = data.read_dtw('distance')

df1_warped = df1.loc[dtw.iloc[:, 0]]
df2_warped = df2.loc[dtw.iloc[:, 1]]

fig, ax = plt.subplots(2, 1)

plt.sca(ax[0])
plt.plot(df1.speed)
plt.plot(df2.speed)

plt.sca(ax[1])
plt.plot(df1.Timestamp, df1.speed)
plt.plot(df2.Timestamp, df2.speed)

plt.show()