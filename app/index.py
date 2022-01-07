import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app_pages.home import create_page_home
from app_pages.nation import create_page_nation
from app_pages.player import create_page_player
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/nation':
        return create_page_nation()
    if pathname == '/player':
        return create_page_player()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)