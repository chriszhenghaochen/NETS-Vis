import pandas as pd
import numpy as np


# names = ['car2', 'truck2', 'truck3', 'truck4', 'bus2', 'bus3']
#
# for name in names:
#     file = pd.read_csv(name + '.csv')
#     id = np.unique(file['id'].values)
#     out = pd.DataFrame(id)
#     out.to_csv('n' + name, header = ['id'], index = False)


file = pd.read_csv('input.csv')
id = np.unique(file['gate'].values)
out = pd.DataFrame(id)
out.to_csv('gate.csv', header = ['id'], index = False)