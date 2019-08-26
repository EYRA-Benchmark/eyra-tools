#!/usr/bin/env bash

./build.sh

docker run --rm --memory=4g -v $(pwd)/data/input/:/data/input/ -v $(pwd)/data/:/data/ {{ cookiecutter.container_name }}