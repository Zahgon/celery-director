import os
import click


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--dev", "dev_mode", default=False, is_flag=True, type=bool)
@click.argument("web_args", nargs=-1, type=click.UNPROCESSED)
def webserver(dev_mode, web_args):
    """Start the webserver instance"""
    pass
