import unittest
import sys
sys.path.append("../VolunteerMatch")
from run import app
from app.volunteer_matching.data import events, volunteers
from flask import jsonify

class VolunteerMatchingTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_user_not_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False
            #sess['email'] = 'patelarti91@gmail.com'

        response = self.tester.get('/history/')
        self.assertIn(str.encode("Welcome! Please login to continue."), response.data)

    def test_user_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'

        response = self.tester.get('/history/')
        val = 'Volunteer Participation History'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)




if __name__ == "__main__":
    unittest.main()


