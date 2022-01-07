import dash_html_components as html
from app_functions.navigation import create_navigation

nav = create_navigation()

header = html.H3('Complete Nation Data for the World Cup!')

def create_page_nation():
    layout = html.Div([
        nav,
        header,
    ])
    return layout