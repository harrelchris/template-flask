from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import current_user

from app.database import session
from app.user.models import User


def has_admin_access() -> bool:
    if current_user.is_anonymous:
        return False
    return current_user.is_admin


class SecureAdminIndexView(AdminIndexView):
    def is_visible(self):
        """Remove duplicate 'Admin Home' link from nav"""

        return False

    @expose("/")
    def index(self):
        """Conditionally grant access to admin interface"""

        if has_admin_access():
            return self.render(self._template)
        else:
            return redirect(url_for("public.index"))


class PublicSiteLink(MenuLink):
    """Menu link leading to public index."""

    def get_url(self):
        return url_for("public.index")


class SecuredModelView(ModelView):
    def is_accessible(self):
        return has_admin_access()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("public.index"))


class CustomModelView(SecuredModelView):
    """See flask_admin.model.BaseModelView for permission and customization options"""

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = False
    can_export = False


admin = Admin(index_view=SecureAdminIndexView(name="Admin Home"))
admin.add_link(PublicSiteLink(name="Public Site"))

admin.add_view(
    CustomModelView(
        model=User,
        session=session,
        name="Users",
        endpoint="users",
        category=None,
    ),
)
