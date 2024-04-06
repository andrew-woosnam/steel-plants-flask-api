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


if __name__ == '__main__':
    unittest.main()
