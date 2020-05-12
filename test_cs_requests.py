import unittest
import uuid

from src.CsRequests import CsRequests


class TestCsRequest(unittest.TestCase):
    def test_get_reservation_details(self):
        session = CsRequests('admin', 'admin')
        details = session.get_reservation_details(str(uuid.UUID()))
        self.assertTrue(details.Name == 'bla')