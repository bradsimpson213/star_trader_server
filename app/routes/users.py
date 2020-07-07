from flask import Blueprint, request
import jwt
from flask_login import login_required

from ..config import Config
from ..models import db, User 
from ..forms import LoginForm, CreateUser


bp = Blueprint("users", __name__, url_prefix="/users")

# LOGIN WITH WTFORMS
 
# @bp.route("/login", methods=['GET', 'POST'])
# def user_login():
#     form = LoginForm()
#     print(request.method)
#     if request.method == 'GET':
#         return ('', {'csrf_token': form.csrf_token._value()})
#     elif form.validate_on_submit():
#         return {'message': 'Login successful'}, 200
#     else:
#         return {'errors': form.errors}

# LOGIN NOT USING WTFORMS

@bp.route("/login", methods=["POST"])
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


# CREATE USER WITH WTFORMS

@bp.route("/create", methods=['GET', 'POST'])
def user_create():
    form = CreateUser()
    print(request.method)
    if request.method == 'GET':
        return ('', {'csrf_token': form.csrf_token._value()})
    elif form.validate_on_submit():

        return {'message': 'User Created Successful'}, 200
    else:
        return {'errors': form.errors}




