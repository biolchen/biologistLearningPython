import plotly.graph_objects as go
import pandas as pd
import os
os.chdir(os.path.dirname(__file__))

df = pd.read_csv('2014_usa_states.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='lavender',
               align='left'))
])

fig.show()