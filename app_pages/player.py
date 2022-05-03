from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import math

from navigation import create_navigation

nav = create_navigation()

data = pd.read_csv("app_data/complete_player_data.csv")

# TODO: Move this to post data function later
data['qualP'] = data['P'] - data['WC_P']
data['qualG'] = data['Goals'] - data['WC_Goals']
data['qualA'] = data['Assists'] - data['WC_Assists']

data['qualGPG'] = data['qualG'] / data['qualP']
data['qualAPG'] = data['qualA'] / data['qualP']

WC_G_A_data = data.loc[(data['WC_Goals'] > 0) | (data['WC_Assists'] > 0)]


# Making the graphs
conf_colours = ['dimgray', 'darkblue', 'deepskyblue', 'gold', 'violet', 'purple']

Q_GPGvAPG = px.scatter(data, x="qualAPG", y="qualGPG", color="Confederation", color_discrete_sequence=conf_colours,
                       hover_name='Name', size_max=60)
WC_GPGvAPG = px.scatter(WC_G_A_data, x="WC_APG", y="WC_GPG", color="Confederation",
                        color_discrete_sequence=conf_colours, hover_name='Name', size='WC_P', size_max=60)


layout = html.Div([
    nav,
    dbc.Row(
        dcc.Graph(figure=Q_GPGvAPG, style={'width': '100%', 'height': 1000})
    ),
    dbc.Row(
        dcc.Graph(id = "gva", style={'width': '100%', 'height': 1000})
    ),
    dbc.Row([
        dbc.Col(html.P("Minimum World Cup Games Played:"),
                ),
        dbc.Col(dcc.RangeSlider(id='range-slider',
                                min=0, max=1000, step=10,
                                marks={0: '0', 100: '100', 200: '200', 300: '300', 400: '400', 500: '500', 600: '600', 700: '700', 800: '800', 900: '900', 1000: '1000'},
                                value=[0, 1000], tooltip={"placement": "bottom", "always_visible": True}),
                ),
    ], style={"display": "grid", "grid-template-columns": "15% 75%"}),
])

@callback(
    Output("gva", "figure"),
    [Input("range-slider", "value")])
def update_bubble(slider_range):
    low, high = slider_range
    mask = (data['WC_P'] > low)
    gva = px.scatter(WC_G_A_data[mask], x="WC_APG", y="WC_GPG", color="Confederation",
                     color_discrete_sequence=conf_colours, hover_name='Name', size = 'WC_P', size_max = 50)

    return gva
