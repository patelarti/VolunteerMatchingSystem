import unittest
from run import app
import sys

sys.path.append("../VolunteerMatch")


class AuthTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_user_not_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/profile/')
        self.assertIn(str.encode("Welcome! Please login to continue."), response.data)

    def test_user_signed_in_goes_to_profile(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.get('/profile/')
        val = 'User Profile Management'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_user_profile_with_non_existing_user(self):
        data = {
            "email": "wrong_email_for_user_profile@gmail.com",
        }
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = data['email']
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.post('/profile/', json=data)
        val = '{"message":"User not found"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(404, response.status_code)

    def test_user_profile_with_existing_user(self):
        data = {
            "email": "patelarti91@gmail.com",
        }
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = data['email']
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.post('/profile/', json=data)
        val = '{"message":"Profile updated successfully"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
