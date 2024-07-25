import unittest
import sys
import psycopg2

sys.path.append("../VolunteerMatch")
from run import app


class EventManagementTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_event_management_signed_in_false(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/events/')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_event_management_signed_in_true(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
            sess['username'] = sess['email'].split('@')[0]

        response = self.tester.get('/events/')
        val = 'Event Management Form'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_display_signed_in_false(self):
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = False

        response = self.tester.get('/events/display.html')
        val = 'Welcome! Please login to continue.'
        self.assertIn(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)

    def test_display_signed_in_true(self):
        # first create a unit_test user. Fetch its user_id. Then perform the test. Then delete the user and the event.
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

        data = {"eventName": "My Event",
                "eventDescription": "This is an event",
                "location": 'Houston',
                "requiredSkills": "ms",
                "urgency": "low",
                "eventDate": "2024-07-08"
                }

        response = self.tester.get('/events/display.html', query_string=data)
        formatted_event_date = "".join(str(data['eventDate']).split('-'))
        command = f"SELECT user_id, event_id FROM event_details " \
                  f"WHERE event_name = \'{data['eventName']}\' AND description = \'{data['eventDescription']}\' AND " \
                  f"location = \'{data['location']}\' AND required_skills = \'{data['requiredSkills']}\' AND " \
                  f"urgency = \'{data['urgency']}\' AND event_date = date({formatted_event_date}::TEXT);"
        cursor.execute(command)
        table_data = cursor.fetchone()
        self.assertEqual(table_data[0], user_id)     # asserts that the event was stored in the db
        self.assertIn(str.encode("Event Details"), response.data)   # asserts that the event details page was displayed
        self.assertEqual(200, response.status_code)

        # need to remove this row from the db.
        # command = f"DELETE FROM event_details " \
        #           f"WHERE event_name = \'{data['eventName']}\' AND description = \'{data['eventDescription']}\' AND " \
        #           f"location = \'{data['location']}\' AND required_skills = \'{data['requiredSkills']}\' AND " \
        #           f"urgency = \'{data['urgency']}\' AND event_date = date({formatted_event_date}::TEXT);"

        command = (f"DELETE FROM event_details "
                   f"WHERE event_id = {table_data[1]};")
        cursor.execute(command)

        command = f"DELETE FROM usercredentials " \
                  f"WHERE id = {user_id};"
        cursor.execute(command)
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    unittest.main()
