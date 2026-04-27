from flask_json_schema import JsonValidationError
from jsonschema.validators import validator_for
from celery.schedules import crontab

from director.exceptions import WorkflowSyntaxError


def validate(payload, schema):
    """Validate a payload according to a given schema"""
    validator_cls = validator_for(schema)
    validator = validator_cls(schema=schema)
    errors = list(validator.iter_errors(payload))
    if errors:
        raise JsonValidationError("Payload is not valid", errors)


def format_schema_errors(e):
    """Format FlaskJsonSchema validation errors"""
    return {
        "error": e.message,
        "errors": [validation_err.message for validation_err in e.errors],
    }


def build_celery_schedule(workflow_name, data):
    """A celery schedule can accept seconds or crontab"""

    def _handle_schedule(schedule):
        pass

    def _handle_crontab(ct):
        pass

    excluded_keys = ["payload"]
    keys = [k for k in data.keys() if k not in excluded_keys]

    schedule_functions = {
        # Legacy syntax for backward compatibility
        "schedule": _handle_schedule,
        # Current syntax
        "crontab": _handle_crontab,
        "interval": float,
    }

    if len(keys) != 1 or keys[0] not in schedule_functions.keys():
        # When there is no key (schedule, interval, crontab) in the periodic configuration
        raise WorkflowSyntaxError(workflow_name)

    schedule_key = keys[0]
    schedule_input = data[schedule_key]
    try:
        # Apply the function mapped to the schedule type
        return str(schedule_input), schedule_functions[schedule_key](schedule_input)
    except Exception:
        raise WorkflowSyntaxError(workflow_name)
