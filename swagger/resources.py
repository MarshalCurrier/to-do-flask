from flask_restx import Resource, Namespace
from .models import Users
from .api_models import user_model, user_signup_model, user_auth_model,user_login_model, get_users_model
from .extensions import *
from .models import Users
from datetime import datetime
# from  my_jwt.my_jwt_config import generate_token
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import hashlib

ns = Namespace("api", description="User API")

    
@ns.route("/user")
class UserListAPI(Resource):
    @ns.expect(user_model)
    @ns.marshal_with(get_users_model) 
    # @jwt_required()
    def get(self):
        return Users.query.all()
    
    @ns.expect(user_signup_model)
    @ns.marshal_with(user_signup_model)   
    def post(self):
        users = Users(
            username=ns.payload["username"],
            password=ns.payload["password"],
            email=ns.payload["email"],
            email_verified=False,
            roles_id = 1,
            account_status_id = 1,
            created_on = datetime.now()
            )
        
        db.session.add(users)
        db.session.commit()
        return users, 201


@ns.route("/login")  
class UserLoginAPI(Resource):
    @ns.expect(user_login_model)
    # @ns.marshal_with(user_login_model)
    def post(self):
            username=ns.payload["username"]
            password=ns.payload["password"]
            print("=========================================")
            print(f"{{username: {username}, password: {password}}}")
            print("=========================================")
            # username=ns.payload.get("username")
            # password=ns.payload.get("password")
            login_response = Users.query.filter(Users.username==username, 
                                                Users.password==password).one_or_none()
            
            print("=========================================")
            print(f"login_response: {login_response} login_repsonse type: {type(login_response)}")
            print("=========================================")
            if login_response is None:
                return "Invalid username or password", 401
            else:
                access_token = create_access_token(identity=username)
                # token = generate_token(login_response.users_id, login_response.username)
                return {"token": access_token}, 200
                return "success", 200
    
    # @ns.expect(user_signup_model)
    # @ns.marshal_with(user_signup_model)   
    # def post(self):
    #     user = User(
    #         username=ns.payload["username"],
    #         password=ns.payload["password"],
    #         email=ns.payload["email"],
    #         active = False
    #         )
    #     # print(user)
    #     # print(type(user))
    #     db.session.add(user)
    #     db.session.commit()
    #     return user, 201
    
@ns.route("/user/<username>")
class UserAPI(Resource):
    ns.doc(title="Something", description="Some Stuff About Users")
    @api.marshal_with(user_auth_model)
    def get(self, username):
        contact_data = Users.query.filter(Users.username==username).one_or_404()
        return contact_data
    
    def delete(self, username):
        request = Users.query.filter(Users.username==username).one_or_404()
        db.session.delete(request)
        db.session.commit()
        return {}