class Volunteer:
    def __init__(self, name, address1, address2, city, state, zip, skills, preferences, availability, email, phone, assigned_event="", history=None):
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.skills = skills
        self.preferences = preferences
        self.availability = availability
        self.email = email
        self.phone = phone
        self.assigned_event = assigned_event
        self.history = history if history is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "skills": self.skills,
            "preferences": self.preferences,
            "availability": self.availability,
            "email": self.email,
            "phone": self.phone,
            "assigned_event": self.assigned_event,
            "history": self.history
        }

class Event:
    def __init__(self, name, description, location, required_skills, urgency, date, id):
        self.name = name
        self.description = description
        self.location = location
        self.required_skills = required_skills
        self.urgency = urgency
        self.date = date
        self.id = id

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "required_skills": self.required_skills,
            "urgency": self.urgency,
            "date": self.date,
            "id": self.id
        }
