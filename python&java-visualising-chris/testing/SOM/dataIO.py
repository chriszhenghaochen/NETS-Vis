import pandas as pd
import pandas as pd
import time as time
import numpy as np
from matplotlib import pyplot as plt
pd.__version__
import sys
import sompy as SOM
from pandas.tools.plotting import scatter_matrix
from pandas import Series, DataFrame


file_fri_1 = pd.read_csv('C:/Users/zchen4/Desktop/data/attraction frequency/freqs_Fri.csv')

print file_fri_1.head()

data_fri_1 = file_fri_1.ix[:,1:72].values

labour_fri_1 = file_fri_1['id'].values.astype('str')

attr =  file_fri_1.columns.values.astype('str')

msz0 = 30
msz1 = 30

Data = data_fri_1
print 'Data size: ', Data.shape
#Put this if you are updating the sompy codes
reload(sys.modules['sompy'])

t0 = time.time()
sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')

sm.init_map()

sm.train(n_job = 1, shared_memory = 'no',verbose='off')

print 'Training is done in: ', time.time()-t0, 'seconds'

a = sm.view_map( what='codebook', which_dim='all',
            pack='Yes', text_size=2.8, save='No',
            save_dir='empty', grid='No', text='Yes', cmap='None', COL_SiZe=6)

b = sm.hit_map()

labels = sm.cluster(method='Kmeans', n_clusters=10)
sm.cluster_labels[:10]

c = sm.hit_map_cluster_number()
d = sm.view_U_matrix(distance2=2, row_normalized='No', show_data='Yes', contooor='Yes', blob='No', save='No', save_dir='')

plt.show()