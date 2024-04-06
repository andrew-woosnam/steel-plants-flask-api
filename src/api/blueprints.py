from flask import Blueprint
from src.api.list_countries import list_countries
from src.api.get_country_details import get_country_details
from src.api.list_plant_types import list_plant_types
from src.api.get_plant_type_counts import plant_counts

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/countries', methods=['GET'])
def countries():
    return list_countries()


@api_blueprint.route('/countries/<country_name>', methods=['GET'])
def country_details(country_name):
    return get_country_details(country_name)


@api_blueprint.route('/plants', methods=['GET'])
def plants():
    return list_plant_types()


@api_blueprint.route('/plants/<plant_type>', methods=['GET'])
def plant_type_counts(plant_type):
    return plant_counts(plant_type)
