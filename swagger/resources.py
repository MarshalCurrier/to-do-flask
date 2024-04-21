from flask_restx import Resource, Namespace
from .models import *
from .api_models import *
from .extensions import *
from .models import *
import hashlib

ns = Namespace("api")



# @ns.route("hello")
# class Hello(Resource):
#     def get(self):
#         return {"hello" : "rest"}
    
# @ns.route("/courses")
# class CourseAPI(Resource):
#     @ns.marshal_list_with(course_model)
#     def get(self):
#         return Course.query.all()
    
#     @ns.expect(course_post_model)
#     @ns.marshal_with(course_model)
#     def post(self):
#         course = Course(name=ns.payload["name"])
#         db.session.add(course)
#         db.session.commit()
#         return course, 201

    
# @ns.route("/students")
# class StudentAPI(Resource):
#     @ns.marshal_list_with(student_model)
#     def get(self):
#         return Student.query.all()
    
@ns.route("/user")
class UserListAPI(Resource):
    @ns.expect(user_model)
    def get(self):
        return User.query.all()
    
    @ns.expect(user_signup_model)
    def post(self):
        user = User(username=ns.payload["username"])
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