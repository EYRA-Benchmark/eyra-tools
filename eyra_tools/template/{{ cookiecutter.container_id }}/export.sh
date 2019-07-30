#!/usr/bin/env bash

docker save --output {{ cookiecutter.container_id }}.tar {{ cookiecutter.container_id }}