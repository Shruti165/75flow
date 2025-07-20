#!/usr/bin/env python3
"""
Railway-specific startup script for 75Flow
"""
import os
import sys
import django

def main():
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
    django.setup()
    
    # Get port from environment
    port = os.getenv('PORT', '8000')
    host = '0.0.0.0'
    
    print(f"🚀 Starting 75Flow on Railway...")
    print(f"✅ Host: {host}")
    print(f"✅ Port: {port}")
    print(f"✅ Environment: {os.getenv('ENVIRONMENT', 'development')}")
    
    # Import and start Gunicorn
    from gunicorn.app.wsgiapp import WSGIApplication
    
    # Configure Gunicorn
    sys.argv = [
        'gunicorn',
        'flow75.wsgi:application',
        f'--bind={host}:{port}',
        '--workers=1',
        '--timeout=120',
        '--log-file=-',
        '--access-logfile=-',
        '--error-logfile=-',
        '--preload',
        '--max-requests=1000',
        '--max-requests-jitter=100',
        '--keep-alive=2'
    ]
    
    # Start the application
    WSGIApplication().run()

if __name__ == '__main__':
    main() 