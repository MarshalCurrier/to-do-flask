import jwt
import datetime
from functools import wraps
from flask import request, jsonify

from functools import wraps

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

