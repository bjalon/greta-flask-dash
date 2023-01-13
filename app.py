from flask import Flask
from flask import render_template, request
from flask_bootstrap import Bootstrap
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
import greta_dash.fig as fig
import greta_dash.navbar as navbar

from db.config import Config
from db.extensions import db
from db.models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhfdkjhgjkdfhgkjdfhg'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/greta_dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
dash_app.layout = html.Div(children=[navbar, dcc.Graph(id='example-graph', figure=fig)])
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def test_bootstrap():
    return render_template("home.html")


@app.route("/dash", methods=['GET', 'POST'])
def dash_endpoint():
    return dash_app.index()


@app.route("/user", methods=['POST'])
def user_creation():
    username = request.args["username"]
    email = request.args["email"]
    password = request.args["password"]
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['PUT'])
def user_update(username):
    email = request.args["email"]
    password = request.args["password"]
    db.session.query(User).filter(User.username == username).update(
        {"email": email, "password": password}, synchronize_session="fetch"
    )
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['DELETE'])
def user_delete(username):
    user = User.get_by_username(username)
    db.session.delete(user)
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['GET'])
def user_get(username):
    user = User.get_by_username(username)
    return str(user)


@app.route("/users", methods=['GET'])
def user_search():
    query = request.args["query"]
    users = db.session.query(User).filter(User.email.like(f'%{query}%'))
    return users
