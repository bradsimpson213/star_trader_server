from flask import Flask, render_template # NOQA
from .config import Config
from .models import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def home():
    return render_template("main_page.html")
