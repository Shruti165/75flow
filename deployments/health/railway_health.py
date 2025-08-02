#!/usr/bin/env python3
"""
Simple health check for Railway deployment
"""
import os
import sys
import django

def health_check():
    try:
        # Set up Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
        django.setup()
        
        # Test database
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Test WSGI app
        from flow75.wsgi import application
        
        print("✅ Health check passed!")
        return True
        
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

if __name__ == '__main__':
    success = health_check()
    sys.exit(0 if success else 1) 