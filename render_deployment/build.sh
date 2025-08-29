#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Detect Python version
PYTHON_VERSION=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "Detected Python version: $PYTHON_VERSION"

# Upgrade pip first to avoid compatibility issues
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Choose requirements file based on Python version
if [[ "$PYTHON_VERSION" == "3.13" ]]; then
    echo "Using Python 3.13 optimized requirements..."
    REQ_FILE="requirements-py313.txt"
else
    echo "Using standard requirements..."
    REQ_FILE="requirements.txt"
fi

# Install requirements with verbose output
echo "Installing requirements from $REQ_FILE..."
pip install -r "$REQ_FILE" --no-cache-dir --verbose

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Import local data if available
            # Debug: Check what files exist
            echo "🔍 Checking available import scripts..."
            ls -la render_deployment/ || echo "render_deployment directory not accessible"
            
            # Always refresh data on every deploy/restart
            if [ -f "render_deployment/refresh_data.py" ]; then
                echo "🔄 Running data refresh on every deploy/restart..."
                python render_deployment/refresh_data.py
            elif [ -f "render_deployment/import_local_data.py" ]; then
                echo "🔄 Importing local data on every deploy/restart..."
                python render_deployment/import_local_data.py
            elif [ -f "render_deployment/import_all_local_data.py" ]; then
                echo "🔄 Importing comprehensive local data on every deploy/restart..."
                python render_deployment/import_all_local_data.py
            else
                echo "⚠️  No import scripts found, creating default users..."
                python manage.py create_default_users
            fi

echo "Build completed successfully!"
