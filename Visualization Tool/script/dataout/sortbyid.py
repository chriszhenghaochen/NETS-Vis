import pandas as pd
import os

filepath = 'C:/Users/jswanson/Documents/vast_to_student/data/MC1 Data June 2015 V3'

df = pd.read_csv(os.path.join(filepath, 'park-movement-Fri-FIXED-2.0.csv'))
df2 = df.sort_values(by=['id', 'Timestamp'])
df2.to_csv("sorted.csv", index=False)
