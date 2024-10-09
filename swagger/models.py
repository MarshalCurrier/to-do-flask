from .extensions import db

class Users(db.Model):
    # __table_args__ = {'schema': 'public'}
    users_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(50))
    email_verified = db.Column(db.Boolean)
    roles_id = db.Column(db.Integer)
    account_status_id = db.Column(db.Integer)
    created_on = db.Column(db.Date)

class AccountStatus(db.Model):
    # __table_args__ = {'schema': 'public'}
    account_status_id = db.Column(db.Integer, primary_key=True)
    account_status_name = db.Column(db.String(24), unique=True)

class Roles(db.Model):
    # __table_args__ = {'schema': 'public'}
    roles_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(24), unique=True)

class TaskStatus(db.Model):
    # __table_args__ = {'schema': 'public'}
    task_status_id = db.Column(db.Integer, primary_key=True)
    task_status_name = db.Column(db.String(24), unique=True)

class Profiles(db.Model):
    # __table_args__ = {'schema': 'public'}
    profile_id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.String(24))
    bio = db.Column(db.String(5000))
    goals = db.Column(db.String(5000))
    phone = db.Column(db.String(24))
    phone_verified = db.Column(db.Boolean)
    
class Tasks(db.Model):
    # __table_args__ = {'schema': 'public'}
    task_id = db.Column(db.Integer, primary_key=True)
    assigned_by = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer)
    task_status = db.Column(db.Integer)
    date_assigned = db.Column(db.TIMESTAMP)
    date_completed = db.Column(db.TIMESTAMP)
    target_date = db.Column(db.TIMESTAMP)
    task_title = db.Column(db.String(50))
    task_body = db.Column(db.String(5000))
    
