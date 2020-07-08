from flask import Blueprint, request
import jwt
from flask_login import login_required

from ..config import Config
from ..models import db, User, Species 
# from ..forms import LoginForm, CreateUser


bp = Blueprint("users", __name__, url_prefix="/users")


# LOGIN ROUTE
@bp.route("/login", methods=["POST"])
def user_login():
    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return { "error": "Email not found" }, 422

    if user.check_password(data['password']):
        starships = user.starships
        dict_starships = [starship.to_dict() for starship in starships]
        user_dict = user.to_dict()
        user_dict["starships"] = dict_starships
        access_token = jwt.encode({'email': user.email}, Config.SECRET_KEY)
        return { "access_token": access_token.decode('UTF-8'), 'user': user_dict }
    else: 
        return { "error": "Incorrect password" }, 401


# GET SPECIES ROUTE
@bp.route("/species")
def get_species():
    species = Species.query.all()
    dict_species = [specie.to_dict() for specie in species]
    return { "species": dict_species }


# GET USER BY ID ROUTE
@bp.route("/<int:userId>")
def get_user_bt_id(userId):
    user = User.query.get(userId)
    starships = user.starships
    dict_starships = [starship.to_dict() for starship in starships]
    dict_species = user.species_info.to_dict()
    user_dict = user.to_dict()
    user_dict["starships"] = dict_starships
    user_dict["species_info"] = dict_species
    return { "user": user_dict }


# CREATE USER ROUTE
@bp.route("/create", methods=["POST"])    
def create_user():
    data = request.json
    rows = db.session.query(User).count() + 2  #not sure why this needs to be +2?
    print(rows)

    try: 
        user = User(id=rows, name=data['name'], email=data['email'], password=data['password'],
                    species=data['species'], bio=data['bio'], faction=data['faction'],
                    credits=150000, user_image=data['user_image'], force_points=0)
        db.session.add(user)
        db.session.commit()
        access_token = jwt.encode({'email': user.email}, Config.SECRET_KEY)
        return {"access_token": access_token.decode('UTF-8'), 'user': user.to_dict()}
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


# UPDATE USER ROUTE
@bp.route("/update/<int:userId>", methods=["PUT"])
def update_user(userId):
    data = request.json
    user = User.query.get(userId)
    if user:
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        user.species = data['species'] 
        user.bio = data['bio']
        user.faction = data['faction']
        user.credits = data['credits']
        user.user_image = data['user_image']
        user.force_points = data['force_points']
        db.session.commit()
        return {"message": f"User {userId} was updated!"}
    else:
        return {"error": "User Not Found"}, 401


# DELETE USER ROUTE
@bp.route("/delete/<int:userId>", methods=["DELETE"])
def delete_user(userId):
    user = User.query.get(userId)

    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message":f"User {userId} was deleted!" }
    else:
        return {"error": "User Not Found"}, 401


# CREATE USER WITH WTFORMS
# @bp.route("/create", methods=['GET', 'POST'])
# def user_create():
#     form = CreateUser()
#     print(request.method)
#     if request.method == 'GET':
#         return ('', {'csrf_token': form.csrf_token._value()})
#     elif form.validate_on_submit():

#         return {'message': 'User Created Successful'}, 200
#     else:
#         return {'errors': form.errors}

# LOGIN WITH WTFORMS
# @bp.route("/login", methods=['GET', 'POST'])
# def user_login():
#     form = LoginForm()
#     print(request.method)
#     if request.method == 'GET':
#         return ('', {'csrf_token': form.csrf_token._value()})
#     elif form.validate_on_submit():
#         data = request.json
#         user = User.query.filter(User.email == data['email']).first()
#         if not user:
#             return {"error": "Email not found"}, 422

#         if user.check_password(data['password']):
#             access_token = jwt.encode({'email': user.email}, Config.SECRET_KEY)
#             return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}, 200
#         else:
#             return {"error": "Incorrect password"}, 401
#     else:
#         return {'errors': form.errors}




