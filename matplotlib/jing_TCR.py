import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn=sqlite3.connect('/Users/liangchen/Dropbox/input/db/jing_TCR.db')

V_count=pd.read_sql_query('select * from V_count', conn)
df=V_count.head(100)
df
V_count.head()
sample_list=[
"CeD_KIR_NEG","CeD_KIR_POS","HD_KIR_NEG2","HD_KIR_NEG3",
"HD_KIR_NEG4","HD_KIR_NEG","HD_KIR_POS2","HD_KIR_POS3",
"HD_KIR_POS4","HD_KIR_POS","MS_KIR_NEG1","MS_KIR_NEG2",
"MS_KIR_NEG","MS_KIR_POS1","MS_KIR_POS2","MS_KIR_POS",
"SLE_KIR_NEG2","SLE_KIR_NEG3","SLE_KIR_NEG4","SLE_KIR_NEG",
"SLE_KIR_POS2","SLE_KIR_POS3","SLE_KIR_POS4","SLE_KIR_POS",
]
df1=pd.melt(df, id_vars=['index'], value_vars=sample_list)
df1

##
["{0} ({1})".format(n[0], n[1]) for n in df[['class', 'counts']].itertuples()]

V_count.head(100)
df_example=V_count[['index','CeD_KIR_NEG']]


#! pip install pywaffle
# Reference: https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart
from pywaffle import Waffle
# Import
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')
df

df_example=V_count[['index', 'CeD_KIR_NEG']].sort_values(['CeD_KIR_NEG'], ascending=False).head(5)


n_categories = df_example.shape[0]
colors = [plt.cm.inferno_r(i/float(n_categories)) for i in range(n_categories)]
# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '111': {
            'values': df_example['CeD_KIR_NEG'],
            'labels': ["{0} ({1})".format(n[0], n[1]) for n in df_example[['index', 'CeD_KIR_NEG']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12},
            'title': {'label': '# Vehicles by Class', 'loc': 'center', 'fontsize':18}
        },
    },
    rows=7,
    colors=colors,
    figsize=(16, 9)
)
#plt.show()

plt.savefig('/Users/liangchen/Dropbox/output/Jing/test.pdf', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
##