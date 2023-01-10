from flask import Blueprint

from . import views

bp = Blueprint("user", __name__, url_prefix="/user", template_folder="templates")

bp.add_url_rule(
    rule="/register",
    endpoint="register",
    view_func=views.register,
    methods=["GET", "POST"],
)
bp.add_url_rule(
    rule="/login",
    endpoint="login",
    view_func=views.login,
    methods=["GET", "POST"],
)
bp.add_url_rule(
    rule="/logout",
    endpoint="logout",
    view_func=views.logout,
    methods=["GET"],
)
