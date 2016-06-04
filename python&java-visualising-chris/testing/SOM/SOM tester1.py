import pandas as pd
import time as time
import numpy as np
from matplotlib import pyplot as plt
pd.__version__
import sys
import sompy as SOM

#The critical factor which increases the computational time, but mostly the memory problem is the size of SOM (i.e. msz0,msz1),
#other wise the training data will be parallelized


#This is your selected map size
msz0 = 30
msz1 = 30

#This is a random data set, but in general it is assumed that you have your own data set as a numpy ndarray
Data = np.random.rand(10*1000,20)
print 'Data size: ', Data.shape

#Put this if you are updating the sompy codes otherwise simply remove it
reload(sys.modules['sompy'])


sm = SOM.SOM('sm', Data, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm.train(n_job = 1, shared_memory = 'no',verbose='final')

sm.view_map(text_size=7)

dlen = 200
Data1 = pd.DataFrame(data= 1*np.random.rand(dlen,2))
Data1.values[:,1] = (Data1.values[:,0][:,np.newaxis] + .42*np.random.rand(dlen,1))[:,0]


Data2 = pd.DataFrame(data= 1*np.random.rand(dlen,2)+1)
Data2.values[:,1] = (-1*Data2.values[:,0][:,np.newaxis] + .62*np.random.rand(dlen,1))[:,0]

Data3 = pd.DataFrame(data= 1*np.random.rand(dlen,2)+2)
Data3.values[:,1] = (.5*Data3.values[:,0][:,np.newaxis] + 1*np.random.rand(dlen,1))[:,0]


Data4 = pd.DataFrame(data= 1*np.random.rand(dlen,2)+3.5)
Data4.values[:,1] = (-.1*Data4.values[:,0][:,np.newaxis] + .5*np.random.rand(dlen,1))[:,0]


DataCL1 = np.concatenate((Data1,Data2,Data3,Data4))

fig = plt.figure()
plt.plot(DataCL1[:,0],DataCL1[:,1],'ob',alpha=0.2, markersize=4)
fig.set_size_inches(7,7)

sm2 = SOM.SOM('sm', DataCL1, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm2.train(n_job = 1, shared_memory = 'no',verbose='final')

sm2.view_map(text_size=7)

##Hit map
sm2.hit_map()

a= sm2.view_U_matrix(distance2=2, row_normalized='No', show_data='Yes', contooor='Yes', blob='No', save='No', save_dir='')

labels = sm2.cluster(method='Kmeans', n_clusters=4)
sm2.cluster_labels[:10]

cents  = sm2.hit_map_cluster_number()

dlen = 700
tetha = np.random.uniform(low=0,high=2*np.pi,size=dlen)[:,np.newaxis]
X1 = 3*np.cos(tetha)+ .22*np.random.rand(dlen,1)
Y1 = 3*np.sin(tetha)+ .22*np.random.rand(dlen,1)
Data1 = np.concatenate((X1,Y1),axis=1)

X2 = 1*np.cos(tetha)+ .22*np.random.rand(dlen,1)
Y2 = 1*np.sin(tetha)+ .22*np.random.rand(dlen,1)
Data2 = np.concatenate((X2,Y2),axis=1)

X3 = 5*np.cos(tetha)+ .22*np.random.rand(dlen,1)
Y3 = 5*np.sin(tetha)+ .22*np.random.rand(dlen,1)
Data3 = np.concatenate((X3,Y3),axis=1)

X4 = 8*np.cos(tetha)+ .22*np.random.rand(dlen,1)
Y4 = 8*np.sin(tetha)+ .22*np.random.rand(dlen,1)
Data4 = np.concatenate((X4,Y4),axis=1)



DataCL2 = np.concatenate((Data1,Data2,Data3,Data4),axis=0)

fig = plt.figure()
plt.plot(DataCL2[:,0],DataCL2[:,1],'ob',alpha=0.2, markersize=4)
fig.set_size_inches(7,7)
# plt.plot(np.cos(tetha))

sm3 = SOM.SOM('sm', DataCL2, mapsize = [msz0, msz1],norm_method = 'var',initmethod='pca')
sm3.train(n_job = 1, shared_memory = 'no',verbose='final')

sm3.hit_map()

labels = sm3.cluster(method='Kmeans', n_clusters=4)
sm2.cluster_labels[:10]

cents  = sm3.hit_map_cluster_number()

a= sm3.view_U_matrix(distance2=1, row_normalized='No', show_data='Yes', contooor='Yes', blob='No', save='No', save_dir='')

# plt.show()