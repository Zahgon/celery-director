import click
import json
from json.decoder import JSONDecodeError
from terminaltables import AsciiTable
import uuid

from flask_json_schema import JsonValidationError

from director.builder import WorkflowBuilder
from director.context import pass_ctx
from director.exceptions import WorkflowNotFound
from director.extensions import cel_workflows
from director.models.workflows import Workflow
from director.utils import validate, format_schema_errors, build_celery_schedule


def tasks_to_ascii(tasks, hooks):
    pass


@click.group()
def workflow():
    """Manage the workflows"""


@workflow.command(name="list")
@pass_ctx
def list_workflow(ctx):
    """List the workflows"""
    pass


@workflow.command(name="show")
@click.argument("name")
@pass_ctx
def show_workflow(ctx, name):
    """Display details of a workflow"""
    pass


@workflow.command(name="run")
@click.argument("fullname")
@click.argument("payload", required=False, default="{}")
@click.option("--comment", help="A comment for the workflow instance.")
@pass_ctx
def run_workflow(ctx, fullname, payload, comment):
    """Execute a workflow"""
    pass


@workflow.command(name="cancel")
@click.argument("id")
@pass_ctx
def cancel_workflow(ctx, id):
    """Cancel a workflow"""
    pass


@workflow.command(name="relaunch")
@click.argument("id")
@pass_ctx
def relaunch_workflow(ctx, id):
    """Relaunch a workflow"""
    pass
