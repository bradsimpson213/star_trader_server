from ..models import db


class Shiptype(db.Model):
    __tablename__ = "shiptypes"

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False)
    starship_class = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    hyperdrive_rating = db.Column(db.Float(), nullable=False)
    mglt = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passenger = db.Column(db.Integer, nullable=False)
    cargo = db.Column(db.BigInteger, nullable=False)
    consumables = db.Column(db.String(30), nullable=False)
    cost_credits = db.Column(db.BigInteger, nullable=False)
    ship_image = db.Column(db.String(150), nullable=False)
    unique = db.Column(db.Boolean, default=False)

    ship = db.relationship("Starship", back_populates="starship_type")

    def to_dict(self):
        return {"id": self.id, "type_name": self.type_name, "starship_class": self.starship_class, "manufacturer": self.manufacturer,
                "model": self.model, "hyperdrive_rating": self.hyperdrive_rating, "mglt": self.mglt, "length": self.length,
                "crew": self.crew, "passenger": self.passenger, "cargo": self.cargo, "consumables": self.consumables,
                "cost_credits": self.cost_credits, "ship_image": self.ship_image, "unique": self.unique}
