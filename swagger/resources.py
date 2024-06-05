from flask_restx import Resource, Namespace
from .models import User
from .api_models import user_post_model, user_model, user_signup_model, user_auth_model,user_login_model
from .extensions import *
from .models import User
from  jwt.jwt_config import generate_token
import hashlib

ns = Namespace("api")

    
@ns.route("/user")
class UserListAPI(Resource):
    @ns.expect(user_model)
    def get(self):
        return User.query.all()
    
    @ns.expect(user_signup_model)
    @ns.marshal_with(user_signup_model)   
    def post(self):
        user = User(
            username=ns.payload["username"],
            password=ns.payload["password"],
            email=ns.payload["email"],
            active = False
            )
        # print(user)
        # print(type(user))
        db.session.add(user)
        db.session.commit()
        return user, 201


@ns.route("/login")  
class UserLoginAPI(Resource):
    @ns.expect(user_login_model)
    # @ns.marshal_with(user_login_model)
    def post(self):
            username=ns.payload.get("username")
            password=ns.payload.get("password")
            login_response = User.query.filter(User.username==username and User.password==password).one_or_none()
            if login_response is None:
                return "Invalid username or password", 401
            else:
                token = generate_token(login_response.user_id, login_response.username)
                return {"token": token.decode("UTF-8")}, 200
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
        contact_data = User.query.filter(User.username==username).one_or_404()
        return contact_data
    
    def delete(self, username):
        request = User.query.filter(User.username==username).one_or_404()
        db.session.delete(request)
        db.session.commit()
        return {}