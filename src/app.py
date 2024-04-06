from flask import Flask
from src.config import Config
from src.api.get_country_details import get_country_details
from src.api.get_plant_type_counts import plant_counts
from src.api.list_plant_types import list_plant_types
from src.api.list_countries import list_countries
from src.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.add_url_rule('/api/countries',
                     view_func=list_countries, methods=['GET'])
    app.add_url_rule('/api/countries/<country_name>',
                     view_func=get_country_details, methods=['GET'])
    app.add_url_rule(
        '/api/plants', view_func=list_plant_types, methods=['GET'])
    app.add_url_rule('/api/plants/<plant_type>',
                     view_func=plant_counts, methods=['GET'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
