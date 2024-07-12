from flask import Blueprint, render_template, url_for, request, redirect

history_bp = Blueprint('history', __name__)

@history_bp.route('/', methods=['GET', 'POST'])
def volunteer_history():
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_history.html')
