import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

data = pd.read_json('https://cdn.rawgit.com/plotly/datasets/master/BulletData.json')

fig = ff.create_bullet(
    data, markers='markers', measures='measures',
    ranges='ranges', subtitles='subtitle', titles='title',
)
iplot(fig)