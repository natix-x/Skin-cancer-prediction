#!/bin/bash

# Check if the virtual environment is already activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    bash ./venv_setup.sh
fi

echo "Initializing..."
python run.py
