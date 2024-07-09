
from flask import Blueprint, render_template

matching_bp = Blueprint('matching', __name__)

@matching_bp.route('/')
def notification():
    return render_template('volunteer_matching.html')