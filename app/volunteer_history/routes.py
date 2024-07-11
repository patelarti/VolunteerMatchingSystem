from flask import render_template, request, jsonify
from app.volunteer_history import history_bp

@history_bp.route('/history', methods=['GET', 'POST'])
def volunteer_history():
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_history.html')
