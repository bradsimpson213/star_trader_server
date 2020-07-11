from ..models import db
# from ..models.shiptypes import Shiptype
# from ..models.users import User

class Starship(db.Model):
    __tablename__ = "starships"

    id = db.Column(db.Integer, primary_key=True)
    ship_type = db.Column(db.Integer, db.ForeignKey("shiptypes.id"), nullable=False)
    custom_name = db.Column(db.String(75),)
    sale_price = db.Column(db.BigInteger, nullable=False)
    lightyears_traveled = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
    for_sale = db.Column(db.Boolean, default=True)
    seller_comment = db.Column(db.String(250), nullable=True)
    post_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="starships")
    starship_type = db.relationship("Shiptype", back_populates="ship")
    transaction = db.relationship(
        "Transaction", back_populates="ship", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "ship_type": self.ship_type, "custom_name": self.custom_name, "sale_price": self.sale_price,
                "lightyears_traveled": self.lightyears_traveled, "owner": self.owner, "for_sale": self.for_sale, "seller_comment": self.seller_comment,
                "post_date": self.post_date, "user": {}, "starship_type": {}}
