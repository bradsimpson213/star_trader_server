from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, RadioField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

    # def to_dict(self):
    # return {"id": self.id, "email": self.email}


class CreateUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    species = SelectField("Species", choices=[("Human", 'Human'), ("Not Human", "Not Human")], validators=[DataRequired()]) # need to updated choices to species table
    bio = TextAreaField("Bio")
    faction = RadioField("Faction", choices=[(True, "Rebel Allaince"), (False, "Galatic Empire")], validators=[DataRequired()])
    user_image = StringField("Image", validators=[DataRequired()])
    submit = SubmitField("Create User")


class ListShip(FlaskForm):
    custom_name = StringField("Custom Ship Name")
    ship_type = SelectField("Ship Type", choices=[("Unique", "Unique"), ("Not Unique", "Not Unique")], validators=[DataRequired()])
    sale_price = IntegerField("Sale Price", validators=[DataRequired()])
    lightyears = IntegerField("Lightyears Traveled", validators=[DataRequired()])
    submit = SubmitField("Create Ship") 
