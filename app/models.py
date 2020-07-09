from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hashed_password = db.Column(db.String(100), nullable=False)
    species = db.Column(db.Integer, db.ForeignKey("species.id"), nullable=False) 
    bio = db.Column(db.String(1000))
    faction = db.Column(db.Boolean, default=False)
    credits = db.Column(db.BigInteger, nullable=False)
    user_image = db.Column(db.String(150), nullable=False)
    force_points = db.Column(db.Integer, default=0)
    
    starships = db.relationship("Starship", back_populates="user")
    species_info = db.relationship("Species", back_populates="user_info")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return { "id": self.id, "name": self.name, "email": self.email, "species": self.species, "bio": self.bio,
                "faction": self.faction, "credit": self.credits, "user_image": self.user_image, "force_points": self.force_points, "starships": {} }


class Species(db.Model):
    __tablename__ = "species"

    id = db.Column(db.Integer, primary_key=True)
    species_type = db.Column(db.String(75), nullable=False)

    user_info = db.relationship("User", back_populates="species_info")

    def to_dict(self):
        return { "id": self.id, "species_type": self.species_type }


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
        return { "id": self.id, "type_name": self.type_name, "starship_class": self.starship_class, "manufacturer": self.manufacturer,
                "model": self.model, "hyperdrive_rating": self.hyperdrive_rating, "mglt": self.mglt, "length": self.length,
                "crew": self.crew, "passenger": self.passenger, "cargo": self.cargo, "consumables": self.consumables, 
                "cost_credits": self.cost_credits, "ship_image": self.ship_image, "unique": self.unique }

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

    def to_dict(self):
        return { "id": self.id, "ship_type": self.ship_type, "custom_name": self.custom_name, "sale_price": self.sale_price,
                "lightyears_traveled": self.lightyears_traveled, "owner": self.owner, "for_sale": self.for_sale, "seller_comment": self.seller_comment, 
                "post_date": self.post_date, "user": {}, "starship_type": {} }

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True )
    buyer = db.Column(db.Integer, db.ForeignKey("users.id"))
    seller = db.Column(db.Integer, db.ForeignKey("users.id"))
    starship = db.Column(db.Integer, db.ForeignKey("starships.id"))
    sale_price = db.Column(db.BigInteger, nullable=False)
    sale_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return { "id": self.id, "buyer": self.buyer, "seller": self.seller, "starship": self.starship,
                 "sale_price": self.sale_price, "sale_date": self.sale_date }