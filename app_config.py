environment = 'development'
brand_name = "Update app_config.py"
secret_key = 'JustSomeJunkForNow'

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

class config:
    SQLALCHEMY_DATABASE_URI = ""
    def __init__(self,environment): 
        if environment == 'development':
            self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DEV_PG_USER}:{DEV_PG_PASS}@{DEV_PG_URL}:{DEV_PG_PORT}/{DEV_PG_DB}"
            