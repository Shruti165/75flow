#!/bin/bash

echo "🔧 Setting Railway Environment Variables for 75Flow..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI is not installed. Please install it first:"
    echo "   npm install -g @railway/cli"
    echo "   Then run: railway login"
    exit 1
fi

echo "📝 Setting environment variables..."

# Set the environment variables
railway variables set ENVIRONMENT=production
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS="flow75.up.railway.app,*.railway.app,*.up.railway.app,localhost,127.0.0.1"
railway variables set CSRF_TRUSTED_ORIGINS="https://flow75.up.railway.app,https://*.railway.app,https://*.up.railway.app"

# Generate a new secret key if needed
SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
railway variables set SECRET_KEY="$SECRET_KEY"

echo "✅ Environment variables set successfully!"
echo ""
echo "🔍 Current environment variables:"
railway variables

echo ""
echo "🚀 Now redeploy the app:"
echo "   railway up"
echo ""
echo "🧪 Test the deployment:"
echo "   curl https://flow75.up.railway.app/health/" 