# app/volunteer_matching/data.py
from .models import Volunteer, Event

# events = [
#     Event(
#         name="Community Cleanup",
#         description="Join us for a community-wide cleanup event to help keep our neighborhood beautiful. Volunteers will pick up litter, plant trees, and more.",
#         location="Central Park, Main Street",
#         required_skills=["Environmental Awareness", "Physical Fitness", "Teamwork"],
#         urgency="Medium",
#         date="2023-07-10",
#         id=1
#     ),
#     Event(
#         name="Charity Run",
#         description="A charity run to raise funds for local schools. Volunteers are needed to help with registration, handing out water, and cheering on participants.",
#         location="Riverfront Park, Riverside Drive",
#         required_skills=["Event Planning", "Public Speaking", "First Aid"],
#         urgency="High",
#         date="2023-08-15",
#         id =2
#
#     ),
#     Event(
#         name="Food Drive",
#         description="Help us organize and distribute food to families in need. Volunteers will sort donations, pack food boxes, and assist with distribution.",
#         location="Community Center, 5th Avenue",
#         required_skills=["Organization", "Customer Service", "Lifting"],
#         urgency="Low",
#         date="2023-09-01",
#         id = 3
#     ),
#     Event(
#         name="Senior Care Visit",
#         description="Spend time with seniors at the local nursing home. Volunteers will engage in activities, assist with meals, and provide companionship.",
#         location="Sunset Nursing Home, Oak Street",
#         required_skills=["Compassion", "Patience", "Communication"],
#         urgency="Medium",
#         date="2023-10-05",
#         id = 4
#
#     ),
#     Event(
#         name="Youth Mentoring",
#         description="Mentor at-risk youth and help them develop essential life skills. Volunteers will participate in one-on-one mentoring and group activities.",
#         location="Youth Center, Elm Street",
#         required_skills=["Mentoring", "Active Listening", "Conflict Resolution"],
#         urgency="High",
#         date="2023-11-20",
#         id = 5
#     ),
#     Event(
#         name="Holiday Toy Drive",
#         description="Collect and distribute toys to children in need during the holiday season. Volunteers will organize toy donations and assist with gift wrapping.",
#         location="Community Hall, Maple Avenue",
#         required_skills=["Organization", "Creativity", "Customer Service"],
#         urgency="Medium",
#         date="2023-12-15",
#         id = 6
#     )
# ]
#
# volunteers = [
#     Volunteer(
#         name="Alice Johnson",
#         address1="123 Main Street",
#         address2="Apt 4B",
#         city="Springfield",
#         state="IL",
#         zip="62704",
#         skills=["Event Planning", "Fundraising"],
#         preferences="I prefer weekend events.",
#         availability=["2023-07-10", "2023-07-11", "2023-07-17"],
#         email="alice@example.com",
#         phone="123-456-7890",
#         assigned_event="",
#         history=[{"event_id": 1, "status": "Completed"}, {"event_id": 2, "status": "Completed"}]
#
#
#     ),
#     Volunteer(
#         name="Bob Smith",
#         address1="456 Elm Street",
#         address2="",
#         city="Riverside",
#         state="CA",
#         zip="92501",
#         skills=["Social Media", "Graphic Design"],
#         preferences="No preferences.",
#         availability=["2023-08-15", "2023-08-20", "2023-08-25"],
#         email="bob@example.com",
#         phone="123-456-7891",
#         assigned_event="Charity Run",
#                 history=[{"event_id": 3, "status": "Completed"}, {"event_id": 2, "status": "Completed"}]
#
#     ),
#     Volunteer(
#         name="Carol Williams",
#         address1="789 Oak Avenue",
#         address2="Suite 100",
#         city="Hometown",
#         state="TX",
#         zip="75001",
#         skills=["Writing", "Translation"],
#         preferences="Prefer morning shifts.",
#         availability=["2023-09-01", "2023-09-03", "2023-09-10"],
#         email="carol@example.com",
#         phone="123-456-7892",
#         assigned_event="",
#                         history=[{"event_id": 5, "status": "Completed"}, {"event_id": 1, "status": "Completed"}]
#
#     ),
#     Volunteer(
#         name="David Brown",
#         address1="321 Maple Drive",
#         address2="",
#         city="Greenville",
#         state="SC",
#         zip="29601",
#         skills=["Customer Service", "Lifting"],
#         preferences="Prefer events that are physically demanding.",
#         availability=["2023-10-05", "2023-10-12", "2023-10-19"],
#         email="david@example.com",
#         phone="123-456-7893",
#         assigned_event=""
#     ),
#     Volunteer(
#         name="Emily Clark",
#         address1="654 Pine Lane",
#         address2="",
#         city="Fairview",
#         state="TN",
#         zip="37062",
#         skills=["Mentoring", "Active Listening"],
#         preferences="Prefer working with youth.",
#         availability=["2023-11-20", "2023-11-25", "2023-11-30"],
#         email="emily@example.com",
#         phone="123-456-7894",
#         assigned_event="Youth Mentoring"
#     ),
#     Volunteer(
#         name="Franklin Green",
#         address1="987 Cedar Court",
#         address2="Floor 2",
#         city="Westfield",
#         state="MA",
#         zip="01085",
#         skills=["Organization", "Creativity"],
#         preferences="I like to work on holiday-related events.",
#         availability=["2023-12-15", "2023-12-20", "2023-12-25"],
#         email="franklin@example.com",
#         phone="123-456-7895",
#         assigned_event="Holiday Toy Drive"
#     )
# ]
