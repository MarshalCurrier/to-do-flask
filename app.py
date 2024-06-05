
from flask import Flask, Blueprint, redirect, render_template,request,session, url_for,jsonify
from flask_restx import Api, Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_jwt_extended import JWTManager
import jwt
import datetime
from functools import wraps
from swagger.extensions import *
from app_config import config,  environment
from app_config import get_brand_name, get_secret_key


app = Flask(__name__)
app_config = config(environment)


app.register_blueprint(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = app_config.SQLALCHEMY_DATABASE_URI 
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = get_secret_key()
db.init_app(app)
# db = SQLAlchemy(app)
sess = Session(app)
jwt = JWTManager(app)

def jwt_token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['sub']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return func(current_user, *args, **kwargs)
    return decorated

def generate_token(user_id, username):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expiration time
        'iat': datetime.datetime.utcnow(),  # Token issuance time
        'sub': user_id,  # Subject (user ID)
        'username': username  # Additional claims (e.g., username)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

@app.route('/protected', methods=['GET'])
@jwt_token_required
def protected(current_user):
    return jsonify({'message': f'Hello, {current_user}!'})

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

@app.route("/profile")
def profile():
    if (session == None or session.get('username') == None):
        return redirect(url_for('login'))
    page_title = "Profile"
    return render_template("profile.html",
                           brand_name = get_brand_name(),
                           page_title = page_title)


if __name__ == "__main__":
    app.run()