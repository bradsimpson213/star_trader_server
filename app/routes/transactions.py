from flask import Blueprint, render_template
from ..models import db, Transaction
from ..auth import require_auth

bp = Blueprint("transactions", __name__, url_prefix="/ships")