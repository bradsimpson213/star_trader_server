from flask import Blueprint, request
from ..models import db, Starship, Shiptype 
from ..auth import require_auth
import datetime

bp = Blueprint("ships", __name__, url_prefix="/ships")


@bp.route("/types")
def get_types():
    ship_types = Shiptype.query.all()
    ship_types = [ship_type.to_dict() for ship_type in ship_types]
    return {"ship_types": ship_types}


@bp.route("/all")
def get_starships():
    starships = Starship.query.all()
    starships = [starship.to_dict() for starship in starships]
    return {"star_ships": starships}


@bp.route("/<int:shipId>")
def get_one_starship(shipId):
    starship = Starship.query.get(shipId)
    starship = starship.to_dict()
    return {"star_ship": starship}


# @bp.route("/create", methods="POST")
# @require_auth
# def creat_ship():
#     data = request.json
#     print(data.body)
#     {'id': , 'ship_type': , 'custom_name': , 'sale_price': , 'lightyears_traveled': , 'owner': ,
#         'for_sale': , 'seller_comment': , 'post_date': datetime.datetime.now()}
