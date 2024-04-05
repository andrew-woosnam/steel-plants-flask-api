import os
import helpers
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.list_countries import list_countries
from database import db
app = Flask(__name__)

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = helpers.get_db_connection_str()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.add_url_rule('/api/countries', view_func=list_countries, methods=['GET'])

db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
