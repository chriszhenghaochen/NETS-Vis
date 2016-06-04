import data
import script.plot.timecube as tc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('C:/Users/zchen4/Desktop/data/outputlab1.csv') as f1:
    data1 = f1.read()


data1 = data1.split('\n')
x1 = [row for row in data1]

x1 = x1[:len(x1)-1]

print(x1)

x1 = map(int, x1)

with open('C:/Users/zchen4/Desktop/data/outputlab2.csv') as f2:
    data2 = f2.read()


data2 = data2.split('\n')
x2 = [row for row in data2]

x2 = x2[:len(x2)-1]

print(x2)

x2 = map(int, x2)

df = data.read_data('Fri')

tc.plot_trajectories(df[df['id'].isin(x1)])
plt.show()

tc.plot_trajectories(df[df['id'].isin(x2)])
plt.show()

