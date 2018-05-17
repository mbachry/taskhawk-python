#!/usr/bin/env bash

set -e

options="-v -s --strict --cov=taskhawk"

if [ -z "${target}" ]; then
    target="tests"
fi

options="${target} ${options}"

mypy taskhawk

python3 -bb -m pytest ${options}

flake8

pip install -e .
make docs
