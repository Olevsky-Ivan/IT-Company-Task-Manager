#!/bin/bash

# Set up a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server (optional)
# python manage.py runserver 0.0.0.0:8000
