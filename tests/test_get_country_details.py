import unittest
from unittest.mock import patch, create_autospec, MagicMock
from src.models.country import Country
from src.app import create_app
from src.api.get_country_details import get_country_details


class MockCountry:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def query():
        pass


class TestGetCountryDetails(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('src.models.country.Country.query')
    def test_country_found(self, mock_query):
        country = MagicMock(spec=Country)
        country.name = 'TestCountry'
        country.total_plants = 10
        country.electric = 5

        type(country).__table__ = MagicMock()
        type(country).__table__.columns = []

        for column_name in ['name', 'total_plants', 'electric']:
            column = MagicMock()
            column.name = column_name
            type(country).__table__.columns.append(column)

        mock_query.filter_by.return_value.first.return_value = country

        expected = {'name': 'TestCountry', 'total_plants': 10, 'electric': 5}
        result = get_country_details('TestCountry')

        self.assertEqual(result, expected)

    @patch('src.models.country.Country.query')
    def test_country_found_case_insensitive(self, mock_query):
        country = MagicMock(spec=Country)
        country.name = 'Brazil'
        country.total_plants = 10
        country.electric = 5

        type(country).__table__ = MagicMock()
        type(country).__table__.columns = []
        for column_name in ['name', 'total_plants', 'electric']:
            column = MagicMock()
            column.name = column_name
            type(country).__table__.columns.append(column)

        mock_query.filter_by.return_value.first.side_effect = \
            lambda **kwargs: country if kwargs.get(
                'name', '').lower() == country.name.lower() else None

        expected = {'name': 'Brazil', 'total_plants': 10, 'electric': 5}
        result_lower = get_country_details('brazil')
        result_upper = get_country_details('BRAZIL')
        result_mixed = get_country_details('BrAzIl')

        self.assertEqual(result_lower, expected)
        self.assertEqual(result_upper, expected)
        self.assertEqual(result_mixed, expected)

    @patch('src.models.country.Country.query')
    def test_country_not_found(self, mock_query):
        mock_query.filter_by.return_value.first.return_value = None

        expected = {'error': 'Country not found'}, 404
        result = get_country_details('NonExistentCountry')

        self.assertEqual(result, expected)

    @patch('src.models.country.Country.query')
    def test_country_server_error(self, mock_query):
        mock_query.filter_by.side_effect = Exception('Unexpected error')

        expected = {'error': 'Unexpected error'}, 500
        result = get_country_details('TestCountry')

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
