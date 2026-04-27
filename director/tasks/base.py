from celery import Task as _Task
from celery.signals import after_task_publish, task_prerun, task_postrun
from celery.utils.log import get_task_logger

from director.extensions import cel, db
from director.models import StatusType
from director.models.workflows import Workflow
from director.models.tasks import Task


logger = get_task_logger(__name__)


@task_prerun.connect
def director_prerun(task_id, task, *args, **kwargs):
    pass


@task_postrun.connect
def close_session(*args, **kwargs):
    # Flask SQLAlchemy will automatically create new sessions for you from
    # a scoped session factory, given that we are maintaining the same app
    # context, this ensures tasks have a fresh session (e.g. session errors
    # won't propagate across tasks)
    pass


class BaseTask(_Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        pass
