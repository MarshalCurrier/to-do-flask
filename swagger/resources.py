from flask_restx import Resource, Namespace
from .models import User
from .api_models import user_post_model, user_model, user_signup_model, user_auth_model
from .extensions import *
from .models import User
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