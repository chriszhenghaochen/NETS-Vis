import pandas as pd
import numpy as np
import time as time
from matplotlib import pyplot as plt
pd.__version__
from pandas.tools.plotting import scatter_matrix
import sys
import sompy as SOM

attr = np.arange(1,71)
dim = len(attr)

file_fri1 = pd.read_csv('C:/Users/zchen4/Desktop/data/attraction frequency/freqs_Fri.csv')
print file_fri1.head()

# file_sat1 = pd.read_csv('C:/Users/zchen4/Desktop/data/attraction frequency/freqs_Sat.csv')
# file_sun1 = pd.read_csv('C:/Users/zchen4/Desktop/data/attraction frequency/freqs_Sun.csv')

label_fri1 = file_fri1['id'].values
# label_sat1 = file_sat1['id'].values
# label_sun1 = file_sun1['id'].values

data_fri1 = file_fri1.ix[:,1:71].values
# data_sat1 = file_sat1.ix[:,1:71].values
# data_sun1 = file_sun1.ix[:,1:71].values

msz0 = 30
msz1 = 30

sm = SOM.SOM('sm',data_fri1, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm.train(n_job = 1, shared_memory = 'no',verbose='final')

sm.view_map(text_size=7)

# df = pd.DataFrame(data = data_fri1, columns= attr)
# fig = scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal='kde')

plt.show()

