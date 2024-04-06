from flask import jsonify
from src.models.country import Country


def list_countries():
    try:
        countries = Country.query.all()
        countries_list = [country.name for country in countries]
        return jsonify(countries_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
