from flask import Blueprint
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

api_bp = Blueprint("swagger", __name__, url_prefix="/swagger/")
api = Api(api_bp, version="1.0",title="Swagger UI", description="Users to-do list")
db = SQLAlchemy()
jwt = JWTManager()
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

authorizations = {
    "jsonwebtoken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}