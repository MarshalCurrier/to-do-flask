
from flask import Flask, Blueprint, redirect, render_template,request,session, url_for,jsonify
# from flask_restx import Api, Namespace
# from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from swagger.extensions import jwt
from jwt_custom_func.jwt_custom_funk import is_token_expired
# import jwt as jwt_auth
from functools import wraps
from swagger.extensions import *
from app_config import config,  environment
from app_config import get_brand_name, get_secret_key, JWT_EXPIRATION_MINUTES
import requests 
import datetime
from jwt_custom_func.jwt_custom_funk import validate_token, token_expire_countdown, authenticated_page, auth_wrapper

app = Flask(__name__)
app_config = config(environment)

app.register_blueprint(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = app_config.SQLALCHEMY_DATABASE_URI 
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = get_secret_key()
db.init_app(app)
jwt.init_app(app)
# db = SQLAlchemy(app)
sess = Session(app)
app.config['JWT_SECRET_KEY'] = 'some super secret key'

# def auth_wrapper():
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             token = request.cookies.get('token')
#             if authenticated_page(token) == False:
#                 return render_template("login.html",
#                                 brand_name = get_brand_name(),
#                                 login_required = True,
#                                 page_title = "Sign Up/Login")
#             return f(*args, **kwargs)
#         return decorated_function
#     return decorator

@app.route("/")
def home():
    page_title = "Home"
    return render_template("index.html",
                           brand_name = get_brand_name(),
                           page_title = page_title)

@app.route("/login")
def login():
    page_title = "Sign Up/Login"
    return render_template("login.html",
                           brand_name = get_brand_name(),
                           page_title = page_title)

@app.route("/logout")
def logout():
    page_title = "logout"
    token = request.cookies.get('token')
    return render_template("logout.html",
                           brand_name = get_brand_name(),
                           token = token,
                           page_title = page_title)

@app.route("/user/<username>")
def user(username):
    page_title = "Profile"
    return render_template("profile.html",
                           brand_name = get_brand_name(),
                           page_title = page_title,
                           username = username
                           )

@app.route("/profile")
def profile():
    page_title = "Profile"
    return render_template("profile.html",
                           brand_name = get_brand_name(),
                           page_title = page_title,
                           )


@app.route('/protected')
@auth_wrapper()
def protected():
    page_title = "Protected"
    token = request.cookies.get('token')
    # if authenticated_page(token) == False:
    #     return render_template("login.html",
    #                        brand_name = get_brand_name(),
    #                        login_required = True,
    #                        page_title = "Sign Up/Login")
    
    valid_token = validate_token(token)
    expires_in = token_expire_countdown(token)
    return render_template("protected.html",
                        brand_name = get_brand_name(),
                        page_title = page_title,
                        token = token,
                        expires_in = expires_in,
                        valid_token = valid_token,
                        )




if __name__ == "__main__":
    app.run()