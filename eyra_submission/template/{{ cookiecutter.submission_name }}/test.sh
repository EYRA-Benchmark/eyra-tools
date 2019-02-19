#!/usr/bin/env bash

./build.sh

#docker volume create {{ cookiecutter.submission_name|lower }}-output

docker run --rm --memory=4g -v $(pwd)/test-input-data/:/input/ -v {{ cookiecutter.submission_name|lower }}-output:/output/ {{ cookiecutter.submission_name|lower }}