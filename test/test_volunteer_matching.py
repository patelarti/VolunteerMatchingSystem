import unittest
import sys
sys.path.append("../VolunteerMatch")
from run import app
from app.volunteer_matching.data import events, volunteers
from flask import jsonify

class VolunteerMatchingTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_get_volunteers_gets_back_volunteer_dict(self):
        response = self.tester.get('/matching/api/volunteers')
        volunteer_dict = [volunteer.to_dict() for volunteer in volunteers]
        self.assertEqual(response.json, volunteer_dict)

    def test_get_volunteers_gets_back_events_dict(self):
        response = self.tester.get('/matching/api/events')
        events_dict = [event.to_dict() for event in events]
        self.assertEqual(response.json, events_dict)

    def test_assign_event_with_volunteer_not_found(self):
        data = {
            "volunteer_name": "Arti",
            "event_name": "abcd"
        }
        response = self.tester.post('/matching/api/assign_event', json=data)
        val = '{"error":"Volunteer not found"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(404, response.status_code)

    def test_assign_event_with_volunteer_found(self):
        data = {
            "volunteer_name": "Alice Johnson",
            "event_name": "Youth Mentoring"
        }
        response = self.tester.post('/matching/api/assign_event', json=data)
        val = '{"message":"Event \'Youth Mentoring\' assigned to volunteer \'Alice Johnson\'"}\n'
        self.assertEqual(str.encode(val), response.data)
        self.assertEqual(200, response.status_code)



if __name__ == "__main__":
    unittest.main()


