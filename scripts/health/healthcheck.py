#!/usr/bin/env python3
"""
Simple health check script for Railway deployment
"""
import os
import sys
import django

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    print("🔍 Running health check...")
    
    # Check Django configuration
    try:
        from django.conf import settings
        print(f"✅ Django settings loaded")
        print(f"✅ DEBUG = {settings.DEBUG}")
        print(f"✅ ALLOWED_HOSTS = {settings.ALLOWED_HOSTS}")
        print(f"✅ DATABASE = {settings.DATABASES['default']['ENGINE']}")
    except Exception as e:
        print(f"❌ Django settings error: {e}")
        sys.exit(1)
    
    # Check database connection
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✅ Database connection successful")
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        sys.exit(1)
    
    print("✅ Health check passed!")
    sys.exit(0) 