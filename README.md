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

Pre-run
- pipenv shell
- cd <project location>

Run:
- eyra_submission init <name>
- add algorithm code to <name>/evaluation.py
- add input data to <name>/test/
- <name>/test.sh

Caveat
------
The `test.sh` script assumes that the output data is written to `/output/data.txt` as it simply `cat`s the contents of
this file to stdout. If the output of your algorithm is structured differently, update the `test.sh` script accordingly.
 
