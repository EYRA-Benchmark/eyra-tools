#!/usr/bin/env bash

./build.sh

docker save {{ cookiecutter.package_name|lower }} > {{ cookiecutter.package_name }}.tar | gzip > {{ cookiecutter.package_name }}.tar.gz
if [ -e {{ cookiecutter.package_name }}.tar ]
then
    rm {{ cookiecutter.package_name }}.tar
fi
