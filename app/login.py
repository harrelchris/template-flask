from flask_login import LoginManager

from app.user.models import User

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "error"


@login_manager.user_loader
def load_user(user_id):
    return User.find(int(user_id))
