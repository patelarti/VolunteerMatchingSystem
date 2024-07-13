
from flask import Blueprint, render_template, jsonify, session

notifications_bp = Blueprint('notification', __name__)

@notifications_bp.route('/')
def notification():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
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

    return render_template('notification.html', notifications = notifications)
