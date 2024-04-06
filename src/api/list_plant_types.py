from flask import jsonify
from src.models.country import Country


def list_plant_types():
    try:
        # Get all column names from the Country model, excluding the 'country' column
        plant_types = [
            column.name for column in Country.__table__.columns if column.name != 'country']
        return jsonify(plant_types), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
