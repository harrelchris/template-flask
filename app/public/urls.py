from flask import Blueprint

from . import views

bp = Blueprint(
    name="public",
    import_name=__name__,
    static_folder=None,
    template_folder=None,
    url_prefix="/",
)

bp.add_url_rule(
    rule="/",
    endpoint="index",
    view_func=views.index,
    methods=["GET"],
)
