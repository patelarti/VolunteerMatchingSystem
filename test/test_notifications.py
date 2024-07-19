import unittest
from run import app

import sys

sys.path.append("../VolunteerMatch")


class NotificationsTest(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)

    def test_notification_signed_in_false(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/notifications/')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_notification_signed_in_true(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.get('/notifications/')
        val = 'Your Notifications'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
