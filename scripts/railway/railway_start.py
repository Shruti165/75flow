#!/usr/bin/env python3
"""
Railway-specific startup script for 75Flow
"""
import os
import sys
import django
import time
import signal

def signal_handler(signum, frame):
    print(f"🛑 Received signal {signum}, shutting down gracefully...")
    sys.exit(0)

def main():
    # Set up signal handlers
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Add project root to Python path
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, project_root)
        
        # Set up Django
        print("🔧 Setting up Django...")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
        django.setup()
        print("✅ Django setup complete")
        
        # Get port from environment
        port = os.getenv('PORT', '8000')
        host = '0.0.0.0'
        
        print(f"🚀 Starting 75Flow on Railway...")
        print(f"✅ Host: {host}")
        print(f"✅ Port: {port}")
        print(f"✅ Environment: {os.getenv('ENVIRONMENT', 'development')}")
        print(f"✅ Debug: {os.getenv('DEBUG', 'True')}")
        
        # Test database connection
        print("🗄️  Testing database connection...")
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✅ Database connection successful")
        
        # Test WSGI application
        print("🔧 Testing WSGI application...")
        from flow75.wsgi import application
        print("✅ WSGI application loaded successfully")
        
        # Import and start Gunicorn
        print("🚀 Starting Gunicorn...")
        from gunicorn.app.wsgiapp import WSGIApplication
        
        # Configure Gunicorn with explicit settings
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
            '--keep-alive=2',
            '--worker-class=sync',
            '--worker-connections=1000'
        ]
        
        print(f"✅ Gunicorn configuration ready")
        print(f"✅ Binding to {host}:{port}")
        
        # Start the application
        app = WSGIApplication()
        app.run()
        
    except Exception as e:
        print(f"❌ Startup error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main() 