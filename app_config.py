from datetime import timedelta
environment = 'development'
brand_name = "The Roster"
secret_key = 'some super secret key'

## Dev DB Connection Info
DEV_PG_USER = "someuser"
DEV_PG_PASS = "SomePassword"
DEV_PG_URL = "localhost"
DEV_PG_PORT = "5432"
DEV_PG_DB = "to-do"

def get_brand_name():
    return brand_name

def get_secret_key():
    return secret_key

JWT_EXPIRATION_MINUTES = 43200
JWT_EXPIRATION_MINUTES = 1

class config:
    SQLALCHEMY_DATABASE_URI = ""
    def __init__(self,environment): 
        if environment == 'development':
            self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DEV_PG_USER}:{DEV_PG_PASS}@{DEV_PG_URL}:{DEV_PG_PORT}/{DEV_PG_DB}"
            self.JWT_EXPIRATION_MINUTES = JWT_EXPIRATION_MINUTES
            