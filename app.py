import os
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from flask import render_template, request
from flask_bootstrap import Bootstrap
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
import greta_dash.fig as fig
import greta_dash.navbar as navbar

from db.config import Config, logger_config, DATABASE_PATH
from db.extensions import db
from db.models.user import User
from db.models.animal_data import AnimalData
from logging.config import dictConfig

dictConfig(logger_config)

app = Flask(__name__)
bootstrap = Bootstrap(app)
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/greta_dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
dash_app.layout = html.Div(children=[navbar, dcc.Graph(id='example-graph', figure=fig)])
app.config.from_object(Config)
app.logger.error(f"database location: {DATABASE_PATH}")
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def test_bootstrap():
    return render_template("home.html")


@app.route("/dash", methods=['GET', 'POST'])
def dash_endpoint():
    return dash_app.index()


class AnimalDataForm(FlaskForm):
    audio_file = FileField("Fichier audio")
    animal_name = StringField("Indiquer l'animal", validators=[DataRequired()])
    submit = SubmitField("Envoyer")


@app.route("/animals_data_collector", methods=['GET', 'POST'])
def animals_data_collector():
    form = AnimalDataForm()
    if form.validate_on_submit():
        uploaded_file = form.audio_file.data
        filename = uploaded_file.filename
        if filename != '':
            uploaded_file.save(os.path.join("data", filename))
            animal_name = form.animal_name.data
            animal_data = AnimalData(file=filename, animal=animal_name)
            db.session.add(animal_data)
            db.session.commit()
    rows = db.session.query(AnimalData).all()
    return render_template("animal_collector.html", form=form, rows=rows)


@app.route("/user", methods=['POST'])
def user_creation():
    username = request.args["username"]
    email = request.args["email"]
    password = request.args["password"]
    user = User(username=username, email=email, password=password)
    app.logger.info(f"Utilisateur créé: {username} {email} {password} ")
    db.session.add(user)
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['PUT'])
def user_update(username):
    email = request.args["email"]
    password = request.args["password"]
    app.logger.info(f"Utilisateur mis à jour: {username} ({email}, {password})")
    db.session.query(User).filter(User.username == username).update(
        {"email": email, "password": password}, synchronize_session="fetch"
    )
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['DELETE'])
def user_delete(username):
    app.logger.info(f"Utilisateur supprimé: {username}")
    user = User.get_by_username(username)
    db.session.delete(user)
    db.session.commit()
    return "ok"


@app.route("/user/<username>", methods=['GET'])
def user_get(username):
    app.logger.info(f"Utilisateur récupéré: {username}")
    user = User.get_by_username(username)
    return repr(user)


@app.route("/users", methods=['GET'])
def user_search():
    query = request.args["query"]
    users = db.session.query(User).filter(User.email.like(f'%{query}%'))
    return users
