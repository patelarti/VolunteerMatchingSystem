
from flask import Blueprint, render_template

notifications_bp = Blueprint('notification', __name__)

@notifications_bp.route('/')
def notification():
    return render_template('notification.html')