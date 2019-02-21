# EYRA tools

## Installation 

#### Prerequisites

Make sure you have the following tools installed:
- Docker
- python 3.6+
- virtualenv/pip

#### Prepare virtual environment

```
clone git@github.com:EYRA-Benchmark/eyra-tools.git

virtualenv eyra_venv
source eyra_venv/bin/activate
pip install -r eyra-tools/requirements.txt
pip install -e eyra-tools
```

## Evaluation

Meant for challenge organisers.

#### Create evaluation project

```
eyra_evaluation init <evaluation_name>
```

This will create a folder with all boilerplate code to start building an evaluation container. 

## Submission

Meant for algorithm developers.

#### Create submission project

```
eyra_submission init <submission_name>
```

This will create a folder with all boilerplate code to start building an algorithm container. 

#### Develop
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
