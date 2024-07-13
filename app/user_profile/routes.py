from flask import render_template, request, jsonify, session
from app.user_profile import profile_bp
import bcrypt
from app.auth.routes import testUsers  # Assuming testUsers is defined in app.auth.routes

@profile_bp.route('/', methods=['GET', 'POST'])
def profile():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        full_name = data.get('fullName')
        dob = data.get('dob')
        address1 = data.get('address1')
        address2 = data.get('address2')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        skills = data.get('skills')
        preferences = data.get('preferences')
        availability = data.get('availability')

        user = next((user for user in testUsers if user['email'] == email), None)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        user.update({
            'fullName': full_name,
            'dob': dob,
            'address1': address1,
            'address2': address2,
            'city': city,
            'state': state,
            'zip': zip_code,
            'skills': skills,
            'preferences': preferences,
            'availability': availability
        })

        return jsonify({'message': 'Profile updated successfully'})

    return render_template('profile.html')
