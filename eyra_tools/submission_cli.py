from pathlib import Path
from uuid import uuid1

import click
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-v", "--version")
def submission():
    pass


@submission.command(short_help="Initialise an EYRA submission project.")
@click.argument("container_id_prefix")
def init(container_id_prefix):
    if not container_id_prefix.isidentifier():
        raise ValueError(f"{container_id_prefix} is not a valid container id prefix!")

    container_id = "{}_{}".format(container_id_prefix, str(uuid1()))
    template_dir = Path(__file__).parent / "submission_template"

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "container_id": container_id,
            },
        )
        click.echo(f"Created submission project in {container_id}. Good luck!")
    except FailedHookException:
        exit(1)
