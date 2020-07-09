from ..models import db
# from ..models.starships import Starship
# from ..models.users import User


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.Integer, db.ForeignKey("users.id"))
    seller = db.Column(db.Integer, db.ForeignKey("users.id"))
    starship = db.Column(db.Integer, db.ForeignKey("starships.id"))
    sale_price = db.Column(db.BigInteger, nullable=False)
    sale_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {"id": self.id, "buyer": self.buyer, "seller": self.seller, "starship": self.starship,
                "sale_price": self.sale_price, "sale_date": self.sale_date}
