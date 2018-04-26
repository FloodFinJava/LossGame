# -*- coding: utf-8 -*-

import toml
# dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

CONF_FILE = "conf.toml"

# Load configuration data from the toml file as a dict
with open(CONF_FILE, 'r') as toml_file:
    toml_string = toml_file.read()
conf = toml.loads(toml_string)


app = dash.Dash()

# Supposedly to prevent errors
app.scripts.config.serve_locally=True

# Plot layout
example_plot = {
    'data': [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    ],
    'layout': {
        'title': 'Dash Data Visualization'
    }
}

# Map layout
map_data = [{'type': 'scattermapbox',
            'lat': [conf['map']['center']['lat']],
            'lon': [conf['map']['center']['lon']],
            # ~ 'mode': 'markers',
            # ~ 'marker': {'size': 8},
            'text': ['Semarang']
           }]

map_layout = {'autosize': True,
              'overmode': 'closest',
              'mapbox': {'accesstoken': conf['map']['mapbox_token'],
                         'bearing': 0,
                         'center': conf['map']['center'],
                         'pitch': 0,
                         'zoom': 9
                         },
              'title': conf['map']['title'],
              "height": 700
             }

map_figure = {'data': map_data,
              'layout': map_layout}

app.layout = html.Div(children=[
    html.H1(children=conf['app']['title']),

    html.Div(children=conf['app']['descr']),

    # Example plot
    # ~ dcc.Graph(id='example-graph', figure=example_plot),

    # Map
    dcc.Graph(id='main-map', figure=map_figure)
])

if __name__ == '__main__':
    app.run_server(debug=True)
