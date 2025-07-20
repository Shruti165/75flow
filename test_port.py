#!/usr/bin/env python3
"""
Test script to verify port binding for Railway deployment
"""
import os
import sys

def test_port_binding():
    """Test if the application can bind to the PORT environment variable"""
    
    # Get the port from environment variable
    port = os.getenv('PORT', '8000')
    
    print(f"🔍 Testing port binding...")
    print(f"✅ PORT environment variable: {port}")
    print(f"✅ Current working directory: {os.getcwd()}")
    print(f"✅ Python version: {sys.version}")
    
    # Test if we can import Django
    try:
        import django
        print(f"✅ Django version: {django.get_version()}")
    except ImportError as e:
        print(f"❌ Django import error: {e}")
        return False
    
    # Test if we can import the WSGI application
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
        django.setup()
        
        from flow75.wsgi import application
        print(f"✅ WSGI application imported successfully")
    except Exception as e:
        print(f"❌ WSGI application error: {e}")
        return False
    
    # Test if we can bind to the port (simulate)
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', int(port)))
        sock.close()
        print(f"✅ Port {port} is available for binding")
    except Exception as e:
        print(f"❌ Port binding error: {e}")
        return False
    
    print(f"✅ All tests passed! Application should work on port {port}")
    return True

if __name__ == '__main__':
    success = test_port_binding()
    sys.exit(0 if success else 1) 