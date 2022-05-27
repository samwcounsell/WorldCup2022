import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
from app_features.navigation import create_navigation
import plotly.graph_objects as go
import plotly.express as px

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
                marker_color='maroon',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCGS"]
            ),
            go.Bar(
                name="RO16",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR16"],
                offsetgroup=0,
                base=data.loc[data['Confederation'] == conf[i]]["WCGS"],
                marker_color='firebrick',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCR16"]
            ),
            go.Bar(
                name="QF",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR8"],
                offsetgroup=0,
                base=[val1 + val2 for val1, val2 in zip(data.loc[data['Confederation'] == conf[i]]["WCGS"], data.loc[data['Confederation'] == conf[i]]["WCR16"])],
                marker_color = 'indianred',
                hovertext=data.loc[data['Confederation'] == conf[i]]["WCR8"]
            ),
            go.Bar(
                name="SF",
                x=data.loc[data['Confederation'] == conf[i]]["Country"],
                y=data.loc[data['Confederation'] == conf[i]]["WCR4"],
                offsetgroup=0,
                base=[val1 + val2 + val3 for val1, val2, val3 in zip(data.loc[data['Confederation'] == conf[i]]["WCGS"],
                                                        data.loc[data['Confederation'] == conf[i]]["WCR16"], data.loc[data['Confederation'] == conf[i]]["WCR8"])],
                marker_color = 'peru',
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
                marker_color='orange',
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
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(
                size=12,
            )
        )

    )

for i in range(len(stacked_figures)):
    stacked_figures[i].update_layout(title = conf[i],
                                     xaxis = dict(title = 'Country'),
                                     yaxis = dict(title = 'Combined Stage Appearances'))
    stacked_figures[i].update_xaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')
    stacked_figures[i].update_yaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')


conf_colours = ['peru', 'orange', 'maroon', 'gold', 'indianred', 'lightpink']

def_fig = px.scatter(data, x = 'Defense', y = 'CS%', trendline="ols", trendline_options=dict(log_x=True),
                     color = 'Confederation', color_discrete_sequence = conf_colours, hover_name='Country')

def_fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
def_fig.update_xaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')
def_fig.update_yaxes(showline=True, linewidth=2, linecolor='peru', gridcolor='peru')


layout = html.Div([
    nav,
    html.H1(
            children='Welcome to the Nation Data analysis',
            style={'textAlign': 'center', 'padding': 30}
        ),
    html.H3(
            children='Section 1',
            style={'textAlign': 'center', 'padding': 30}
        ),
    html.Div(children='The following plots show how often each country reached each World Cup stage, the graphs are'
                      ' split by Confederation.',
                 style={'textAlign': 'center', 'padding': 10}
        ),
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
    html.H3(
            children='Section 2',
            style={'textAlign': 'center', 'padding': 30}
        ),
    html.Div(children='Plots further below begin to become more analytical, investigating the effects of individual'
                      'parameters on results.',
                 style={'textAlign': 'center', 'padding': 10}
        ),
    dbc.Row(
        dcc.Graph(figure = def_fig, style = {'width': '100%', 'height': 500})
            ),
])
