#!/usr/bin/env bash

./build.sh

docker tag {{ cookiecutter.container_name }} {{ cookiecutter.docker_registry_url }}/{{ cookiecutter.container_name }}
docker push {{ cookiecutter.docker_registry_url }}/{{ cookiecutter.container_name }}