from werkzeug.security import generate_password_hash
from terminaltables import AsciiTable


from director.context import pass_ctx
from director.exceptions import UserNotFound
from director.models.users import User

import click


def _get_users():
    pass


@click.group()
def user():
    """Manage the users"""


@user.command(name="list")
@pass_ctx
def list_users(ctx):
    """Display users"""
    pass


@user.command(name="create")
@click.argument("username")
@click.password_option()
@pass_ctx
def create_user(ctx, username, password):
    """Create user"""
    pass


@user.command(name="update")
@click.argument("username")
@click.password_option()
@pass_ctx
def update_user(ctx, username, password):
    """Update user"""
    pass


@user.command(name="delete")
@click.argument("username")
@pass_ctx
def delete_user(ctx, username):
    """delete user"""
    pass
