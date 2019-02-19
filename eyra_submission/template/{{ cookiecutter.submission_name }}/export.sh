#!/usr/bin/env bash

./build.sh

docker save {{ cookiecutter.submission_name|lower }} > {{ cookiecutter.submission_name }}.tar | gzip > {{ cookiecutter.submission_name }}.tar.gz
if [ -e {{ cookiecutter.submission_name }}.tar ]
then
    rm {{ cookiecutter.submission_name }}.tar
fi
