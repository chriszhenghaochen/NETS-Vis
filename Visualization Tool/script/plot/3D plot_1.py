import data
import script.plot.timecube_1 as tc
import matplotlib.pyplot as plt
import pandas as pd



with open('outputlab.csv') as f1:
    data1 = f1.read()


data1 = data1.split('\n')
x1 = [row for row in data1]

x1 = x1[:len(x1)-1]

print(x1)

df = pd.read_csv('out.csv', parse_dates=['time'])
print(df[df['id'].isin(x1)])

tc.plot_trajectories(df[df['id'].isin(x1)])

plt.show()
