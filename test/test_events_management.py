import unittest
import sys

sys.path.append("../VolunteerMatch")
from run import app
from flask import jsonify

class EventManagementTest(unittest.TestCase):
    def test_event_management_signed_in_false(self):
        tester = app.test_client(self)
        with tester.session_transaction() as sess:
            sess['signed_in'] = False

            response = tester.get('/events/')
            self.assertEqual(response.status_code, 200)

    def test_event_management_signed_in_true(self):
        tester = app.test_client(self)

        with tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'

        response = tester.get('/events/')
        self.assertEqual(response.status_code, 200)

    def test_display_signed_in_false(self):
        tester = app.test_client(self)
        with tester.session_transaction() as sess:
            sess['signed_in'] = False

            response = tester.get('/events/display.html')
            self.assertEqual(response.status_code, 200)

    def test_display_signed_in_true(self):
        tester = app.test_client(self)

        with tester.session_transaction() as sess:
            sess['signed_in'] = True
            sess['email'] = 'patelarti91@gmail.com'
        data = {"eventName": "My Event",
                "eventDescription": "This is an event",
                "location":'Houston',
                "requiredSkills": "ms",
                "urgency":"low",
                "eventDate":"7-13-2024"
                }
        response = tester.get('/events/display.html', data=data)
        self.assertEqual(response.status_code, 200)




if __name__ == "__main__":
    unittest.main()
