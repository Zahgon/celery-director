from flask import current_app as app
from flask import jsonify, abort
from flask_httpauth import HTTPBasicAuth

from director.models.users import User

from werkzeug.security import check_password_hash

ANONYMOUS_USERNAME = "anonymous"

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    # no need to check if auth is disabled
    pass


@auth.error_handler
def unauthorized():
    pass
