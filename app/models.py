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
    species = db.Column(db.Integer, db.ForeignKey("species.id"), nullable=False) #Come back to foreign key
    bio = db.Column(db.String(1000))
    faction = db.Column(db.Boolean, default=False)
    credits = db.Column(db.Integer, nullable=False)
    user_image = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Integer)


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Species(db.Model):
    __tablename__ = "species"
    id = db.Column(db.Integer, primary_key=True)
    species_type = db.Column(db.String(50), nullable=False)


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
    cargo = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.Integer, nullable=False)
    cost_credits = db.Column(db.Integer, nullable=False)
    ship_image = db.Column(db.Integer, nullable=False)
    unique = db.Column(db.Boolean, default=False) 

