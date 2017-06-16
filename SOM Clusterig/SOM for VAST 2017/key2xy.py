import pandas as pd
import numpy as np

input = pd.read_csv('input.csv')
key = pd.read_csv('key points.csv')

iv = input.values.tolist()
kv = key.values

dic = {}

for i in kv:
    dic[i[1]] = [float(i[2]), float(i[3])]

for i in iv:
    i.append(dic[i[3]][0])
    i.append(dic[i[3]][1])

out = pd.DataFrame(iv, columns = ['time','id','type','gate','x','y'])
out.to_csv('out.csv', index= False)