#!/usr/bin/env bash

docker build -t {{ cookiecutter.submission_name|lower }} .
