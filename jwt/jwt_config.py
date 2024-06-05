import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from app_config import get_secret_key

from functools import wraps

app_secret_key = get_secret_key()

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
    return jwt.encode(payload, app_secret_key, algorithm='HS256')