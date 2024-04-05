import unittest
from unittest.mock import patch

from helpers import get_db_connection_str


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


if __name__ == '__main__':
    unittest.main()
