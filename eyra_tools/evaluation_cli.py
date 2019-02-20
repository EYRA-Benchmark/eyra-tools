from pathlib import Path
from uuid import uuid1

import click
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-v", "--version")
def evaluation():
    pass


@evaluation.command(short_help="Initialize an EYRA evaluation project.")
@click.argument("container_id_prefix")
def init(container_id_prefix):
    if not container_id_prefix.isidentifier():
        raise ValueError(f"{container_id_prefix} is not a valid container id prefix!")

    container_id = "{}_{}".format(container_id_prefix, str(uuid1()))
    template_dir = Path(__file__).parent / "evaluation_template"

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "container_id": container_id,
            },
        )
        click.echo(f"Created evaluation project in {container_id}")
    except FailedHookException:
        exit(1)
