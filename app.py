from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhfdkjhgjkdfhgkjdfhg'
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route("/", methods=['GET', 'POST'])
def test_bootstrap():
    return render_template("home.html")

