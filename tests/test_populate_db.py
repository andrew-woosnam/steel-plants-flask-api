import unittest
from unittest.mock import patch
from app.populate_db import get_db_connection_str


class TestPopulateDB(unittest.TestCase):
    @patch('os.getenv')
    def test_get_db_connection_str(self, mock_getenv):
        mock_getenv.side_effect = ['user', 'pass', 'db', 'host', '5432']
        expected_str = 'postgresql://user:pass@host:5432/db'
        self.assertEqual(get_db_connection_str(), expected_str)


if __name__ == '__main__':
    unittest.main()
