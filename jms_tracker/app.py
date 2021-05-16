from flask import Blueprint, render_template
from flask_login import  current_user, login_required
from . import db

app = Blueprint("app", __name__)


@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/profile")
# def profile():
#     return render_template('profile.html')


@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
