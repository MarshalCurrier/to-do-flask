
from flask import Flask, Blueprint, redirect, render_template,request,session, url_for,jsonify
from flask_restx import Api, Namespace
from flask_sqlalchemy import SQLAlchemy
from swagger.api_models import *
from swagger.extensions import *
from swagger.models import *
from swagger.resources import *

app = Flask(__name__)

# blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

# api = Api(
#     blueprint,
#     version="1.0",
#     title="Mini REST API",
#     description="A mini REST API",
# )
# ns = api.namespace("items", description="Item operations")
# api.add_namespace(ns)

app.register_blueprint(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres-to-do:strong-password@localhost:5432/to-do"  
api.add_namespace(ns)
db.init_app(app)

@app.route("/")
def home():
    page_title = "My Tasks"
    return render_template("index.html",
                           page_title = page_title)

@app.route("/login")
def login():
    page_title = "Sign Up/Login"
    return render_template("login.html",
                           page_title = page_title)


if __name__ == "__main__":
    app.run()