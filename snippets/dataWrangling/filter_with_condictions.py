from functools import reduce
import numpy as np
import pandas as pd

d = {'col1': [1, 2, 'NA', 7], 'col2': [3, 4, 5, 0]}
df = pd.DataFrame(data=d)

def filters(*con):
    return reduce(np.logical_and, con)

c1 = df['A']!='NA'
c2 = df['B']!=0

df_filtered = df[filters(c1,c2)]