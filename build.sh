#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Upgrade pip first to avoid compatibility issues
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements with more verbose output and error handling
echo "Installing requirements..."
pip install -r requirements.txt --no-cache-dir --verbose

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"
