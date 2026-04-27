from flask_json_schema import JsonValidationError
from jsonschema.validators import validator_for
from celery.schedules import crontab

from director.exceptions import WorkflowSyntaxError


def validate(payload, schema):
    """Validate a payload according to a given schema"""
    pass


def format_schema_errors(e):
    """Format FlaskJsonSchema validation errors"""
    pass


def build_celery_schedule(workflow_name, data):
    """A celery schedule can accept seconds or crontab"""

    pass
