import click

from app.user.crypto import hash_password
from app.user.models import User


@click.group()
def user():
    """Commands for the User package"""


@user.command()
@click.argument("username")
@click.argument("password")
def default(username, password):
    """Create a default user"""

    hashed = hash_password(password)
    default_user = User(
        username=username,
        password=hashed,
        is_admin=False,
    )
    default_user.save()


@user.command()
@click.argument("username")
@click.argument("password")
def admin(username, password):
    """Create an admin user"""

    hashed = hash_password(password)
    admin_user = User(
        username=username,
        password=hashed,
        is_admin=True,
    )
    admin_user.save()
