#!/usr/bin/env bash

python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install dist/my_minipack-1.0.0-py3-none-any.whl
