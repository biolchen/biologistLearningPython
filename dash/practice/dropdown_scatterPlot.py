import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('dash/gapminder-FiveYearData.csv')


app = dash.Dash(__name__)

year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})



app.layout = html.Div([
    dcc.Graph(id='Graph'),
    dcc.Dropdown(id='year-picker', options=year_options,
                value=df['year'].min())
], style={'padding': 30})

@app.callback(Output('Graph','figure'),
    [Input('year-picker', 'value')]
)
def update_figures(selected_year):

    filtered_df = df[df['year']==selected_year]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            name=continent_name
        ))
    return {'data':traces, 'layout': go.Layout(title='My plot',xaxis={'title':'GDP per Cap',
    'type':'log'}, yaxis={'title':'Life expectancy'})}

if __name__ == '__main__':
    app.run_server(debug=True)