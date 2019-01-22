EYRA submission template
------------------------

Requirements:
- Docker
- python 3.6+
- pipenv/pip

Install:
- clone repo
- cd repo
- pipenv install
- pipenv install -e .

Future install (after pypi upload):
- pip install eyra_submission

Run:
- eyra_submission init <name>
- add algorithm code to <name>/evaluation.py
- add input data to <name>/test/
- <name>/test.sh


