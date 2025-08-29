#!/usr/bin/env python3
"""
Test script to verify file paths and build environment
"""

import os
import sys

def test_paths():
    """Test various file paths"""
    print("🔍 Testing file paths...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    # Test render_deployment directory
    render_deployment_path = "render_deployment"
    if os.path.exists(render_deployment_path):
        print(f"✅ {render_deployment_path} directory exists")
        
        # List contents
        try:
            files = os.listdir(render_deployment_path)
            print(f"📁 Files in {render_deployment_path}:")
            for file in files:
                print(f"  - {file}")
        except Exception as e:
            print(f"❌ Error listing files: {e}")
    else:
        print(f"❌ {render_deployment_path} directory not found")
    
    # Test specific files
    test_files = [
        "render_deployment/refresh_data.py",
        "render_deployment/import_local_data.py", 
        "render_deployment/import_all_local_data.py",
        "manage.py"
    ]
    
    print("\n🔍 Testing specific files:")
    for file_path in test_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} not found")
    
    # Test current directory files
    print("\n🔍 Testing current directory files:")
    current_files = os.listdir(".")
    for file in current_files:
        if file.endswith('.py'):
            print(f"  - {file}")

if __name__ == "__main__":
    test_paths()
