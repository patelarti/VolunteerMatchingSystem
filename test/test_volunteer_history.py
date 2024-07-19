import unittest
from run import app
import sys

sys.path.append("../VolunteerMatch")


class VolunteerMatchingTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_user_not_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/history/')
        self.assertIn(str.encode("Welcome! Please login to continue."), response.data)

    def test_user_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.get('/history/')
        val = 'Volunteer Participation History'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()