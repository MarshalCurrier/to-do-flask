
import jwt as jwt_auth
from flask import request, render_template, redirect
from app_config import config,  environment, get_secret_key, get_brand_name
import datetime
import hashlib
from functools import wraps

secret_key = get_secret_key()

def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hash_password = hash_object.hexdigest()
    return hash_password

def is_token_expired(token, secret_key):
    try:
        decoded_token = jwt_auth.decode(token, secret_key, algorithms=['HS256'])
        exp_timestamp = decoded_token.get('exp')
        if exp_timestamp:
            current_time = datetime.datetime.utcnow().timestamp()
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print(exp_timestamp)
            print(current_time)
            print(exp_timestamp - current_time)
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            return exp_timestamp < current_time
        else:
            return False  # Token doesn't have an expiration claim, consider it valid
    except jwt_auth.ExpiredSignatureError:
        return True  # Token is expired
    except jwt_auth.InvalidTokenError:
        return True  # Token is invalid for other reasons
    
def validate_token(token):
    try:
        payload = jwt_auth.decode(token, secret_key , algorithms="HS256")
        print(payload)
        return payload
    except jwt_auth.ExpiredSignatureError:
        return None  # Token expired
    except jwt_auth.InvalidTokenError:
        return None  # Invalid token
    
def token_expire_countdown(token):
    try:
        expires_in = datetime.datetime.fromtimestamp(jwt_auth.decode(token, secret_key, algorithms='HS256')['exp']) - datetime.datetime.now()
        return expires_in
    except jwt_auth.ExpiredSignatureError:
        return True
    except jwt_auth.InvalidTokenError:
        return True

def authenticated_page(token):
    try:
        valid_token = validate_token(token)
        expires_in = token_expire_countdown(token)
        if token == "":
            return False
        if valid_token == None:
            return False
        if expires_in == True:
            return False
        return True
    except:
        return render_template("login.html",
                        brand_name = get_brand_name(),
                        login_required = True,
                        page_title = "Sign Up/Login")
    
def auth_wrapper():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.cookies.get('token')
            if authenticated_page(token) == False:
                return render_template("login.html",
                                brand_name = get_brand_name(),
                                login_required = True,
                                page_title = "Sign Up/Login")
            return f(*args, **kwargs)
        return decorated_function
    return decorator
