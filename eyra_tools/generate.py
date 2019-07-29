from pathlib import Path
from uuid import uuid1

import click
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__


@click.command(short_help="Initialise an EYRA submission or evaluation project.")
@click.version_option(__version__, "-v", "--version")
@click.argument("container_type", type=click.Choice(['submission', 'evaluation']))
@click.argument("container_id_prefix")
def generate(container_type, container_id_prefix):
    if not container_id_prefix.isidentifier():
        raise ValueError("{} is not a valid container id prefix!".format(container_id_prefix))

    container_id = "{}_{}".format(container_id_prefix, str(uuid1()))
    template_dir = Path(__file__).parent / "template"

    if container_type == 'submission':
        src_prefix = 'algorithm'
    else:
        src_prefix = 'evaluation'

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "container_id": container_id,
                "container_type": container_type,
                "src_prefix": src_prefix
            },
        )
        click.echo(f"Created submission project in {container_id}. Good luck!")
    except FailedHookException:
        exit(1)
