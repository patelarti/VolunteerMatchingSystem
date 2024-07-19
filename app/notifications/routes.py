
from flask import Blueprint, render_template, jsonify, session

notifications_bp = Blueprint('notification', __name__)

@notifications_bp.route('/', methods=['GET'])
def notification():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    notifications = [
        "You have a new message",
        "Volunteer matched successfully",
        "Your event was approved",
        "Event ABC might need your attention",
        "Your event was cancelled",
        "Event XYZ might need your attention",
    ]

    return render_template('notification.html', notifications = notifications, username = session['username'])
