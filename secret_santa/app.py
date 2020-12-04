from flask import Flask
from flask import render_template
from flask import request

from .forms import SecretSantaForm


def create_app():
    app = Flask(__name__)
    app.secret_key = 'hello'

    @app.route('/')
    def dashboard():
        form = SecretSantaForm(request.args)
        return render_template("dashboard.html.jinja2", form=form)

    return app
