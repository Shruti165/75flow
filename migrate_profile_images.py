#!/usr/bin/env python3
"""
Profile Image Migration Script
This script ensures profile images work properly in production.
"""

import os
import sys
import django
import shutil
from pathlib import Path

def setup_django():
    """Set up Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
    django.setup()

def check_profile_images():
    """Check and fix profile images"""
    print("🔍 Checking profile images...")
    
    from habits.models import Profile
    from django.contrib.auth.models import User
    
    # Ensure media directory exists
    media_root = Path("media")
    media_root.mkdir(exist_ok=True)
    
    profile_images_dir = media_root / "profile_images"
    profile_images_dir.mkdir(exist_ok=True)
    
    print(f"✅ Media directory: {media_root}")
    print(f"✅ Profile images directory: {profile_images_dir}")
    
    # Check each profile
    profiles = Profile.objects.all()
    for profile in profiles:
        print(f"\n👤 Checking profile for user: {profile.user.username}")
        
        if profile.profile_image:
            # Get the current profile image path
            image_path = profile.profile_image.path if hasattr(profile.profile_image, 'path') else str(profile.profile_image)
            print(f"   📁 Current profile image: {image_path}")
            
            # Check if file exists
            if os.path.exists(image_path):
                print(f"   ✅ Profile image file exists")
            else:
                print(f"   ❌ Profile image file missing: {image_path}")
                
                # Try to find the file in different locations
                possible_locations = [
                    f"media/profile_images/{profile.user.username}.png",
                    f"media/profile_images/{profile.user.username}.jpg",
                    f"media/profile_images/{profile.user.username}.jpeg",
                    f"static/images/default_avatar.png",
                ]
                
                found_file = None
                for location in possible_locations:
                    if os.path.exists(location):
                        found_file = location
                        print(f"   🔍 Found file at: {location}")
                        break
                
                if found_file:
                    # Copy to correct location
                    new_filename = f"{profile.user.username}_{os.path.basename(found_file)}"
                    new_path = profile_images_dir / new_filename
                    shutil.copy2(found_file, new_path)
                    print(f"   ✅ Copied to: {new_path}")
                else:
                    print(f"   ⚠️  No profile image file found for {profile.user.username}")
        else:
            print(f"   ⚠️  No profile image set for {profile.user.username}")

def create_default_avatar():
    """Create a default avatar if needed"""
    print("\n🎨 Creating default avatar...")
    
    default_avatar_path = Path("static/images/default_avatar.png")
    if not default_avatar_path.exists():
        default_avatar_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create a simple default avatar (you can replace this with a real image)
        print(f"   📝 Creating default avatar at: {default_avatar_path}")
        # For now, just create an empty file - you can add a real default image later
        default_avatar_path.touch()
        print(f"   ✅ Default avatar created")

def main():
    """Main function"""
    print("🚀 Profile Image Migration Script")
    print("=" * 40)
    
    setup_django()
    check_profile_images()
    create_default_avatar()
    
    print("\n✅ Profile image check completed!")
    print("\n📝 Next steps:")
    print("1. If any images are missing, add them to the media/profile_images/ directory")
    print("2. Deploy to Railway with these updated settings")
    print("3. Profile images should now work in production")

if __name__ == '__main__':
    main() 