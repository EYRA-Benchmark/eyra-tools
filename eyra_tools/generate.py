from pathlib import Path

import click
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__


@click.command(short_help="Initialise an EYRA algorithm container.")
@click.version_option(__version__.__version__, "-v", "--version")
@click.argument("container_type", type=click.Choice(['submission', 'evaluation']))
@click.argument("container_name")
def generate(container_type, container_name):
    if not container_name.isidentifier():
        raise ValueError("{} is not a valid container id prefix!".format(container_name))

    template_dir = Path(__file__).parent / "template"

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "container_name": container_name,
                "container_type": container_type
            },
        )
        click.echo("Created algorithm container in {}. Good luck!".format(container_name))
    except FailedHookException:
        exit(1)
