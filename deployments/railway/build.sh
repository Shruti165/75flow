#!/bin/bash

echo "🔨 Building 75Flow for Railway deployment..."

# Exit on any error
set -e

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗄️  Running database migrations..."
python manage.py migrate --noinput

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Build completed successfully!" 