environment = 'development'


class config:
    SQLALCHEMY_DATABASE_URI = ""
    def __init__(self,environment): 
        if environment == 'development':
            self.SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://productivitypals:Pr0duc71v17yp4l$@hirehumble.com:5432/productivitypals"
