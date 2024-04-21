from flask import Flask, Blueprint
from flask_restx import Api, Namespace, inputs
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select



from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker

api_bp = Blueprint("swagger", __name__, url_prefix="swagger")
api = Api(api_bp, version="1.0",title="Swagger UI", description="Users to-do list")
db = SQLAlchemy()

# class UserAPI(Resource):


# def create_app():
    # db = SQLAlchemy()
    # app = Flask(__name__)
    
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres-to-do:strong-password@localhost:5432/to-do"   
    # blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
    # api = Api(
    #     blueprint,
    #     version="1.0",
    #     title="Mini REST API",
    #     description="A mini REST API",
    # )
    # ns = api.namespace("items", description="Item operations")
    # api.add_namespace(ns)
    # # api.init_app(app)
    # db.init_app(app)
    
    
    


    # return app