#!/usr/bin/env bash

pip freeze > ./requirements.txt
docker build -t {{ cookiecutter.submission_name|lower }} .
