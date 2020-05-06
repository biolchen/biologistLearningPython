import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot

data = [
    go.Scatter(
        x=[0, 1, 2],
        y=[1, 3, 2],
        mode='markers',
        text=['Text A', 'Text B', 'Text C']
    )
]

layout = go.Layout(
    title='Hover over the points to see the text'
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)