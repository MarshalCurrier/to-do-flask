from ..extensions import api
from flask_restx import fields

#######################
## Rebuild
#######################

get_account_status_model = api.model("AccountStatus",{
    "account_status_id": fields.Integer,
    "account_status_name": fields.String, 
})