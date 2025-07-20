#!/bin/bash

echo "🚀 75Flow Deployment Script for Railway"
echo "========================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
fi

echo "🔐 Logging into Railway..."
railway login

echo "🚂 Creating new Railway project..."
railway init

echo "🗄️  Adding PostgreSQL database..."
echo "   Please select 'Database' → 'PostgreSQL' when prompted"
railway add

echo "⚙️  Setting environment variables..."
railway variables set ENVIRONMENT=production
railway variables set DEBUG=False
railway variables set SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
railway variables set ALLOWED_HOSTS=*.railway.app
railway variables set CSRF_TRUSTED_ORIGINS=https://*.railway.app

echo "📤 Deploying to Railway..."
railway up

echo "🔄 Running database migrations..."
railway run python manage.py migrate_to_postgres

echo "✅ Deployment complete!"
echo "🌐 Your app is now live at: $(railway domain)"

echo ""
echo "📋 Next steps:"
echo "1. Visit the admin panel: $(railway domain)/admin/"
echo "2. Create a superuser: railway run python manage.py createsuperuser"
echo "3. Share the URL with Sid and Sanju!"
echo ""
echo "🔧 Useful commands:"
echo "   - View logs: railway logs"
echo "   - Open app: railway open"
echo "   - Connect to database: railway connect"
echo "   - Check status: railway status"
echo ""
echo "🗄️  Database info:"
echo "   - PostgreSQL is automatically configured"
echo "   - DATABASE_URL is auto-provided by Railway"
echo "   - Local development continues to use SQLite" 