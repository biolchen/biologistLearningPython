# https://altair-viz.github.io/user_guide/compound_charts.html

import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data

alt.renderers.enable("altair_viewer")

cars = data.cars()
cars['Make'] = cars['Name'].str.split(' ').str[0]


chart1 = alt.Chart(cars).mark_circle(opacity=.33).encode(
    x = 'Horsepower',
    y = 'Miles_per_Gallon',
    color = 'Origin',
    size = 'Acceleration'
).interactive()

chart2 = alt.Chart(cars).mark_bar().encode(
    y = 'Origin',
    x = 'count()',
    color = 'Cylinders:N'
)

chart3 = alt.Chart(cars).mark_area(opacity=.33, interpolate='step').encode(
    x = alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=20)),
    y = alt.Y('count()', stack=None),
    color = 'Origin'
)


chart4 = alt.Chart(cars).mark_circle().encode(
    alt.X(alt.repeat('column'), type='quantitative'),
    alt.Y(alt.repeat('row'), type='quantitative'),
    color = 'Origin'
).properties(
    width = 150,
    height = 150
).repeat(
    row=['Horsepower', 'Acceleration', 'Miles_per_Gallon'],
    column=['Horsepower', 'Acceleration', 'Miles_per_Gallon']
).interactive()


chart5 = alt.Chart(cars).mark_line().encode(
    x='Year:T',
    y='count()',
    color='Origin'
).properties(
    width = 500,
    height = 500
)

chart6 = alt.Chart(cars).mark_area().encode(
    x='Year:T',
    y='count()',
    color = 'Origin'
)

chart7 = alt.Chart(cars).mark_line().encode(
    x = 'Year:T',
    y = 'mean(Weight_in_lbs)',
    color = 'Origin'
)





chart8 = alt.Chart(cars).mark_bar().encode(
x= alt.X('Make', sort=alt.EncodingSortField(field='count',op='count',order='descending')),
    y='count()'
)

from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

cars_df = pd.DataFrame(cars)
X_cars = cars_df.select_dtypes(include=[np.number]).dropna().values
X_embedding = TSNE(n_components=2).fit_transform(X_cars)
clustering = KMeans(n_clusters=3, random_state=0).fit(X_cars)
df = pd.DataFrame(X_embedding)
df['cindex'] = clustering.labels_
df.columns = ['x', 'y', 'cindex']
chart9 = alt.Chart(df).mark_circle().encode(
    x = 'x',
    y = 'y',
    color = 'cindex:N')


    
from altair import datum

chart10 = alt.Chart(cars).transform_window(
    index='count()'
).transform_fold(
    ['Miles_per_Gallon', 'Cylinders', 'Displacement','Horsepower']
).transform_joinaggregate(
    min='min(value)',
    max='max(value)',
    groupby=['key']
).transform_calculate(
    minmax_value=(datum.value-datum.min)/(datum.max-datum.min),
    mid=(datum.max+datum.min)/2
).mark_line().encode(
    x='key:N',
    y='minmax_value:Q',
    color='Origin:N',
    detail='index:N'
).properties(
    width=700
)



(chart1| chart2| chart3 | chart4 | chart5 | chart6 | chart7 | chart8 | chart9 | chart10).show()