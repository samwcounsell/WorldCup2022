import dash_html_components as html
from app_functions.navigation import create_navigation

nav = create_navigation()

header = html.H3('Welcome to Python World Cup 2022 Dash App!')

def create_page_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout