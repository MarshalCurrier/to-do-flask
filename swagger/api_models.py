from .extensions import api
from flask_restx import fields

# course_model = api.model("Course",{
#     "id": fields.Integer,
#     "name": fields.String
# })

# student_model = api.model("Student",{
#     "id": fields.Integer,
#     "name": fields.String
# })

# course_post_model = api.model("CoursePost",{
#     "name" :fields.String,
# })

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