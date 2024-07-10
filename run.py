from flask import Flask
from app.auth.routes import auth_bp
from app.user_profile.routes import profile_bp
from app.events_management.routes import events_bp
from app.volunteer_matching.routes import matching_bp
from app.notifications.routes import notifications_bp
from app.volunteer_history.routes import history_bp

app = Flask(__name__)

# app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(matching_bp, url_prefix='/matching')
app.register_blueprint(notifications_bp, url_prefix='/notifications')
app.register_blueprint(history_bp, url_prefix='/history')

if __name__ == '__main__':
    app.run(debug=True)