from flask import Blueprint
import jwt
from flask_login import login_required

from ..config import Config
from ..models import db, User 
from ..forms import LoginForm, CreateUser


bp = Blueprint("users", __name__, url_prefix="")


@bp.route("/login", methods=["GET"])
def user_login_form();
    form = LoginForm
    return { "form": form.to_dict() }


@bp.route("/login" methods=["POST"])
def user_login():
    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"error": "Email not found"}, 422

    if user.check_password(data['password']):
        access_token = jwt.encode({'email': user.email}, Config.SECRET_KEY)
        return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    else: 
        return {"error": "Incorrect password"}, 401


# @bp.route("/add", methods=['GET', 'POST'])
# def creat_user():
#     form = CreateUser()
#     return "<h1> Create a new user Rebel Scum!</h1>"
