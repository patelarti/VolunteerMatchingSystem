import unittest
import sys

sys.path.append("../VolunteerMatch")
from run import app
from flask import jsonify

class NotificationsTest(unittest.TestCase):
    def test_notification_signed_in_false(self):
        tester = app.test_client(self)
        with tester.session_transaction() as sess:
            sess['signed_in'] = False

            response = tester.get('/notifications/')
            self.assertEqual(response.status_code, 200)

    def test_notification_signed_in_true(self):
        tester = app.test_client(self)

        with tester.session_transaction() as sess:
            sess['signed_in'] = True

        response = tester.get('/notifications/')
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
