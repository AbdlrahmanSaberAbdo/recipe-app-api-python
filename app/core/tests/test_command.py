from unittest.mock import patch

from django.core.management import call_command
# simulte error is db available or not
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    """Django command to pause execution until database is available"""

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # Overrid the behave of getitem function
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # mock for replace the behaviour of time sleep
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
