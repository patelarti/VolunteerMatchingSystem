import unittest
import sys

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
        with self.tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
            sess['username'] = sess['email'].split('@')[0]

        data = {"eventName": "My Event",
                "eventDescription": "This is an event",
                "location": 'Houston',
                "requiredSkills": "ms",
                "urgency": "low",
                "eventDate": "2024-07-08"
                }

        response = self.tester.get('/events/display.html', query_string=data)
        self.assertIn(str.encode("Event Details"), response.data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
