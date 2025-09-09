#!/usr/bin/env python3
"""
Reset user passwords on Render deployment
This script resets passwords to usernames for easy access
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User

def reset_passwords():
    """Reset all user passwords to their usernames"""
    print("🔐 Resetting user passwords...")
    
    for user in User.objects.all():
        try:
            user.set_password(user.username)
            user.save()
            print(f"  ✅ Reset password for: {user.username}")
        except Exception as e:
            print(f"  ❌ Error resetting password for {user.username}: {e}")
    
    print("\n🎉 Password reset complete!")
    print("All users can now login with:")
    print("Username: their_username")
    print("Password: their_username")

if __name__ == "__main__":
    reset_passwords()
