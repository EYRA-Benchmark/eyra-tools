import os
import shutil

from pathlib import Path


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

ctype = '{{ cookiecutter.container_type }}'

if ctype == 'evaluation':
    remove(str(Path('data')/'input'/'test_data'))
elif ctype == 'submission':
    remove(str(Path('data')/'input'/'implementation_output'))
    remove(str(Path('data')/'input'/'ground_truth'))
