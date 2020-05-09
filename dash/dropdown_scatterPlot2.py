import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from numpy import random

df = pd.read_csv('dash/mpg.csv')
df['year'] = random.randint(-4,5,len(df))*0.05+df['model_year']

app = dash.Dash(__name__)

trace = go.Scatter(x=df['year'] + 1900, 
                   y=df['mpg'], 
                   text = df['name'],
                   hovertemplate='model: %{text}<br>'+ 'mpg: %{y}<br>'+'year: %{x}<br>'+'<extra></extra>',
                   mode='markers')

layout = go.Layout(title='MPG Data', 
                    xaxis={'title':'Model Year'},
                    yaxis={'title': 'MPG'},
                    hovermode='closest')



trace2 = go.Scatter(x=[0,1], 
                   y=[0,1], 
                   mode='lines')

layout2 = go.Layout(title='acceleration',
                    margin={'l':0}
                    )

app.layout = html.Div([
    html.Div([
    dcc.Graph(id='mpg-scatter1', figure={'data': [trace], 'layout':layout}),
    ],style={'padding': 30, 'width':'50%','display':'inline-block'}),
    html.Div([dcc.Graph(id='mpg-line', figure={'data': [trace2], 'layout':layout2})],
    style={'width':'20%','height':'50%','display':'inline-block'}),
    html.Div([
        dcc.Markdown(id='mpg_stats')], 
                style={'width':'20%', 'height':'50%','display':'inline-block'})
                        ])



@app.callback(Output('mpg-line','figure'), 
            [Input('mpg-scatter1', 'hoverData')]
)
def callback_graph(hoverData):
    v_index = hoverData['points'][0]
    figure = {
        'data':[go.Scatter(x=[0,1],
                            y=[0,60/df.iloc[v_index]['acceleration']],
                            mode='lines'
                            )],
        'layout': go.Layout(title=df.iloc[v_index]['name'],
                                margin = {'l':0},
                                height=300
        )}
    return figure

@app.callback(Output('mpg_stats', 'children'),
               [Input('mpg-scatter1', 'hoverData')])
def callback_stats(hoverData):
    #v_index = hoverData['points'][0]['pointsIndex']
    stat = hoverData
    return stat

if __name__ == '__main__':
    app.run_server(debug=True)