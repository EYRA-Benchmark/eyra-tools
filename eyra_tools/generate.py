import os
from pathlib import Path

import click

from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__


@click.command(short_help="Initialise an EYRA algorithm container.")
@click.version_option(__version__.__version__, "-v", "--version")
@click.argument("container_type", type=click.Choice(['submission', 'evaluation']))
@click.argument("container_name")
@click.option('-d', '--docker-hub-account', prompt='Docker hub account')
def generate(container_type, container_name, docker_hub_account):
    if not container_name.isidentifier():
        raise ValueError("{} is not a valid container name!".format(container_name))

    template_dir = Path(__file__).parent / "template"

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "container_name": container_name,
                "container_type": container_type,
                "docker_hub_account": docker_hub_account
            },
        )
        msg = 'Created {} {} container in "{}{}". Good luck!'
        p = 'an' if container_type == 'evaluation' else 'a'
        click.echo(msg.format(p, container_type, container_name, os.sep))
    except FailedHookException:
        exit(1)
