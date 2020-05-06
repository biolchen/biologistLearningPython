import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import plot, iplot

import numpy as np

X = np.random.rand(15, 15)
dendro = ff.create_dendrogram(X)
dendro['layout'].update({'width':800, 'height':500})
iplot(dendro)