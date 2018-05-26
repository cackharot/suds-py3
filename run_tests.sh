#!/bin/sh
echo "Running tests on $(python --version)"
python -m unittest discover tests *_test.py
