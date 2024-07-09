
from flask import Blueprint, render_template

events_bp = Blueprint('events', __name__)

@events_bp.route('/')
def notification():
    return render_template('event_management.html')