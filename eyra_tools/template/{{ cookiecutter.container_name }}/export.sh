#!/usr/bin/env bash

docker save --output {{ cookiecutter.container_name }}.tar {{ cookiecutter.container_name }}