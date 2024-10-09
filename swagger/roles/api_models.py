from ..extensions import api
from flask_restx import fields

#######################
## Rebuild
#######################

get_roles_model = api.model("Roles",{
    "roles_id": fields.Integer,
    "role_name": fields.String, 
})