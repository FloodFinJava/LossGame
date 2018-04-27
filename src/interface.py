# -*- coding: utf-8 -*-

import toml
# dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# local import
import game

CONF_FILE = "conf.toml"

# Load configuration data from the toml file as a dict
with open(CONF_FILE, 'r') as toml_file:
    toml_string = toml_file.read()
conf = toml.loads(toml_string)


app = dash.Dash()

# Supposedly to prevent errors
app.scripts.config.serve_locally=True

# Plot layout
# ~ example_plot = {
    # ~ 'data': [
        # ~ {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        # ~ {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    # ~ ],
    # ~ 'layout': {
        # ~ 'title': 'Dash Data Visualization'
    # ~ }
# ~ }

# Default map
map_data = [{'type': 'scattermapbox',
            'lat':[],
            'lon': [],
           }]

map_layout = {'autosize': True,
              'overmode': 'closest',
              'mapbox': {'accesstoken': conf['map']['mapbox_token'],
                         'bearing': conf['map']['bearing'],
                         'center': conf['map']['center'],
                         'pitch': conf['map']['pitch'],
                         'zoom': conf['map']['zoom']
                         },
              'title': conf['map']['title'],
              "height": conf['map']['height']
             }

app.layout = html.Div(children=[
    html.H1(children=conf['app']['title']),

    html.Div(children=conf['app']['descr']),

    # Example plot
    # ~ dcc.Graph(id='example-graph', figure=example_plot),

    # input number of points
    dcc.Input(id='input-npoints', value='number of points', type='integer'),
    html.Button('Submit', id='submit-button'),
    # Map
    dcc.Graph(id='main-map', figure={'data': map_data, 'layout': map_layout})
])


@app.callback(Output('main-map', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-npoints', 'value')]
             )
def update_map(n_clicks, n_points):
    """Draw the map
    """

    points_lat, points_lon = game.distribute_inhabited_points(conf['zone']['extent'],
                                                              int(n_points))

    map_data = [{'type': 'scattermapbox',
                'lat': points_lat,
                'lon': points_lon,
                'mode': 'markers',
                'marker': {'size': 8},
                # ~ 'text': ['Semarang']
               }]

    map_layout = {'autosize': True,
                  'overmode': 'closest',
                  'mapbox': {'accesstoken': conf['map']['mapbox_token'],
                             'bearing': conf['map']['bearing'],
                             'center': conf['map']['center'],
                             'pitch': conf['map']['pitch'],
                             'zoom': conf['map']['zoom']
                             },
                  'title': conf['map']['title'],
                  "height": conf['map']['height']
                 }

    return {'data': map_data, 'layout': map_layout}

if __name__ == '__main__':
    app.run_server(debug=True)
