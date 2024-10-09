from flask_restx import Namespace
import json
from sqlalchemy.exc import IntegrityError, DataError, NoResultFound

ns_error_handling = Namespace("")

message_key = "message"

# @ns_error_handling.errorhandler(InvalidHeaderError)
#     def invalid_header_error(error):
#         message = error.args[0]
#         return {message_key: message}, 401

@ns_error_handling.errorhandler(NoResultFound)
def no_result_found(error):
    message = error.args[0]
    return {message_key: message}, 404

@ns_error_handling.errorhandler(IntegrityError)
def integrity_error(error):
    message = error.args[0]
    if "(psycopg2.errors.UniqueViolation)" in message:
        details = message.split("DETAIL: ")[1][:-2]
        details = details.split('=', 1)[1]
        details = details.replace('(', '')
        details = details.replace(')', '')
        message = f"{details}"
    elif "(psycopg2.errors.NotNullViolation)" in message:
        details = message.split("\nDETAIL: ")[0][35:]
        message = f"Value unprovided or cannot be null: {details}"
    elif "(psycopg2.errors.ForeignKeyViolation)" in message:
        details = message.split("DETAIL: ")[1][:-2]
        message = f"Foreign key constraint violation:{details}"
    return {message_key: message}, 400

@ns_error_handling.errorhandler(ValueError)
def value_error(error):
    message = error.args[0]
    return {message_key: message}, 400

@ns_error_handling.errorhandler(DataError)
def data_error(error):
    message = error.args[0]
    if "(psycopg2.errors.InvalidTextRepresentation)" in message:
        details = message.split('\nLINE')[0][44:].replace('"', "'")
        message = f"Invalid text representation: {details}"
    return {message_key: message}, 400