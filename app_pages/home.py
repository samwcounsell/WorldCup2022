from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
from app_features.navigation import create_navigation

# Importing navbar
nav = create_navigation()

# Reading in nation data
data = pd.read_csv("app_data/complete_nation_data.csv")

# Page Layout
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
    dcc.Dropdown(id='stage_dropdown', options=[
            {'label': 'World Cup Group Stages', 'value': 'WCGS'},
            {'label': 'World Cup Round of 16', 'value': 'WCR16'},
            {'label': 'World Cup Quarter-Finals', 'value': 'WCR8'},
            {'label': 'World Cup Semi-Finals', 'value': 'WCR4'},
            {'label': 'World Cup Finals', 'value': 'WCF'},
            {'label': 'World Cup Wins', 'value': 'WC_Wins'}
    ],
            value = 'WCGS', style = {'width': 400, 'textAlign': 'center'}),
    dcc.Graph(id = 'world_map', style = {'width': '100%', 'height': 1000}),
    html.Div(children='Figure 1: Plot displaying number of World Cup stage appearances by country',
             style={'textAlign': 'center'})
])

# Callback for choropleth World Map
@callback(
    Output("world_map", "figure"),
    [Input("stage_dropdown", "value")])

# Function to create and update map depending on stage selected
def update_map(selected_value):

    world_map = px.choropleth(data, locations="iso_alpha",
                              color=selected_value,
                              hover_name="Country",  # column to add to hover information
                              color_continuous_scale=px.colors.sequential.matter,
                              labels={
                                  'iso_alpha': 'ISO Alpha ',
                                  'WCGS': 'World Cups Reached ',
                                  'WCR16': 'World Cups Round of 16 Reached ',
                                  'WCR8': 'World Cups Quarter-Finals Reached ',
                                  'WCR4': 'World Cups Semi-Finals Reached ',
                                  'WCF': 'World Cups Finals Reached ',
                                  'WC_Wins': 'World Cups Won ',
                              }
                              )

    return world_map