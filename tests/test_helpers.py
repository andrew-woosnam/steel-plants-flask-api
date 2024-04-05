import unittest
from unittest.mock import patch, mock_open
from sqlalchemy import Integer, String
from app.helpers import get_db_connection_str, infer_column_types


class TestHelpers(unittest.TestCase):
    @patch('os.getenv')
    def test_get_db_connection_str(self, mock_getenv):
        mock_env_vars = {
            'POSTGRES_USER': 'user',
            'POSTGRES_PASSWORD': 'pass',
            'POSTGRES_DB': 'db',
            'POSTGRES_HOST': 'host',
            'POSTGRES_PORT': '5432'
        }

        def getenv_side_effect(var_name, default=None):
            return mock_env_vars.get(var_name, 'default_value')

        mock_getenv.side_effect = getenv_side_effect

        expected_str = 'postgresql://user:pass@host:5432/db'
        self.assertEqual(get_db_connection_str(), expected_str)


class TestInferColumnTypes(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=(
        "Country,Total Plants,electric,\"electric, oxygen\"\n"
        "Albania,1,0,0\n"
        "Algeria,4,1,0\n"
        "Angola,1,1,0"))
    def test_infer_column_types(self, mock_file):
        expected = {
            'Country': String(255),
            'Total Plants': Integer(),
            'electric': Integer(),
            'electric, oxygen': Integer()
        }
        result = infer_column_types('fake_file_path.csv')

        # ensure inferred col types match expected
        for column, column_type in expected.items():
            with self.subTest(column=column):
                self.assertIsInstance(result[column], type(column_type))


if __name__ == '__main__':
    unittest.main()
