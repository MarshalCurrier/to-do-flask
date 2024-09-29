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


user_login_model = api.model("UserLoginGet",{
    "username" :fields.String,
    "password" :fields.String,
})

#######################
## Rebuild
#######################

get_users_model = api.model("User",{
    "users_id": fields.Integer,
    "username": fields.String, 
    "email": fields.String,
})

user_signup_model = api.model("Users",{
    "username": fields.String,
    "password": fields.String,
    "email" : fields.String,
})