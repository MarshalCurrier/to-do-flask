from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres-to-do:strong-password@localhost:5432/db")