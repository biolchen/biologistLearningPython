import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode='lines+markers+text',
    name='Lines, Markers and Text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='top center'
)

trace2 = go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode='markers+text',
    name='Markers and Text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

trace3 = go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode='lines+text',
    name='Lines and Text',
    text=['Text G', 'Text H', 'Text I'],
    textposition='bottom center'
)

data = [trace1, trace2, trace3]

layout = go.Layout(
    showlegend=False
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)