import pandas as pd
import numpy as np

#read
file = pd.read_csv('output.csv')

ips = file['visitingIp'].unique()

pd.DataFrame(ips).to_csv('ip.csv',index = False)

ips = file['user'].unique()

pd.DataFrame(ips).to_csv('user.csv',index = False)

ips = file['station'].unique()

pd.DataFrame(ips).to_csv('station.csv',index = False)