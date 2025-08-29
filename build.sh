#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Upgrade pip first to avoid compatibility issues
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Try to install Pillow first with fallback options
echo "Installing Pillow..."
if ! pip install Pillow==8.4.0 --no-cache-dir --verbose; then
    echo "Pillow 8.4.0 failed, trying Pillow 7.2.0..."
    if ! pip install Pillow==7.2.0 --no-cache-dir --verbose; then
        echo "Pillow 7.2.0 failed, trying latest compatible version..."
        pip install Pillow --no-cache-dir --verbose
    fi
fi

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
