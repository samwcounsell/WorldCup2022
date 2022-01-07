import dash_bootstrap_components as dbc

def create_navigation():

    navigation = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Nation", href='/nation'),
                    dbc.DropdownMenuItem("Player", href='/player'),
                ],
            ),
        ],
        brand="Home",
        brand_href="/",
        sticky="top",
        color="dark",
        dark=True,
    )

    return navigation