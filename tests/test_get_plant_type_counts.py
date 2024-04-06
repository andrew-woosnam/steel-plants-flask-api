from unittest.mock import patch, MagicMock
import unittest
from flask import jsonify
from src.app import create_app
from src.models.country import Country
from src.api.get_plant_type_counts import plant_counts


class TestPlantCounts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('src.models.country.Country.query')
    def test_plant_counts_invalid_plant_type(self, mock_query):
        Country.__table__.columns = [MagicMock(key='valid_plant_type')]

        response, status_code = plant_counts('invalid_plant_type')

        expected_response = jsonify({'error': 'Invalid plant type'})
        self.assertEqual(status_code, 400)
        self.assertEqual(response.json, expected_response.json)

    @patch('src.models.country.Country.query')
    @patch('src.models.country.Country.__table__.columns')
    def test_plant_counts_success(self, mock_columns, mock_query):
        mock_columns.__iter__.return_value = [MagicMock(key='plant_type')]
        setattr(Country, 'plant_type', MagicMock())
        mock_query.with_entities.return_value.all.return_value = [
            ('Country1', 10), ('Country2', 20)]

        response, status_code = plant_counts('plant_type')

        expected_response = jsonify([{'Country1': 10}, {'Country2': 20}])
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, expected_response.json)

    @patch('src.models.country.Country.query')
    @patch('src.models.country.Country.__table__.columns')
    def test_plant_counts_server_error(self, mock_columns, mock_query):
        mock_columns.__iter__.return_value = [MagicMock(key='plant_type')]
        setattr(Country, 'plant_type', MagicMock())
        mock_query.with_entities.side_effect = Exception('Super cool error')

        response, status_code = plant_counts('plant_type')

        expected_response = jsonify({'error': 'Super cool error'})
        self.assertEqual(status_code, 500)
        self.assertEqual(response.json, expected_response.json)
