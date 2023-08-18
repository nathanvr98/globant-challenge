#!/bin/bash

# Run Python code quality checks

echo "Running code quality checks..."

# Run flake8
flake8 app/

# Run black
black app/

# Run mypy
mypy app/

echo "Code quality checks completed."