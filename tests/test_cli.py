import pytest
import os

from click.testing import CliRunner
from plumbum.cmd import ls

from eyra_tools.generate import generate


def test_generate_submission_invalid_container_id():
    runner = CliRunner()
    result = runner.invoke(generate, ['submission', 'in valid'])

    assert result.exit_code == 1


@pytest.mark.parametrize('container_type', ['submission', 'evaluation'])
def test_project_creation(container_type):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(generate, [container_type, 'example'])

        print(result)

        assert result.exit_code == 0

        project_dir_name = ls().strip()

        assert os.path.isdir(project_dir_name)
