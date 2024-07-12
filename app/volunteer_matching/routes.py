<<<<<<< HEAD
from flask import Blueprint, render_template, jsonify, request
from .data import events, volunteers
from .models import Volunteer, Event

matching_bp = Blueprint('matching', __name__)

@matching_bp.route('/', methods=['GET'])
def volunteer_matching():
    return render_template('volunteer_matching.html')

@matching_bp.route('/api/volunteers', methods=['GET'])
def get_volunteers():
    return jsonify([volunteer.to_dict() for volunteer in volunteers])

@matching_bp.route('/api/events', methods=['GET'])
def get_events():
    return jsonify([event.to_dict() for event in events])

@matching_bp.route('/api/assign_event', methods=['POST'])
def assign_event():
    data = request.get_json()
    volunteer_name = data.get('volunteer_name')
    event_name = data.get('event_name')

    for volunteer in volunteers:
        if volunteer.name == volunteer_name:
            volunteer.assigned_event = event_name
            return jsonify({"message": f"Event '{event_name}' assigned to volunteer '{volunteer_name}'"}), 200

    return jsonify({"error": "Volunteer not found"}), 404
=======
from flask import Blueprint, render_template, url_for, request, redirect

matching_bp = Blueprint('matching', __name__)

@matching_bp.route('/', methods=['GET', 'POST'])
def volunteer_matching():
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_matching.html')
>>>>>>> ee5031843ca527ec37135e8b27494f9d64205578
