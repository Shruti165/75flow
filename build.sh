#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Upgrade pip first to avoid compatibility issues
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install Pillow first with specific flags to avoid build issues
echo "Installing Pillow..."
pip install Pillow==9.5.0 --no-cache-dir --verbose --global-option=build_ext --global-option=--disable-platform-guessing

# Install remaining requirements
echo "Installing remaining requirements..."
pip install -r requirements.txt --no-cache-dir --verbose

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"
