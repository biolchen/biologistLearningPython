import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


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
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
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


app.layout = html.Div([
    dcc.Input(id='my-id', value='Initial Text', type='text'),
    html.Div(id='my-div', style= {'border':'2px blue solid'})
], style={'padding': 30})

@app.callback(Output(component_id="my-div", component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)


def update_output_div(input_value):
    return "You entered: {}".format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)