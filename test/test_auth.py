import unittest
import sys
sys.path.append("../VolunteerMatch")
from run import app
from flask import jsonify

class AuthTest(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_index(self):
        tester = app.test_client(self)

        response = tester.get('/', content_type='text/HTML')
        self.assertEqual(response.status_code, 200)

    # def test_login(self):
    #     tester = app.test_client(self)
    #
    #     data = {
    #         "email":"patelarti91@gmail.com",
    #         "password":"1111"
    #     }
    #
    #     response = tester.post('/login', data=data, follow_redirects=True)
    #     # val = f"Welcome {data['email']}!"
    #     val = "login success"
    #     # self.assertEqual(response.status_code, 200)
    #     self.assertIn(str.encode(val), response.data)



if __name__ == "__main__":
    unittest.main()

