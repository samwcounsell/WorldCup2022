import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from navigation import create_navigation
import plotly.graph_objects as go
import numpy as np

nav = create_navigation()


# Making the graphs for nation
# TODO: Move to another file later

data = pd.read_csv("app_data/complete_nation_data.csv")

stacked_figures = ['AFCstack', 'CAFstack', 'CONCstack', 'CONMstack', 'OFCstack', 'UEFAstack']
conf = ['AFC', 'CAF', 'CONCACAF', 'CONMEBOL', 'OFC', 'UEFA']

for i in range(len(conf)):

    stacked_figures[i] = go.Figure(
        data=[
            go.Bar(
                name="Group Stages",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCGS"],
                offsetgroup=0,
                marker_color='dimgray',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCGS"]
            ),
            go.Bar(
                name="RO16",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR16"],
                offsetgroup=0,
                base=data.loc[data['Confederation'] == conf[i]]["WCGS"],
                marker_color='darkblue',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCR16"]
            ),
            go.Bar(
                name="QF",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR8"],
                offsetgroup=0,
                base=[val1 + val2 for val1, val2 in zip(data.loc[data['Confederation'] == conf[i]]["WCGS"], data.loc[data['Confederation'] == conf[i]]["WCR16"])],
                marker_color = 'mediumblue',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCR8"]
            ),
            go.Bar(
                name="SF",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR4"],
                offsetgroup=0,
                base=[val1 + val2 + val3 for val1, val2, val3 in zip(data.loc[data['Confederation'] == conf[i]]["WCGS"],
                                                        data.loc[data['Confederation'] == conf[i]]["WCR16"], data.loc[data['Confederation'] == conf[i]]["WCR8"])],
                marker_color = 'skyblue',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCR4"]
            ),
            go.Bar(
                name="Finals",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCF"],
                offsetgroup=0,
                base=[val1 + val2 + val3 + val4 for val1, val2, val3, val4 in zip(data.loc[data['Confederation'] == conf[i]]["WCGS"],
                                                                     data.loc[data['Confederation'] == conf[i]][
                                                                         "WCR16"],
                                                                     data.loc[data['Confederation'] == conf[i]][
                                                                         "WCR8"], data.loc[data['Confederation'] == conf[i]]["WCR4"])],
                marker_color='lightskyblue',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCF"]
            ),
            go.Bar(
                name="Wins",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WC_Wins"],
                offsetgroup=0,
                base=[val1 + val2 + val3 + val4 + val5 for val1, val2, val3, val4, val5 in
                      zip(data.loc[data['Confederation'] == conf[i]]["WCGS"],
                          data.loc[data['Confederation'] == conf[i]][
                              "WCR16"],
                          data.loc[data['Confederation'] == conf[i]][
                              "WCR8"], data.loc[data['Confederation'] == conf[i]]["WCR4"], data.loc[data['Confederation'] == conf[i]]["WCF"])],
                marker_color='gold',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WC_Wins"]
            )
        ],
        layout=go.Layout(
            yaxis_title="Stage Appearances",
            font=dict(
                size=12,
            )
        )
    )


layout = html.Div([
    nav,
    dbc.Row(
        dcc.Graph(figure = stacked_figures[0], style = {'width': '100%', 'height': 500})
            ),
    dbc.Row(
        dcc.Graph(figure = stacked_figures[1], style = {'width': '100%', 'height': 500})
            ),
    dbc.Row(
        dcc.Graph(figure = stacked_figures[2], style = {'width': '100%', 'height': 500})
            ),
    dbc.Row(
        dcc.Graph(figure = stacked_figures[3], style = {'width': '100%', 'height': 500})
            ),
    dbc.Row(
        dcc.Graph(figure = stacked_figures[4], style = {'width': '100%', 'height': 500})
            ),
    dbc.Row(
        dcc.Graph(figure = stacked_figures[5], style = {'width': '100%', 'height': 500})
            ),
])
