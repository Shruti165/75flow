#!/bin/bash

echo "🚀 75Flow - One-Line Deployment to Railway"
echo "=========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 Committing changes to GitHub..."
    git add .
    git commit -m "🚀 Auto-deploy: $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin main
    echo "✅ Changes pushed to GitHub!"
else
    echo "✅ No changes to commit"
fi

# Generate secret key
SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

echo "✅ Project is ready for deployment!"
echo ""
echo "🔑 Generated Secret Key: $SECRET_KEY"
echo ""
echo "🚂 Deploying to Railway..."
echo ""

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
fi

echo "🔐 Logging into Railway..."
railway login

echo "🚂 Creating new Railway project..."
railway init

echo "⚙️  Setting environment variables..."
railway variables set SECRET_KEY="$SECRET_KEY"
railway variables set DEBUG=False
railway variables set ENVIRONMENT=production
railway variables set ALLOWED_HOSTS=*.railway.app

echo "📤 Deploying to Railway..."
railway up

echo "✅ Deployment complete!"
echo "🌐 Your app is now live at: $(railway domain)"

echo ""
echo "📋 Next steps:"
echo "1. Visit the admin panel: $(railway domain)/admin/"
echo "2. Create a superuser: railway run python manage.py createsuperuser"
echo "3. Share the URL with Sid and Sanju!"
echo ""
echo "👥 User credentials:"
echo "- Shruti / Shruti123"
echo "- Sid / Sid123"
echo "- Sanju / Sanju123"
echo ""
echo "🔧 To view logs: railway logs"
echo "🔧 To open the app: railway open" 