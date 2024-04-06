import os
from src.helpers import get_db_connection_str


class Config:
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_TABLE = os.getenv('POSTGRES_TABLE')
    SQLALCHEMY_DATABASE_URI = get_db_connection_str()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
