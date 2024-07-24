from flask import Blueprint, render_template, jsonify, request, session
from .data import events, volunteers
import psycopg2
from .models import Volunteer, Event

matching_bp = Blueprint('matching', __name__)

# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")
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
    db_id = cursor.fetchone()
    print("user_profile table data (from volunteer matching):", db_id)
    cursor.close()

    return jsonify([volunteer.to_dict() for volunteer in volunteers])

@matching_bp.route('/api/events', methods=['GET'])
def get_events():
    cursor = conn.cursor()

    command = f"SELECT * FROM event_details;"

    cursor.execute(command)
    db_id = cursor.fetchone()
    print("event_details table data (from volunteer matching):", db_id)
    cursor.close()

    return jsonify([event.to_dict() for event in events])

@matching_bp.route('/api/assign_event', methods=['POST'])
def assign_event():
    data = request.get_json()
    volunteer_name = data.get('volunteer_name')
    event_name = data.get('event_name')
    # cursor = conn.cursor()

    # # get user_id using volunteer_name
    # command = f'''SELECT user_id FROM user_profile WHERE full_name = {volunteer_name};'''
    # cursor.execute(command)
    # user_id = cursor.fetchone()[0]
    #
    # # get event_id from event_name
    # command = f'''SELECT event_id FROM event_details WHERE event_name = {event_name}'''
    # cursor.execute(command)
    # event_id = cursor.fetchone()[0]
    #
    # # create a new record in history_db
    # command = f'''INSERT INTO volunteer_history(user_id, event_id) VALUES ({user_id}, {event_id});'''
    # cursor.execute(command)
    # cursor.close()
    # conn.commit()

    for volunteer in volunteers:
        if volunteer.name == volunteer_name:
            volunteer.assigned_event = event_name
            return jsonify({"message": f"Event '{event_name}' assigned to volunteer '{volunteer_name}'"}), 200

    return jsonify({"error": "Volunteer not found"}), 404



