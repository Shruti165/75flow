#!/bin/bash

echo "🚀 Starting 75Flow application..."

# Exit on any error
set -e

# Print environment information
echo "🔍 Environment Information:"
echo "   PORT: $PORT"
echo "   ENVIRONMENT: $ENVIRONMENT"
echo "   DEBUG: $DEBUG"
echo "   DATABASE_URL: ${DATABASE_URL:0:50}..."

# Test port binding
echo "🔧 Testing port binding..."
python test_port.py

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "🚀 Starting Gunicorn..."
exec gunicorn flow75.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 1 \
    --timeout 120 \
    --log-file - \
    --access-logfile - \
    --error-logfile - \
    --preload \
    --max-requests 1000 \
    --max-requests-jitter 100 