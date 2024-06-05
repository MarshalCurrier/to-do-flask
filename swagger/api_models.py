from .extensions import api
from flask_restx import fields

user_model = api.model("User",{
    "user_id": fields.Integer,
    "username": fields.String
})

user_auth_model = api.model("User",{
    "user_id": fields.Integer,
    "username": fields.String,
    "password": fields.String,
    "email" : fields.String,
    "about_me" : fields.String,
    "active" : fields.Boolean
})

user_signup_model = api.model("User",{
    "username": fields.String,
    "password": fields.String,
    "email" : fields.String,
})

user_post_model = api.model("UserPost",{
    "username" :fields.String,
})

user_login_model = api.model("UserLoginGet",{
    "username" :fields.String,
    "password" :fields.String,
})