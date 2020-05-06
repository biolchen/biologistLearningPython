
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objs as go
import os
os.chdir(os.path.dirname(__file__))


df=pd.read_csv("slide_timeSeries.csv")

trace_high = go.Scatter(
                x=df.contb_receipt_dt,
                y=df['Clinton, Hillary Rodham'],
                name = "Clinton",
                line = dict(color = '#0015bc'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=df.contb_receipt_dt,
                y=df['Trump, Donald J.'],
                name = "Trump",
                line = dict(color = '#ff0000'),
                opacity = 0.8)

data = [trace_high, trace_low]

layout = dict(
    title = "Comparison of Donation to Clinton and Trump in 2016 (USD)",
    xaxis = dict(
        range = ['2015-05-01','2016-10-18'],
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=12,
                     label='12m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    
    )
)

fig = dict(data=data, layout=layout)
iplot(fig)