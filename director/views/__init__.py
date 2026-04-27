from uuid import UUID

from flask import Blueprint, abort, render_template


view_bp = Blueprint("views", __name__, url_prefix="/")


@view_bp.route("/")
def home():
    pass


@view_bp.route("/<id>")
def get_workflow(id):
    pass


@view_bp.app_template_filter("status")
def status(code):
    pass
