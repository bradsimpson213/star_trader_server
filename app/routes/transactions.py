from flask import Blueprint, request
from sqlalchemy import or_
from ..models import db
from ..models.transactions import Transaction
from ..models.users import User
from ..models.starships import Starship
from ..auth import require_auth
import datetime

bp = Blueprint("transactions", __name__, url_prefix="/transactions")


# SELL SHIP TRANSACTION ROUTE
@bp.route("", methods=["POST"])
@require_auth
def ship_transaction():
    data = request.json
    ship_sold = data['starship']
    ship_buyer = data['buyer']
    ship_seller = data['seller']
    ship_price = data['sale_price']

    buyer_ship = User.query.get(ship_buyer)
    seller_ship = User.query.get(ship_seller)
    sold_ship = Starship.query.get(ship_sold)

    if buyer_ship.credits >= ship_price:
        try:
            transaction = Transaction(buyer=ship_buyer, seller=ship_seller, starship=ship_sold,
                                    sale_price=ship_price, sale_date=datetime.datetime.now())
            db.session.add(transaction)
            buyer_ship.credits -= ship_price
            buyer_ship.force_points += 1
            seller_ship.credits += ship_price
            seller_ship.force_points += 1
            sold_ship.owner = buyer_ship.id
            sold_ship.for_sale = False
            db.session.commit()
            return {"transaction": transaction.to_dict()}, 200
        except AssertionError as message:
            print(str(message))
            return jsonify({"error": str(message)}), 400
    else:
        return {"error": "Buyer does not have enough credits to buy Starship"}


# TRANSACTIONS BY USER
@bp.route("/user/<int:userId>")
@require_auth
def transactions_by_user(userId):
    transactions = Transaction.query.filter(or_(Transaction.buyer == userId, Transaction.seller == userId)).all()
    dict_transactions = [transaction.to_dict() for transaction in transactions]
    return {'transactions': dict_transactions }


# TRANSACTIONS BY SHIP
@bp.route("/ship/<int:shipId>")
@require_auth
def transactions_by_ship(shipId):
    transactions = Transaction.query.filter(Transaction.starship == shipId).all()
    dict_transactions = [transaction.to_dict() for transaction in transactions]
    return {'transactions': dict_transactions}
