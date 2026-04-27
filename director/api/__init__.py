from flask import jsonify, Blueprint
from flask_json_schema import JsonValidationError

from director.utils import validate, format_schema_errors


# Main application
api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.errorhandler(JsonValidationError)
def schema_exception_handler(e):
    pass


@api_bp.route("/ping")
def ping():
    pass
