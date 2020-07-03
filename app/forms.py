from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, RadioField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class CreateUser(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    species = SelectField("Species", choices=[("Human", 'Human'), ("Not Human", "Not Human")]) # need to updated choices to species table
    bio = TextAreaField("Bio")
    faction = RadioField("Faction", choices=[(True, "Rebel Allaince"), (False, "Galatic Empire")], [DataRequired()])
    user_image = StringField("Image", [DataRequired()])
    submit = SubmitField("Create User")


class ListShip(FlaskForm):
    custom_name = StringField("Custom Ship Name")
    ship_type = SelectField("Ship Type", choices=[], [DataRequired()])
    sale_price = IntegerField("Sale Price", [DataRequired()])
    lightyears = IntegerField("Lightyears Traveled", [DataRequired()])
    submit = SubmitField("Create Ship") 
