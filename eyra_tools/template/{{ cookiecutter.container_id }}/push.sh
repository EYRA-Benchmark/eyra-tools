#!/usr/bin/env bash

./build.sh

docker tag {{ cookiecutter.container_id }} {{ cookiecutter.docker_registry_url }}/{{ cookiecutter.container_id }}
docker push {{ cookiecutter.docker_registry_url }}/{{ cookiecutter.container_id }}