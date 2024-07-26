from flask import Blueprint, render_template, session, request
import psycopg2

notifications_bp = Blueprint('notification', __name__)

# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")


def get_notification():
    command = ""
    if session["is_admin"]:
        command = f"SELECT msg FROM notifications " \
                  f"WHERE notification_type = {True} OR user_id = {session['user_id']};"
    else:
        command = f"SELECT msg FROM notifications " \
                  f"WHERE notification_type = {False} AND user_id = {session['user_id']};"

    cursor = conn.cursor()
    cursor.execute(command)
    table_data = cursor.fetchall()
    cursor.close()

    return [notif[0] for notif in table_data]


@notifications_bp.route('/', methods=['GET'])
def notification():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")

    return render_template('notification.html', notifications=get_notification(), username=session['username'])


@notifications_bp.route('/delete', methods=['GET', 'POST'])
def notification_delete():
    if request.method == 'POST':
        data = request.get_json()
        notification = data['notification_name'].split('\n')[-2].strip()

        cursor = conn.cursor()
        command = f"DELETE FROM notifications WHERE msg LIKE '%{notification}%';"
        cursor.execute(command)
        cursor.close()
        conn.commit()

        return render_template('notification.html', notifications=get_notification(), username=session['username'])
