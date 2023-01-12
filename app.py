from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pandas as pd
from dash import Dash, dcc, html

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhfdkjhgjkdfhgkjdfhg'
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')


dash_app.layout = html.Div(children=[
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
