#!/usr/bin/env bash

./build.sh

TAG=${1:-latest}

echo "Using tag: $TAG."

docker tag {{ cookiecutter.container_name }} {{ cookiecutter.docker_hub_account }}/{{ cookiecutter.container_name }}:$TAG
docker push {{ cookiecutter.docker_hub_account }}/{{ cookiecutter.container_name }}