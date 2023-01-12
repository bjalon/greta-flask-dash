from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
import plotly.express as px
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
            html.Li(dbc.NavItem(dbc.NavLink("Home", href="/", external_link=True, style={'color': '#9d9d9d'}))),
            html.Li(dbc.NavItem(dbc.NavLink("Stats", active=True, href="/dash", style={'color': 'white'})))
        ], className="nav navbar-nav")
            , className="navbar-collapse collapse")
    ])])

data = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# fig = px.bar(data, x="Fruit", y="Amount", color="City", barmode="group")
fig = go.Figure()
fig.add_scatter(x=[1, 2, 3], y=[4, 2, 3])
fig.add_scatter(x=[1, 2, 3, 4], y=[4, 5, 2, 3])

dash_app.layout = html.Div(children=[
    navbar,
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


@app.route("/", methods=['GET', 'POST'])
def test_bootstrap():
    return render_template("home.html")


@app.route("/dash", methods=['GET', 'POST'])
def dash_endpoint():

    return dash_app.index()
