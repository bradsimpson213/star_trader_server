from flask import Blueprint, request
from ..models import db
from ..models.starships import Starship
from ..models.shiptypes import Shiptype 
from ..auth import require_auth
import datetime

bp = Blueprint("ships", __name__, url_prefix="/ships")


# GET ALL SHIP TYPES
@bp.route("/types")
def get_types():
    ship_types = Shiptype.query.all()
    ship_types = [ship_type.to_dict() for ship_type in ship_types]
    return {"ship_types": ship_types}


# GET ALL STARSHIPS
@bp.route("/all")
def get_starships():
    starships = Starship.query.all()
    starships_return = []
    for starship in starships:
        dict_ship_type = starship.starship_type.to_dict()
        dict_user = starship.user.to_dict()
        starship = starship.to_dict()
        starship["starship_type"] = dict_ship_type
        starship["user"] = dict_user
        starships_return.append(starship)
    return { "star_ships": starships_return }


# GET UNIQUE SHIPS
@bp.route("/uniques")
def get_unique_ships():
    starships = Starship.query.all()
    starships_return = []
    for starship in starships:
        ship_type = starship.starship_type
        if ship_type.unique == True:
            dict_ship_type = ship_type.to_dict()
            dict_user = starship.user.to_dict()
            starship = starship.to_dict()
            starship["starship_type"] = dict_ship_type
            starship["user"] = dict_user
            starships_return.append(starship)
    return { "star_ships": starships_return }


# GET SHIPS BY CLASS
@bp.route("/class/<string:shipclass>")
def get_ships_by_class(shipclass):
    starships = Starship.query.all()
    starships_return = []
    for starship in starships:
        ship_type = starship.starship_type
        if ship_type.starship_class == shipclass:
            dict_ship_type = ship_type.to_dict()
            dict_user = starship.user.to_dict()
            starship = starship.to_dict()
            starship["starship_type"] = dict_ship_type
            starship["user"] = dict_user
            starships_return.append(starship)
    return {"star_ships": starships_return}


# GET STARSHIP BY ID
@bp.route("/<int:shipId>")
def get_one_starship(shipId):
    starship = Starship.query.get(shipId)
    dict_ship_type = starship.starship_type.to_dict()
    dict_user = starship.user.to_dict()
    starship = starship.to_dict()
    starship["starship_type"] = dict_ship_type
    starship["user"] = dict_user
    return {"star_ship": starship}


# GET STARTSHIP BY USER ID
@bp.route("/user/<int:userId>")
def get_ship_by_user(userId):
    starships = Starship.query.filter(Starship.owner==userId).all()
    starships_return = []
    for starship in starships:
        dict_ship_type = starship.starship_type.to_dict()
        starship = starship.to_dict()
        starship["starship_type"] = dict_ship_type
        starships_return.append(starship)
    return {"star_ships": starships_return}


# CREATE NEW SHIP ROUTE
@bp.route("/create", methods=["POST"])
@require_auth
def creat_ship():
    data = request.json
    print(data)
    try:
        starship = Starship(ship_type=data['ship_type'], 
                            custom_name=data['custom_name'], 
                            sale_price=data['sale_price'], 
                            lightyears_traveled=data['lightyears_traveled'], 
                            owner=data['owner'], 
                            for_sale=data['for_sale'],
                            seller_comment=data['seller_comment'], 
                            post_date=datetime.datetime.now())
        db.session.add(starship)
        db.session.commit()
        return {"starship": starship.to_dict()}, 200
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


# UPDATE SHIP ROUTE
@bp.route("/update/<int:shipId>", methods=["PUT"])
@require_auth
def update_user(shipId):
    data = request.json
    starship = Starship.query.get(shipId)

    if starship:
        starship.custom_name = data['custom_name']
        starship.sale_price = data['sale_price']
        starship.lightyears_traveled = data['lightyears_traveled']
        starship.owner = data['owner']
        starship.for_sale = data['for_sale']
        starship.seller_comment = data['seller_comment']
        starship.post_date = datetime.datetime.now()
        db.session.commit()
        return {"message": f"Starship {shipId} was updated!"}
    else:
        return {"error": "Starship Not Found"}, 401


# DELETE SHIP ROUTE
@bp.route("/delete/<int:shipId>", methods=["DELETE"])
@require_auth
def delete_user(shipId):
    starship = Starship.query.get(shipId)

    if starship:
        db.session.delete(starship)
        db.session.commit()
        return {"message": f"Starship {shipId} was deleted!"}
    else:
        return {"error": "User Not Found"}, 401
