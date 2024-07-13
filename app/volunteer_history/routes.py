from flask import Blueprint, render_template, url_for, request, redirect, session

history_bp = Blueprint('history', __name__)

@history_bp.route('/', methods=['GET', 'POST'])
def volunteer_history():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_history.html')
