from dash import html
import dash_bootstrap_components as dbc

LOGO = "https://gretaformation.ac-orleans-tours.fr/sites/all/themes/themes/adscom/images/logo.jpg"
navbar = dbc.Navbar(
    color="dark", dark=True,
    children=[dbc.Container([
        html.A(
            href="/", style={"textDecoration": "none"},
            children=dbc.Row(
                align="center", className="g-0",
                children=[
                    dbc.Col(html.Img(src=LOGO, height="36px")),
                ]),

        ),
        html.Div(html.Ul([
            html.Li(dbc.NavItem(dbc.NavLink("Home", href="/", external_link=True, style={'color': '#9d9d9d'}))),
            html.Li(dbc.NavItem(dbc.NavLink("Stats", active=True, href="/greta_dash", style={'color': 'white'})))
        ], className="nav navbar-nav")
            , className="navbar-collapse collapse")
    ])])
