import imp
import json
from pathlib import Path
from json.decoder import JSONDecodeError

import yaml
import sentry_sdk
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_json_schema import JsonSchema, JsonValidationError
from flask_migrate import Migrate
from pluginbase import PluginBase
from sqlalchemy.schema import MetaData
from sentry_sdk.integrations import celery as sentry_celery
from sentry_sdk.utils import capture_internal_exceptions
from celery.exceptions import SoftTimeLimitExceeded

from director.exceptions import SchemaNotFound, SchemaNotValid, WorkflowNotFound


class CeleryWorkflow:
    def __init__(self):
        self.app = None
        self.workflows = None

    def init_app(self, app):
        pass

    def get_by_name(self, name):
        pass

    def get_tasks(self, name):
        pass

    def get_hook_task(self, name, hook_name):
        pass

    def get_failure_hook_task(self, name):
        pass

    def get_success_hook_task(self, name):
        pass

    def get_queue(self, name):
        pass

    def import_user_tasks(self):
        pass

    def read_schemas(self):
        pass


# Celery Extension
class FlaskCelery(Celery):
    def __init__(self, *args, **kwargs):
        kwargs["include"] = ["director.tasks"]
        super(FlaskCelery, self).__init__(*args, **kwargs)

        if "app" in kwargs:
            self.init_app(kwargs["app"])

    def init_app(self, app):
        pass


# Sentry Extension
class DirectorSentry:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        pass

    def enrich_tags(self, tags, workflow_id, task):
        pass

    def enrich_extra(self, extra, args, kwargs):
        pass

    def custom_event_processor(self, task, uuid, args, kwargs, request=None):
        """
        This function is the same as the original, except that we
        add custom tags and extras about the workflow object.

        Published under a BSD-2 license and available at:
        https://github.com/getsentry/sentry-python/blob/0.16.3/sentry_sdk/integrations/celery.py#L176
        """
        pass


# List of extensions
db = SQLAlchemy(
    metadata=MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(column_0_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
)
migrate = Migrate()
schema = JsonSchema()
cel = FlaskCelery("director")
cel_workflows = CeleryWorkflow()
sentry = DirectorSentry()
