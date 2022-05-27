from dash import dcc, html
import plotly.express as px
import pandas as pd
from app_features.navigation import create_navigation

nav = create_navigation()

data = pd.read_csv("app_data/complete_nation_data.csv")

world_fig = px.choropleth(data, locations="iso_alpha",
                          color="WCGS",
                          hover_name="Country",  # column to add to hover information
                          color_continuous_scale=px.colors.sequential.matter,
                          labels = {
                              'iso_alpha': 'ISO Alpha',
                              'WCGS': 'World Cups Reached'
                          }
                          )

layout = html.Div([
    nav,
    html.H1(
        children='Welcome to the Python World Cup Dashboard',
        style={'textAlign': 'center', 'padding': 30}
    ),
    html.Div(children='This multipage application allows you to explore all the data generated throughout your'
                      'World Cup simulations.',
             style={'textAlign': 'center', 'padding': 10}
             ),
    html.Div(children='Currently there are the following pages: Nation data, Player data.',
             style={'textAlign': 'center'}
             ),
    dcc.Graph(figure=world_fig, style={'height': 1000}),
    html.Div(children='Figure 1: Plot displaying number of World Cup group stage appearances by country',
             style={'textAlign': 'center'}
             ),
])
