import logging

from sqlalchemy.orm import load_only

from director.builder import WorkflowBuilder
from director.extensions import cel, db
from director.models.workflows import Workflow

logger = logging.getLogger()


@cel.task()
def execute(workflow, payload):
    pass


@cel.task()
def cleanup(retentions):
    pass
