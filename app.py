from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pandas as pd
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhfdkjhgjkdfhgkjdfhg'
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

soccer = pd.read_csv('data/fifa_soccer_players.csv')

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
            html.Li([
                dbc.NavItem(dbc.NavLink("Home", href="/", external_link=True, style={'color': 'white'}))
            ])
        ], className="nav navbar-nav")
            , className="navbar-collapse collapse")
    ])])

dash_app.layout = html.Div(children=[
    navbar,
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

])


@app.route("/", methods=['GET', 'POST'])
def test_bootstrap():
    return render_template("home.html")


@app.route("/dash", methods=['GET', 'POST'])
def dash_endpoint():
    return dash_app.index()
