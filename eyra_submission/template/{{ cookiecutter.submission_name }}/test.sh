#!/usr/bin/env bash

./build.sh

docker volume create {{ cookiecutter.submission_name|lower }}-output

docker run --rm --memory=4g -v $(pwd)/test-input-data/:/input/ -v {{ cookiecutter.submission_name|lower }}-output:/output/ {{ cookiecutter.submission_name|lower }}

docker run --rm -v {{ cookiecutter.submission_name|lower }}-output:/output/ {{ cookiecutter.docker_base_image }} cat /output/data.txt

docker volume rm {{ cookiecutter.submission_name|lower }}-output
