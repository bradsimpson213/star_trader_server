from flask import Blueprint, render_template
from ..models import db, Starship, Shiptype 
from ..auth import require_auth

bp = Blueprint("ships", __name__, url_prefix="/ships")

@bp.route("/types")
def get_types():
    ship_types = Shiptype.query.all()
    ship_types = [ship_type.to_dict() for ship_type in ship_types]
    return {"ship_types": ship_types}
