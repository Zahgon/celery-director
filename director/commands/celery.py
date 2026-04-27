import os
import click

from urllib.parse import urlparse

from director.context import pass_ctx


@click.group()
def celery():
    """Celery commands"""
    pass


@celery.command(name="beat", context_settings=dict(ignore_unknown_options=True))
@click.option("--dev", "dev_mode", default=False, is_flag=True, type=bool)
@click.argument("beat_args", nargs=-1, type=click.UNPROCESSED)
def beat(dev_mode, beat_args):
    """Start the beat instance"""
    pass


@celery.command("worker", context_settings=dict(ignore_unknown_options=True))
@click.option("--dev", "dev_mode", default=False, is_flag=True, type=bool)
@click.argument("worker_args", nargs=-1, type=click.UNPROCESSED)
def worker(dev_mode, worker_args):
    """Start a Celery worker instance"""
    pass


@celery.command(name="flower", context_settings=dict(ignore_unknown_options=True))
@click.argument("flower_args", nargs=-1, type=click.UNPROCESSED)
@pass_ctx
def flower(ctx, flower_args):
    """Start the flower instance"""
    pass
