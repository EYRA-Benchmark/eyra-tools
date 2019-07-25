import pytest
import os
import plumbum

from pathlib import Path
from plumbum.cmd import bash


@pytest.mark.parametrize('ctype,prefix', [('submission', 'algorithm'),
                                          ('evaluation', 'evaluation')])
def test_project_container_type(ctype, prefix, cookies):
    template_dir = Path(__file__).parent.parent / "eyra_tools" / "submission_template"

    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_id': 'example',
                                          'container_type': ctype,
                                          'src_prefix': prefix})
    print(template_dir)

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project.basename.startswith('example')
    assert project.project.isdir()


@pytest.mark.parametrize('ctype,prefix', [('submission', 'algorithm'),
                                          ('evaluation', 'evaluation')])
def test_submission_run_test_sh(ctype, prefix, cookies):
    template_dir = Path(__file__).parent.parent / \
        "eyra_tools" / "submission_template"

    project = cookies.bake(template=str(template_dir.absolute()),
                           extra_context={'container_id': 'example',
                                          'container_type': ctype,
                                          'src_prefix': prefix})
    cwd = os.getcwd()
    os.chdir(str(project.project))

    # run script
    try:
        bash('test.sh')
    except plumbum.ProcessExecutionError as e:
        pytest.fail(e)
    finally:
        os.chdir(cwd)

    # test output
    out = project.project.join('data', 'output', 'example_output_data.txt')
    assert os.path.isfile(out)


