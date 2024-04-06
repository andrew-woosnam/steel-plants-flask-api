from flask import jsonify
from models.country import Country


def plant_counts(plant_type):
    try:
        # Check if the plant_type is a valid column in the Country model
        if plant_type not in [column.key for column in Country.__table__.columns]:
            return jsonify({'error': 'Invalid plant type'}), 400

        # Query the database for all countries with their specific plant count
        countries = Country.query.with_entities(
            Country.name, getattr(Country, plant_type)).all()

        # Create a list of key/value pairs where keys are country names and values are the counts
        plant_counts_list = [{country[0]: country[1]} for country in countries]

        return jsonify(plant_counts_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
