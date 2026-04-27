from datetime import datetime, timedelta
from distutils.util import strtobool

import pytz
from flask import abort, jsonify, request
from flask import current_app as app

from director.api import api_bp, validate
from director.auth import auth
from director.builder import WorkflowBuilder
from director.exceptions import WorkflowNotFound
from director.extensions import cel_workflows, schema
from director.models.workflows import Workflow
from director.utils import build_celery_schedule


def _get_workflow(workflow_id):
    pass


def _execute_workflow(project, name, payload={}, comment=None):
    pass


def _cancel_workflow(obj):
    pass


@api_bp.route("/workflows", methods=["POST"])
@auth.login_required
@schema.validate(
    {
        "required": ["project", "name", "payload"],
        "additionalProperties": False,
        "properties": {
            "project": {"type": "string"},
            "name": {"type": "string"},
            "payload": {"type": "object"},
            "comment": {"type": "string"},
        },
    }
)
def create_workflow():
    pass


@api_bp.route("/workflows/<workflow_id>/relaunch", methods=["POST"])
@auth.login_required
def relaunch_workflow(workflow_id):
    pass


@api_bp.route("/workflows/<workflow_id>/cancel", methods=["POST"])
@auth.login_required
def cancel_workflow(workflow_id):
    pass


@api_bp.route("/workflows")
@auth.login_required
def list_workflows():
    pass


@api_bp.route("/workflows/<workflow_id>")
@auth.login_required
def get_workflow(workflow_id):
    pass


@api_bp.route("/definitions")
@auth.login_required
def list_definitions():
    pass
