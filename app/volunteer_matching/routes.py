from flask import render_template, request, jsonify
from app.volunteer_matching import matching_bp

@matching_bp.route('/matching', methods=['GET', 'POST'])
def volunteer_matching():
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_matching.html')
