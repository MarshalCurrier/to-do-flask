
from flask import Flask, Blueprint, redirect, render_template,request,session, url_for,jsonify
from flask_restx import Api, Namespace
from flask_sqlalchemy import SQLAlchemy
from swagger.extensions import *
from app_config import config,  environment

app = Flask(__name__)
app_config = config(environment)

app.register_blueprint(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = app_config.SQLALCHEMY_DATABASE_URI 
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