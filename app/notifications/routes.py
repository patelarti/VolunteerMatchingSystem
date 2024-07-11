
from flask import Blueprint, render_template, jsonify

notifications_bp = Blueprint('notification', __name__)

@notifications_bp.route('/')
def notification():
    notifications = [
        "You have a new message",
        "Volunteer matched successfully",
        "Your event was approved",
        "Indicates a warning that might need attention",
        "Your event was approved",
        "Indicates a warning that might need attention",
        "Your event was approved",
        "Indicates a warning that might need attention"
    ]

    return render_template('../../templates/notification.html', notifications = notifications)
