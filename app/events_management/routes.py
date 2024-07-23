
from flask import Blueprint, render_template, url_for, request, redirect, session
import psycopg2

events_bp = Blueprint('events', __name__)


# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")


@events_bp.route('/', methods=['POST', 'GET'])
def event_management_form():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    return render_template('event_management.html', email=session['email'], username=session['username'])
@events_bp.route('/display.html', methods=['GET'])
def display_event():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    # Retrieve query parameters
    event_name = request.args.get('eventName')
    event_description = request.args.get('eventDescription')
    event_location = request.args.get('location')
    required_skills = request.args.getlist('requiredSkills')  # handle multiple values
    urgency = request.args.get('urgency')
    event_date = request.args.get('eventDate')

    formatted_required_skills = ""
    for skill in required_skills:
        formatted_required_skills += skill + ","

    formatted_event_date = "".join(str(event_date).split('-'))
    print(formatted_event_date)
    # print("required_skills==>", str(required_skills))
    cursor = conn.cursor()

    command = f'''INSERT INTO event_details(
                    event_name, description, location, required_skills, urgency, event_date, user_id)
                    VALUES('{event_name}','{event_description}','{event_location}','{formatted_required_skills}','{urgency}',date({formatted_event_date}::TEXT),{session["user_id"]});'''

    cursor.execute(command)
    # db_password = cursor.fetchone()
    cursor.close()
    conn.commit()


    # For demonstration, print the values
    print(f"Event Name: {event_name}")
    print(f"Event Description: {event_description}")
    print(f"Event Location: {event_location}")
    print(f"Required Skills: {required_skills}")
    print(f"Urgency: {urgency}")
    print(f"Event Date: {event_date}")

    # Pass the values to the template
    return render_template('display.html',
                           event_name=event_name,
                           event_description=event_description,
                           event_location=event_location,
                           required_skills=required_skills,
                           urgency=urgency,
                           event_date=event_date,
                           username=session['username'])
