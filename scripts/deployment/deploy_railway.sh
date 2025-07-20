#!/bin/bash

echo "🚀 Starting Railway deployment for 75Flow..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check if git is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: You have uncommitted changes. Please commit them first."
    echo "   Run: git add . && git commit -m 'Your commit message'"
    read -p "   Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI is not installed. Please install it first:"
    echo "   npm install -g @railway/cli"
    echo "   Then run: railway login"
    exit 1
fi

echo "📦 Committing and pushing changes to GitHub..."

# Add all changes
git add .

# Commit with timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "Deploy update: $TIMESTAMP"

# Push to GitHub
git push origin main

echo "✅ Changes pushed to GitHub"

echo "🚂 Deploying to Railway..."

# Deploy to Railway
railway up

echo "✅ Deployment completed!"
echo "🌐 Your app should be available at: https://flow75.up.railway.app"
echo "🔍 Check the deployment status at: https://railway.app/dashboard"

# Test the deployment
echo "🧪 Testing deployment..."
sleep 10  # Wait for deployment to complete

# Test health endpoint
HEALTH_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://flow75.up.railway.app/health/)
if [ "$HEALTH_RESPONSE" = "200" ]; then
    echo "✅ Health check passed! App is running correctly."
else
    echo "⚠️  Health check returned status: $HEALTH_RESPONSE"
    echo "   Check the Railway logs for more details."
fi

echo "🎉 Deployment process completed!" 