from celery import chain, group
from celery.utils import uuid

from director.exceptions import WorkflowSyntaxError
from director.extensions import cel, cel_workflows
from director.models import StatusType
from director.models.tasks import Task
from director.models.workflows import Workflow
from director.tasks.workflows import start, end, failure_hooks_launcher


class WorkflowBuilder(object):
    def __init__(self, workflow_id):
        self.workflow_id = workflow_id
        self._workflow = None

        self.queue = cel_workflows.get_queue(str(self.workflow))
        self.custom_queues = {}

        self.tasks = cel_workflows.get_tasks(str(self.workflow))
        self.canvas = []

        self.failure_hook = cel_workflows.get_failure_hook_task(str(self.workflow))
        self.failure_hook_canvas = []

        self.success_hook = cel_workflows.get_success_hook_task(str(self.workflow))
        self.success_hook_canvas = []

        # Pointer to the previous task(s)
        self.previous = []

    @property
    def workflow(self):
        if not self._workflow:
            self._workflow = Workflow.query.filter_by(id=self.workflow_id).first()
        return self._workflow

    def new_task(self, task_name, is_hook, single=True):
        pass

    def parse_queues(self):
        pass

    def parse(self, tasks, is_hook=False):
        pass

    def build(self):
        pass

    def build_hooks(self):
        pass

    def run(self):
        pass

    def cancel(self):
        pass
