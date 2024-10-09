from swagger.error_handlers import ns_error_handling
from swagger.users.resources import users_ns    
from swagger.roles.resources import roles_ns   
from swagger.account_status.resources import account_status_ns    
from swagger.extensions import api

api.add_namespace(ns_error_handling)
api.add_namespace(users_ns)
api.add_namespace(roles_ns)
api.add_namespace(account_status_ns)