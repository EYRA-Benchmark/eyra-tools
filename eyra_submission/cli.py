from pathlib import Path

import click
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from . import __version__

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-v", "--version")
def main():
    pass

@main.command(short_help="Initialise an EYRA submission project.")
@click.argument("package_name")
def init(package_name):
    template_dir = Path(__file__).parent / "template"

    try:
        cookiecutter(
            template=str(template_dir.absolute()),
            no_input=True,
            extra_context={
                "package_name": package_name,
            },
        )
        click.echo(f"Created project {package_name}")
    except FailedHookException:
        exit(1)
