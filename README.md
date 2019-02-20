EYRA tools
----------

## Evaluation
Bliep

## Submission

#### Prerequisites:
- Docker
- python 3.6+
- virtualenv/pip

#### Prepare virtual environment:
```
clone git@github.com:EYRA-Benchmark/eyra-submission.git

virtualenv eyra_venv
source eyra_venv/bin/activate
pip install cookiecutter
pip install -e eyra-submission
```

#### Run:
- `eyra_submission init <submission_name>`

This will create a folder with all boilerplate code to start building an algorithm container. 

#### Develop:
- add all your algorithm's dependencies to the `<submission_name>/requirements.txt` file
- add your algorithm's code to the run method in the `algorithm_src/algorithm.py` module (remember the imports)
- add your input data to the `test-input-data` folder
- Due to the infrastructure (docker), these folders will be renamed from the algorithm's perspective. 

<aside class="warning">
NOTE: So, please write your code so the input data is read from the `/input/` folder and the output data will need to be written to the `/output/` folder 
 </aside>

- any other files that your algorithm depends on should be placed in the `algorithm_src` folder

- to run the algorithm, execute the `test.sh` script: this will create a Docker container with your algorithm in it, and run it
- the output data can be found in the `test-output-data` folder
