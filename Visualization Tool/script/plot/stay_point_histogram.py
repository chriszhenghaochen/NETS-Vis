import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import data

df = data.read_data('Fri').sort_values(by=['id', 'Timestamp'])
df = df[(df.X.diff() != 0) | (df.Y.diff() != 0)]  # drop consecutive duplicates
tdiff = df.Timestamp.diff().shift(-1)
tdiff[df.id != df.id.shift(-1)] = pd.NaT
tdiff /= np.timedelta64(1, 's')  # convert to seconds so it works nicer
counts = tdiff.value_counts().sort_index()
counts = counts[counts > 5]  # discard small values
counts.plot(kind='bar')
