import unittest
import psycopg2
from run import app

import sys

sys.path.append("../VolunteerMatch")


class NotificationsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tester = app.test_client(cls)

    def test_notification_signed_in_false(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/notifications/')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_notification_signed_in_true(self):
        conn = psycopg2.connect(database="volunteers_db", user="postgres",
                                password="arti", host="localhost", port="5432")
        cursor = conn.cursor()

        command = f"INSERT INTO usercredentials (username, email, password, is_admin)" \
                  f" VALUES ('unit_test', 'unit_test@domain.com','super_secret_password', true);"
        cursor.execute(command)
        cursor.execute(f"SELECT id FROM usercredentials"
                       f" WHERE email='unit_test@domain.com';")
        user_id = cursor.fetchone()[0]
        conn.commit()

        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'unit_test@domain.com'
            sess['username'] = 'unit_test'
            sess['user_id'] = user_id
            sess['is_admin'] = True

        # push a fake notification to the db and check for its existence in the front end.
        command = f"INSERT INTO notifications (user_id, msg, notification_type) " \
                  f"VALUES ({sess['user_id']}, " \
                  f"'Test notification for automated unit testing with fake user {sess['email']}...', {True});"
        cursor.execute(command)
        conn.commit()

        response = self.tester.get('/notifications/')
        self.assertIn(str.encode(f"Test notification for automated unit testing with fake user {sess['email']}..."),
                      response.data)
        # print(f'response.data => {response.data}')
        self.assertEqual(200, response.status_code)

        # delete the fake notif.
        command = (f"DELETE FROM notifications "
                   f"WHERE user_id = {user_id};")
        cursor.execute(command)

        command = f"DELETE FROM usercredentials " \
                  f"WHERE id = {user_id};"
        cursor.execute(command)
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    unittest.main()
