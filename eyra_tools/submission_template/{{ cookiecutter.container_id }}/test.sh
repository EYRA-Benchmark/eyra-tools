#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/test-input-data/:/input/ -v $(pwd)/test-output-data/:/output/ {{ cookiecutter.container_id }}