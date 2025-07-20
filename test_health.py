#!/usr/bin/env python3
"""
Simple script to test the health endpoint
"""
import os
import sys
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.test import Client

def test_health_endpoint():
    """Test the health endpoint"""
    client = Client()
    
    # Test health endpoint
    response = client.get('/health/')
    print(f"Health endpoint status: {response.status_code}")
    print(f"Health endpoint content: {response.content.decode()}")
    
    if response.status_code == 200:
        print("✅ Health endpoint is working correctly!")
        return True
    else:
        print("❌ Health endpoint is not working!")
        return False

if __name__ == '__main__':
    test_health_endpoint() 