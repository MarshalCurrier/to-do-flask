from flask_restx import Resource, Namespace
from ..models import Users, Roles, AccountStatus
from .api_models import user_model, user_signup_model, user_auth_model,user_login_model, get_users_model
from ..extensions import *
from datetime import datetime, timedelta
from swagger.extensions import db#, authorizations
# from  my_jwt.my_jwt_config import generate_token
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import hashlib
from app_config import config,  environment
from jwt_custom_func.jwt_custom_funk import hash_password
import hashlib

authorizations = {
    "jsonwebtoken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

users_ns = Namespace("api", description="User API", authorizations=authorizations)

app_config = config(environment)
    
@users_ns.route("/user")
class UserListAPI(Resource):
    method_decorators = [jwt_required()]
    @users_ns.doc(security='jsonwebtoken')
    @users_ns.marshal_with(get_users_model) 
    # @jwt_required()
    def get(self):
        return Users.query.all()
    
    @users_ns.expect(user_signup_model)
    def post(self):
        username = users_ns.payload["username"]
        email=users_ns.payload["email"]
        password=hash_password(users_ns.payload["password"])
        # hash_object = hashlib.sha256()
        # hash_object.update(password.encode())
        # hash_password = hash_object.hexdigest()
        users = Users(
            username=username,
            password=password,
            email=email,
            email_verified=False,
            roles_id = 1,
            account_status_id = 1,
            created_on = datetime.now()
            )
        
        db.session.add(users)
        db.session.commit()
        
        additional_claims = {
            "role": "User",
            "account_status": "Pending"
        }
        expires_time = timedelta(minutes=app_config.JWT_EXPIRATION_MINUTES)
        access_token = create_access_token(username, expires_delta=expires_time, additional_claims=additional_claims)
        response = {
                    "username": username,
                    "email": email,
                    "token": access_token
                }
        return response, 201


@users_ns.route("/login")
class UserLoginAPI(Resource):
    # method_decorators = [jwt_required()]
    # @users_ns.doc(security='jsonwebtoken')
    @users_ns.expect(user_login_model)
    def post(self):
            username=users_ns.payload["username"]
            password=hash_password(users_ns.payload["password"])
            login_response = db.session.query(Users, Roles, AccountStatus).\
                                        join(Roles, Users.roles_id == Roles.roles_id).\
                                        join(AccountStatus, Users.account_status_id == AccountStatus.account_status_id).\
                                        filter(Users.username==username,  Users.password==password).one_or_none(),
            try:
                additional_claims = {
                    "role": login_response[0][1].role_name,
                    "account_status": login_response[0][2].account_status_name
                }
                expires_time = timedelta(minutes=app_config.JWT_EXPIRATION_MINUTES)
                access_token = create_access_token(username, expires_delta=expires_time, additional_claims=additional_claims)
                # access_token = create_access_token(username,additional_claims=additional_claims)
                response = {
                    "username": login_response[0][0].username,
                    "password": login_response[0][0].password,
                    "email": login_response[0][0].email,
                    "role": login_response[0][1].role_name,
                    "account_status": login_response[0][2].account_status_name,
                    "token": access_token
                }
                return response, 200
            except:
                return "Invalid Login Credentials", 401
    
@users_ns.route("/user/<username>")
class UserAPI(Resource):
    users_ns.doc(title="Something", description="Some Stuff About Users")
    @api.marshal_with(user_auth_model)
    def get(self, username):
        contact_data = Users.query.filter(Users.username==username).one_or_404()
        return contact_data
    
    def delete(self, username):
        request = Users.query.filter(Users.username==username).one_or_404()
        db.session.delete(request)
        db.session.commit()
        return {}