# EYRA tools

[![Build Status](https://travis-ci.org/EYRA-Benchmark/eyra-tools.svg?branch=master)](https://travis-ci.org/EYRA-Benchmark/eyra-tools)
[![Documentation Status](https://readthedocs.org/projects/eyra-tools/badge/?version=latest)](https://eyra-tools.readthedocs.io/en/latest/?badge=latest)

## Installation

#### Prerequisites

Make sure you have the following tools installed:
- Docker
- python 3.6+
- virtualenv/pip

#### Prepare virtual environment

```
git clone git@github.com:EYRA-Benchmark/eyra-tools.git
cd eyra-tools
virtualenv eyra_venv
source eyra_venv/bin/activate
pip install -r requirements.txt
pip install -e .
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

#### Build, export and push
To build the docker image of your algorithm, use the `build.sh` script. To export the image to a tar file, use
the `export.sh` script. To upload the algorithm image to the EYRA docker registry, use the `push.sh` script.

## License

Copyright (c) 2019, Netherlands eScience Center

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
