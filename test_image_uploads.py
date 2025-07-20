#!/usr/bin/env python3
"""
Image Upload Test Script
This script tests image upload functionality and diagnoses production issues.
"""

import os
import sys
import django
import tempfile
from pathlib import Path
from PIL import Image

def setup_django():
    """Set up Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
    django.setup()

def test_media_directory():
    """Test media directory setup and permissions"""
    print("🔍 Testing media directory setup...")
    
    from django.conf import settings
    
    media_root = settings.MEDIA_ROOT
    profile_images_dir = media_root / 'profile_images'
    
    print(f"📁 Media root: {media_root}")
    print(f"📁 Profile images dir: {profile_images_dir}")
    
    # Check if directories exist
    print(f"✅ Media root exists: {media_root.exists()}")
    print(f"✅ Profile images dir exists: {profile_images_dir.exists()}")
    
    # Check permissions
    if media_root.exists():
        stat_info = media_root.stat()
        print(f"📊 Media root permissions: {oct(stat_info.st_mode)[-3:]}")
    
    if profile_images_dir.exists():
        stat_info = profile_images_dir.stat()
        print(f"📊 Profile images dir permissions: {oct(stat_info.st_mode)[-3:]}")
    
    # Test write permissions
    try:
        test_file = profile_images_dir / 'test_write.txt'
        test_file.write_text('test')
        test_file.unlink()  # Clean up
        print("✅ Write permissions: OK")
    except Exception as e:
        print(f"❌ Write permissions failed: {e}")

def test_image_upload():
    """Test image upload functionality"""
    print("\n🖼️  Testing image upload functionality...")
    
    from habits.models import Profile
    from django.contrib.auth.models import User
    from django.core.files.uploadedfile import SimpleUploadedFile
    
    # Get first user
    try:
        user = User.objects.first()
        if not user:
            print("❌ No users found in database")
            return
        
        profile = Profile.objects.get(user=user)
        print(f"👤 Testing with user: {user.username}")
        
        # Create a test image
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
            # Create a simple test image
            img = Image.new('RGB', (100, 100), color='red')
            img.save(tmp_file.name)
            
            # Read the file
            with open(tmp_file.name, 'rb') as f:
                image_data = f.read()
            
            # Create SimpleUploadedFile
            uploaded_file = SimpleUploadedFile(
                name='test_image.png',
                content=image_data,
                content_type='image/png'
            )
            
            # Test upload
            try:
                # Save the image to profile
                profile.profile_image.save('test_upload.png', uploaded_file, save=True)
                print("✅ Image upload test successful")
                print(f"📁 Saved to: {profile.profile_image.path}")
                print(f"🌐 URL: {profile.profile_image.url}")
                
                # Test if file exists
                if profile.profile_image.path and os.path.exists(profile.profile_image.path):
                    print("✅ File exists on disk")
                else:
                    print("❌ File does not exist on disk")
                
            except Exception as e:
                print(f"❌ Image upload failed: {e}")
            
            finally:
                # Clean up temp file
                os.unlink(tmp_file.name)
    
    except Exception as e:
        print(f"❌ Test failed: {e}")

def check_existing_images():
    """Check existing profile images"""
    print("\n📸 Checking existing profile images...")
    
    from habits.models import Profile
    
    profiles = Profile.objects.all()
    for profile in profiles:
        print(f"\n👤 {profile.user.username}:")
        
        if profile.profile_image:
            print(f"   📁 Path: {profile.profile_image.path}")
            print(f"   🌐 URL: {profile.profile_image.url}")
            print(f"   📊 File exists: {os.path.exists(profile.profile_image.path) if profile.profile_image.path else False}")
            
            if profile.profile_image.path and os.path.exists(profile.profile_image.path):
                file_size = os.path.getsize(profile.profile_image.path)
                print(f"   📏 File size: {file_size} bytes")
        else:
            print("   ⚠️  No profile image")

def test_form_validation():
    """Test form validation"""
    print("\n✅ Testing form validation...")
    
    from habits.forms import ProfileForm
    from habits.models import Profile
    from django.contrib.auth.models import User
    
    user = User.objects.first()
    if not user:
        print("❌ No users found")
        return
    
    profile = Profile.objects.get(user=user)
    
    # Test valid form
    form_data = {
        'bio': 'Test bio',
        'email': 'test@example.com',
        'weekly_stats_enabled': True
    }
    
    form = ProfileForm(data=form_data, instance=profile)
    if form.is_valid():
        print("✅ Form validation: OK")
    else:
        print(f"❌ Form validation failed: {form.errors}")

def main():
    """Main function"""
    print("🚀 Image Upload Test Script")
    print("=" * 40)
    
    setup_django()
    test_media_directory()
    test_image_upload()
    check_existing_images()
    test_form_validation()
    
    print("\n✅ Image upload test completed!")
    print("\n📝 Recommendations:")
    print("1. If write permissions failed, check Railway file system permissions")
    print("2. If uploads fail, ensure media directory exists and is writable")
    print("3. For production, consider using cloud storage (AWS S3, etc.)")
    print("4. Monitor file uploads in Railway logs")

if __name__ == '__main__':
    main() 