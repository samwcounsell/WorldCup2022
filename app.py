from dash import Dash, dcc, html, Input, Output, callback
from app_pages import home, nation, player
import dash_bootstrap_components as dbc

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Updating app when user selects specific page
@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/player':
        return player.layout
    elif pathname == '/nation':
        return nation.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
