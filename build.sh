#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip first
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
