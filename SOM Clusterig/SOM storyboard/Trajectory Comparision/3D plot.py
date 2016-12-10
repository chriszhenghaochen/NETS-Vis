import data
import script.plot.timecube as tc
import matplotlib.pyplot as plt



with open('C:/Users/zchen4/Desktop/data/outputlab.csv') as f1:
    data1 = f1.read()


data1 = data1.split('\n')
x1 = [row for row in data1]

x1 = x1[:len(x1)-1]

print(x1)

x1 = map(int, x1)


df = data.read_data('Fri')

tc.plot_trajectories(df[df['id'].isin(x1)])

plt.show()
