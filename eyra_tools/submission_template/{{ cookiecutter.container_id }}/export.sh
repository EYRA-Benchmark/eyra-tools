#!/usr/bin/env bash

./build.sh

docker save {{ cookiecutter.container_id }} > {{ cookiecutter.container_id }}.tar | gzip > {{ cookiecutter.container_id }}.tar.gz
if [ -e {{ cookiecutter.container_id }}.tar ]
then
    rm {{ cookiecutter.container_id }}.tar
fi
