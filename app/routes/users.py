from flask import Blueprint
from flask_login import login_required
from ..models import db 
from ..forms import LoginForm, CreateUser


bp = Blueprint("users", __name__, url_prefix="")

@bp.route("/")
# @login_required
def user_login():
    return "<h1> Log in Rebel Scum! </h1>"
