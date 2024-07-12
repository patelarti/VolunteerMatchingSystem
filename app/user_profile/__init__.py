from flask import Blueprint

profile_bp = Blueprint('profile_bp', __name__)

from app.user_profile import routes
