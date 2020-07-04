from flask import Blueprint, render_template
from .models import db, Starship


bp = Blueprint("ships", __name__, url_prefix="")