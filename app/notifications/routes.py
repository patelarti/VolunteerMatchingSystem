from flask import Blueprint, render_template, jsonify, session
import psycopg2

notifications_bp = Blueprint('notification', __name__)

# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")

@notifications_bp.route('/', methods=['GET'])
def notification():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")

    command = ""
    if session["is_admin"]:
        command = "SELECT msg FROM notifications "\
                   f"WHERE notification_type = {True};"
    else:
        command = ("SELECT msg FROM notifications "
                   f"WHERE notification_type = {False} and user_id = {session['user_id']};")
    cursor = conn.cursor()
    cursor.execute(command)
    table_data = cursor.fetchall()
    print(session["is_admin"])
    print(table_data)
    cursor.close()
    #
    # print(f"tabledata => {table_data}")

    notifications = [notif[0] for notif in table_data]

    #
    # notifications = [
    #     "You have a new message",
    #     "Volunteer matched successfully",
    #     "Your event was approved",
    #     "Event ABC might need your attention",
    #     "Your event was cancelled",
    #     "Event XYZ might need your attention",
    # ]

    return render_template('notification.html', notifications = notifications, username = session['username'])
