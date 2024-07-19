import unittest
from run import app
import sys
sys.path.append("../VolunteerMatch")


class AuthTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_canary(self):
        self.assertTrue(True)

    def test_index(self):
        response = self.tester.get('/', content_type='text/HTML')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_login_send_get_request(self):
        response = self.tester.get('/login')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_login_incorrect_pwd(self):
        data = {
            "email": "patelarti91@gmail.com",
            "password": "abcd"
        }

        response = self.tester.post('/login', json=data)
        val = '{"message":"Invalid email or password"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(401, response.status_code)

    def test_login_correct_pwd(self):
        data = {
            "email": "patelarti91@gmail.com",
            "password": "1111"
        }

        response = self.tester.post('/login', json=data)
        val = '{"message":"Login successful"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_base_not_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/base')
        self.assertIn(str.encode("Welcome! Please login to continue."), response.data)

    def test_base_signed_in(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'

        response = self.tester.get('/base')
        self.assertIn(str.encode(sess['email']), response.data)

    def test_logout(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'

        self.tester.get('/logout')

        with self.tester.session_transaction() as sess:
            self.assertEqual(sess['signed_in'], False)
            self.assertEqual(sess['email'], "")

    def test_register_send_get_request(self):
        response = self.tester.get('/register')
        val = 'Create your account. It\'s free and only takes a minute.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_register_password_do_not_match(self):
        data = {
            "email": "test@gmail.com",
            "password": "1111",
            "confirmPassword": "1234"
        }

        response = self.tester.post('/register', json=data)
        val = '{"message":"Passwords do not match"}\n'
        # print(response.data)
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(400, response.status_code)

    def test_register_email_already_exists(self):
        data = {
            "email": "patelarti91@gmail.com",
            "password": "1111",
            "confirmPassword": "1111"
        }

        response = self.tester.post('/register', json=data)
        val = '{"message":"User already exists"}\n'
        # print(response.data)
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(400, response.status_code)

    def test_register_with_new_email(self):
        data = {
            "email": "abc@gmail.com",
            "password": "1111",
            "confirmPassword": "1111"
        }

        response = self.tester.post('/register', json=data)
        val = '{"message":"User registered successfully"}\n'
        # print(response.data)
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(201, response.status_code)

        with self.tester.session_transaction() as sess:
            self.assertEqual(sess['signed_in'], True)
            self.assertEqual(sess['email'], "abc@gmail.com")

    def test_forgot_send_get_request(self):
        response = self.tester.get('/forgot')
        val = 'Forgot Password'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_forgot_send_post_request_with_existing_user(self):
        data = {
            "email": "patelarti91@gmail.com",
        }

        response = self.tester.post('/forgot', json=data)
        val = '{"message":"Password reset link sent to your email"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_forgot_send_post_request_with_not_existing_user(self):
        data = {
            "email": "abc@gmail.com",
        }

        response = self.tester.post('/forgot', json=data)
        val = '{"message":"Email not found"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(404, response.status_code)

    def test_reset_send_get_request(self):
        response = self.tester.get('/reset')
        val = 'Reset Password'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_reset_send_post_request_with_matching_password_and_existing_email(self):
        data = {
            "email": "patelarti91@gmail.com",
            "newPassword": "1234",
            "confirmNewPassword": "1234"

        }
        response = self.tester.post('/reset', json=data)
        val = '{"message":"Password reset successfully"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_reset_send_post_request_with_non_matching_password_and_existing_email(self):
        data = {
            "email": "patelarti91@gmail.com",
            "newPassword": "1111",
            "confirmNewPassword": "1234"

        }
        response = self.tester.post('/reset', json=data)
        val = '{"message":"Passwords do not match"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(400, response.status_code)

    def test_reset_send_post_request_with_matching_password_and_non_existing_email(self):
        data = {
            "email": "wrong_email_abc@gmail.com",
            "newPassword": "1234",
            "confirmNewPassword": "1234"

        }
        response = self.tester.post('/reset', json=data)
        val = '{"message":"Email not found"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(404, response.status_code)


if __name__ == "__main__":
    unittest.main()
