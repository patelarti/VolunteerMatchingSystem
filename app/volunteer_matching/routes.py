from flask import Blueprint, render_template, url_for, request, redirect

matching_bp = Blueprint('matching', __name__)

@matching_bp.route('/', methods=['GET', 'POST'])
def volunteer_matching():
    if request.method == 'POST':
        # Handle POST request
        pass
    return render_template('volunteer_matching.html')
