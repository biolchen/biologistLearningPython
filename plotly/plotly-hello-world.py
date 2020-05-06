from plotly.graph_objs import Scatter, Figure, Layout
from plotly.offline import init_notebook_mode, plot, iplot
iplot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])