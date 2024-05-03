from swagger.error_handlers import ns_error_handling
from swagger.resources import ns    
from swagger.extensions import api

api.add_namespace(ns_error_handling)
api.add_namespace(ns)