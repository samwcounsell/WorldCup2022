from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from navigation import create_navigation

nav = create_navigation()

header = html.H3('Welcome to Python World Cup 2022 Dash App!')

layout = html.Div([
        nav,
        header,
    ])

