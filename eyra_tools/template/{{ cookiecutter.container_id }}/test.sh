#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/data/input/:/input/ -v $(pwd)/data/output/:/output/ {{ cookiecutter.container_id }}