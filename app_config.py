environment = 'development'
brand_name = "Update app_config.py"

## Dev DB Connection Info
DEV_PG_USER = "productivitypals"
DEV_PG_PASS = "Pr0duc71v17yp4l$"
DEV_PG_URL = "hirehumble.com"
DEV_PG_PORT = "5432"
DEV_PG_DB = "productivitypals"

def get_brand_name():
    return brand_name

class config:
    SQLALCHEMY_DATABASE_URI = ""
    def __init__(self,environment): 
        if environment == 'development':
            self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DEV_PG_USER}:{DEV_PG_PASS}@{DEV_PG_URL}:{DEV_PG_PORT}/{DEV_PG_DB}"
            