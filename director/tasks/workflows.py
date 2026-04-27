import time

from celery.utils.log import get_task_logger
from celery import chain
from celery.utils import uuid


from director.extensions import cel
from director.models import StatusType
from director.models.workflows import Workflow
from director.models.tasks import Task


logger = get_task_logger(__name__)


@cel.task(name="celery.ping")
def ping():
    # type: () -> str
    """Simple task that just returns 'pong'."""
    pass


@cel.task()
def start(workflow_id):
    pass


@cel.task()
def end(workflow_id):
    # Waiting for the workflow status to be marked in error if a task failed
    pass


@cel.task()
def mark_as_canceled_pending_tasks(workflow_id):
    pass


@cel.task()
def failure_hooks_launcher(workflow_id, queue, tasks_names, payload):
    pass
