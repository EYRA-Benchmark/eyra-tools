EYRA submission template
------------------------

#### Prerequisites:
- Docker
- python 3.6+
- pipenv/pip

#### Install:
- clone repo
- `cd repo`
- `pipenv install`
- `pipenv install -e .`


#### Future install (after pypi upload):
- `pip install eyra_submission`

#### Pre-run
- `pipenv shell`
- `cd <project location>`

#### Run:
- `eyra_submission init <submission_name>`
- `deactivate`

This will create a folder with all boilerplate code to start building an algorithm container. Don't forget to 
deactivate the virtualenv as you will develop in a separate virtualenv. 


#### Develop:
- create a virtualenv and activate it
- install all your requirements in the virtualenv
- add your code to the run method in the `algorithm_src/algorithm.py` module
- the algorithm code should read input data from the `/input/` folder and write any output files to the '/output/' 
folder
- any other files that your algorithm depends on should be placed in the `algorithm_src` folder
- add your input data to the `test-input-data` folder
- for running the algorithm, make sure your virtualenv is activated and execute the `test.sh` script: this will 
create a Docker container with your algorithm and run it
- the output data can be found in the `test-output-data` folder
- the `build.sh` script needs to be run while the virtualenv is activated! 
