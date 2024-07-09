
from flask import Blueprint, render_template

history_bp = Blueprint('history', __name__)

@history_bp.route('/')
def notification():
    return render_template('volunteer_history.html')