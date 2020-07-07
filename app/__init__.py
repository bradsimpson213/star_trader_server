from flask import Flask, render_template
from flask_cors import CORS
from .config import Config
from .models import db
from .routes import users, ships, transactions
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

app.register_blueprint(users.bp)
app.register_blueprint(ships.bp)
app.register_blueprint(transactions.bp)

db.init_app(app)
migrate = Migrate(app, db)



# @app.route("/")
# def home():
#     return render_template("main_page.html")
