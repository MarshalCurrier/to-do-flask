from flask_restx import Resource, Namespace
# from ..models import Roles
# from .api_models import get_roles_model
# from ..extensions import *
# from ..models import Roles
# from datetime import datetime
# from  my_jwt.my_jwt_config import generate_token
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import hashlib

account_status_ns = Namespace("account_status", description="Account Status API")

    
# @users_ns.route("/user")
# class UserListAPI(Resource):
#     @users_ns.expect(user_model)
#     @users_ns.marshal_with(get_users_model) 
#     # @jwt_required()
#     def get(self):
#         return Users.query.all()
    
#     @users_ns.expect(user_signup_model)
#     @users_ns.marshal_with(user_signup_model)   
#     def post(self):
#         users = Users(
#             username=users_ns.payload["username"],
#             password=users_ns.payload["password"],
#             email=users_ns.payload["email"],
#             email_verified=False,
#             roles_id = 1,
#             account_status_id = 1,
#             created_on = datetime.now()
#             )
        
#         db.session.add(users)
#         db.session.commit()
#         return users, 201


# @users_ns.route("/login")  
# class UserLoginAPI(Resource):
#     @users_ns.expect(user_login_model)
#     # @users_ns.marshal_with(user_login_model)
#     def post(self):
#             username=users_ns.payload["username"]
#             password=users_ns.payload["password"]
#             login_response = Users.query.filter(Users.username==username, 
#                                                 Users.password==password).one_or_none()
#             if login_response is None:
#                 return "Invalid username or password", 401
#             else:
                
#                 access_token = create_access_token(identity=username)
#                 return {"token": access_token}, 200
    
# @users_ns.route("/user/<username>")
# class UserAPI(Resource):
#     users_ns.doc(title="Something", description="Some Stuff About Users")
#     @api.marshal_with(user_auth_model)
#     def get(self, username):
#         contact_data = Users.query.filter(Users.username==username).one_or_404()
#         return contact_data
    
#     def delete(self, username):
#         request = Users.query.filter(Users.username==username).one_or_404()
#         db.session.delete(request)
#         db.session.commit()
#         return {}