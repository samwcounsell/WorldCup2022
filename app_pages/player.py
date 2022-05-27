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
conf_colours = ['peru', 'orange', 'maroon', 'gold', 'indianred', 'lightpink']

Q_GPGvAPG = px.scatter(data, x="qualAPG", y="qualGPG", color="Confederation", color_discrete_sequence=conf_colours,
                       hover_name='Name', size_max=60)
Q_GPGvAPG.update_layout(plot_bgcolor='rgba(0,0,0,0)')
Q_GPGvAPG.update_xaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')
Q_GPGvAPG.update_yaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')


layout = html.Div([
    nav,
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
    mask_index = mask[mask].index.to_list()
    gva = px.scatter(WC_G_A_data[WC_G_A_data.index.isin(mask_index)], x="WC_APG", y="WC_GPG", color="Confederation",
                     color_discrete_sequence=conf_colours, hover_name='Name', size = 'WC_P', size_max = 50)
    gva.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    gva.update_xaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')
    gva.update_yaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')

    return gva
