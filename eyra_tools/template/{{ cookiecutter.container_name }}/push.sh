#!/usr/bin/env bash

./build.sh

docker tag {{ cookiecutter.container_name }} {{ cookiecutter.docker_hub_account }}/{{ cookiecutter.container_name }}
docker push {{ cookiecutter.docker_hub_account }}/{{ cookiecutter.container_name }}