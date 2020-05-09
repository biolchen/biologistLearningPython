import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import os
os.chdir(os.path.dirname(__file__))
import pandas as pd
import matplotlib.pyplot as plt

import plotly.offline as py
from plotly.offline import init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import plotly.tools as tls
import seaborn as sns
import warnings


country = pd.read_csv('../plotly/API_ILO_country_YU.csv',encoding= 'unicode_escape')

country_list = ['Afghanistan','Angola','Albania','Argentina','Armenia','Australia'
,'Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria'
,'Bahrain','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Barbados','Brunei Darussalam'
,'Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Cameroon'
,'Congo','Colombia','Comoros','Cabo Verde','Costa Rica','Cuba','Cyprus','Czech Republic','Germany'
,'Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Spain','Estonia','Ethiopia','Finland','Fiji'
,'France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Greece','Guatemala','Guyana','Hong Kong'
,'Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel'
,'Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Cambodia','Korea, Rep.','Kuwait','Lebanon','Liberia'
,'Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Macao','Morocco','Moldova','Madagascar'
,'Maldives','Mexico','Macedonia','Mali','Malta','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania'
,'Mauritius','Malawi','Malaysia','North America','Namibia','Niger','Nigeria','Nicaragua','Netherlands'
,'Norway','Nepal','New Zealand   ','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea'
,'Poland','Puerto Rico','Portugal','Paraguay','Qatar','Romania','Russian Federation','Rwanda','Saudi Arabia'
,'Sudan','Senegal','Singapore','Solomon Islands','Sierra Leone','El Salvador','Somalia','Serbia','Slovenia'
,'Sweden','Swaziland','Syrian Arab Republic','Chad','Togo','Thailand','Tajikistan','Turkmenistan','Timor-Leste'
,'Trinidad and Tobago','Tunisia','Turkey','Tanzania','Uganda','Ukraine','Uruguay','United States','Uzbekistan'
,'Venezuela, RB','Vietnam','Yemen, Rep.','South Africa','Congo, Dem. Rep.','Zambia','Zimbabwe'
]

country_clean = country[country['Country Name'].isin(country_list)]


external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]


external_stylesheets = [
    'https://raw.githubusercontent.com/biolchen/dataScience/master/css/dash.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]



app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)



np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)


# a scatter plot
trace1 = go.Scatter(x = random_x, y=random_y, mode='markers',
                                    marker = {
                                            'size':12,
                                            'color':'rgb(51,204,153)',
                                            'symbol':'pentagon',
                                            'line':{'width':2}
                                            }
                                         )

layout1 = go.Layout(autosize= True,
            title='My Scatterplot', 
            xaxis= {
                    'title': 'Pop',
                    'ticklen': 5,
                    'zeroline': False,
                    'gridwidth': 2})

layout1 = go.Layout(
    autosize= False,
    title= 'Scatter plot of unemployment rates in 2010',
    hovermode= 'closest',
     xaxis= dict(
         title= 'Pop',
         ticklen= 5,
         zeroline= False,
         gridwidth= 2,
     ),
    yaxis=dict(
        title= 'Unemployment Rate',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False,
    margin=dict(t=50)
)



# a bubble plot
trace2 = go.Scatter(
                        y = country_clean['2010'].values,
                        mode='markers',
                        marker=dict(
                            size= country_clean['2010'].values,
                            #color = np.random.randn(500), #set color equal to a variable
                            color = country_clean['2010'].values,
                            colorscale='Portland',
                            showscale=True
                        ),
                        text = country_clean['Country Name'].values
)

layout2 = go.Layout(
    autosize= False,
    title= 'Scatter plot of unemployment rates in 2010',
    hovermode= 'closest',
     xaxis= dict(
         title= 'Pop',
         ticklen= 5,
         zeroline= False,
         gridwidth= 2,
     ),
    yaxis=dict(
        title= 'Unemployment Rate',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False,
    margin=dict(t=50)
)



app.layout = html.Div(children = [
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g1', figure = {'data': [trace1], 'layout':layout1})
        ], className = 'five.columns'),
        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure = {'data': [trace2], 'layout':layout2})
        ], className = 'five.columns'),
    ],className="five.columns",style={'padding': 50})
])


if __name__ == '__main__':
    app.run_server(debug=True)
