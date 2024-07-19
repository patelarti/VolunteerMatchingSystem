from flask import Blueprint

profile_bp = Blueprint('profile', __name__)

from app.user_profile import routes
