# noinspection PyInterpreter
from flask import Blueprint, render_template, jsonify, request, session
import psycopg2
from .models import Volunteer, Event

matching_bp = Blueprint('matching', __name__)

# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")

events = []
volunteers = []
@matching_bp.route('/', methods=['GET'])
def volunteer_matching():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")

    return render_template('volunteer_matching.html', username=session['username'])


@matching_bp.route('/api/volunteers', methods=['GET'])
def get_volunteers():
    cursor = conn.cursor()

    command = f"SELECT * FROM user_profile;"

    cursor.execute(command)
    table_data = cursor.fetchall()
    # print("user_profile table data (from volunteer matching):", table_data)
    # cursor.close()

    # create Volunteer objects and store in volunteer list
    for row in table_data:
        # fetch this user's email
        command = f"SELECT email FROM usercredentials WHERE id = {row[0]};"
        cursor.execute(command)
        email = cursor.fetchone()[0]

        # in the same session, it adds the volunteers as many times as you refresh, hence this check.
        exists = False
        record_idx = -1
        for volunteer in volunteers:
            record_idx += 1
            # print(f"vol.email => {volunteer.to_dict()['email']}, email => {email}, equality => {volunteer.to_dict()['email'] == email}")
            # this is O(n). Can we improve this?
            # volunteer below is a new object hence "if volunteer in volunteers" isn't working.
            if volunteer.to_dict()['email'] == email:
                exists = True
                break

        # Fetch volunteer's history.
        command = f"SELECT event_id FROM volunteer_history WHERE user_id = {row[0]};"
        cursor.execute(command)
        history = []
        table_data = cursor.fetchall()

        for hist in table_data:
            history.append({"event_id": hist[0], "status": "Incomplete"})
        # End volunteer history

        formatted_skills = row[7].split(',')
        volunteer = Volunteer(
            name=row[1],
            address1=row[2],
            address2=row[3],
            city=row[4],
            state=row[5],
            zip=row[6],
            skills=formatted_skills,
            preferences=row[8],
            availability=[row[9]],
            email=email,
            phone="PHONE DUMMY DATA",
            history=history
        )
        if exists:
            # the history may have been updated, hence replace
            volunteers[record_idx] = volunteer
        else:
            volunteers.append(volunteer)
    cursor.close()
    # for volunteer in volunteers:
    #     print(volunteer.to_dict())

    return jsonify([volunteer.to_dict() for volunteer in volunteers])


@matching_bp.route('/api/events', methods=['GET'])
def get_events():
    cursor = conn.cursor()

    command = f"SELECT * FROM event_details;"

    cursor.execute(command)
    table_data = cursor.fetchall()
    print("event_details table data (from volunteer matching):", table_data)
    cursor.close()

    # create Event objects and store in event list
    for row in table_data:
        # in the same session, it adds the events as many times as you refresh, hence this check.
        exists = False
        for event in events:
            if event.to_dict()['id'] == row[0]:
                exists = True
                break

        if exists:
            continue

        formatted_required_skills = row[4].split(",")
        event = Event(
            name=row[1],
            description=row[2],
            location=row[3],
            required_skills=formatted_required_skills,
            urgency=row[5],
            date=row[6],
            id=row[0],
        )
        events.append(event)

    return jsonify([event.to_dict() for event in events])


@matching_bp.route('/api/assign_event', methods=['POST'])
def assign_event():
    data = request.get_json()
    volunteer_name = data.get('volunteer_name')
    event_name = data.get('event_name')
    cursor = conn.cursor()

    # volunteer_name_db = 'Arti Patel'
    # get user_id using volunteer_name
    command = f'''SELECT user_id FROM user_profile WHERE full_name = '{volunteer_name}';'''
    cursor.execute(command)
    user_id = cursor.fetchone()[0]

    # event_name_db = 'Hiking'
    # get event_id from event_name
    command = f'''SELECT event_id, event_date FROM event_details WHERE event_name = '{event_name}';'''
    cursor.execute(command)
    table_data = cursor.fetchone()
    event_id = table_data[0]
    event_date = table_data[1]

    # print(f"user_id = {user_id}, event_id = {event_id}")

    # create a new record in history_db
    command = f'''INSERT INTO volunteer_history(user_id, event_id) VALUES ('{user_id}', '{event_id}');'''
    cursor.execute(command)

    command = (f"INSERT INTO notifications (user_id, msg, notification_type) "
               f"VALUES ({user_id}, 'You have been assigned the event {event_name} on {event_date}', {False});")
    cursor.execute(command)

    cursor.close()
    conn.commit()

    # we will have already created Volunteer and Event objects and stored them. Simply check them here.
    for volunteer in volunteers:
        if volunteer.name == volunteer_name:
            volunteer.assigned_event = event_name
            return jsonify({"message": f"Event '{event_name}' assigned to volunteer '{volunteer_name}'"}), 200

    return jsonify({"error": "Volunteer not found"}), 404
