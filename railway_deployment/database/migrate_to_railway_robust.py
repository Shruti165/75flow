#!/usr/bin/env python3
"""
Robust Migration Script for Railway PostgreSQL
This script handles data migration more carefully to avoid conflicts.
"""

import os
import sys
import django
import subprocess
import json
from pathlib import Path

def check_database_url():
    """Check if DATABASE_URL is set"""
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable is not set!")
        print("Please set it with:")
        print("export DATABASE_URL='your_railway_database_url_here'")
        return False
    
    print(f"✅ DATABASE_URL found: {database_url[:50]}...")
    return True

def clear_all_data():
    """Clear all data from the database"""
    print("🧹 Clearing all existing data...")
    
    try:
        subprocess.run([
            'python3', 'manage.py', 'shell', '-c',
            '''
from django.contrib.auth.models import User
from habits.models import Category, Habit, HabitDay, Profile

print("Clearing all data...")
HabitDay.objects.all().delete()
Habit.objects.all().delete()
Profile.objects.all().delete()
Category.objects.all().delete()
User.objects.all().delete()
print("✅ All data cleared!")
'''
        ], check=True)
        print("✅ All existing data cleared!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clear data: {e}")
        return False

def load_data_without_conflicts():
    """Load data using a more robust approach"""
    print("📥 Loading data without conflicts...")
    
    backup_dir = Path("migration_backup")
    
    # Load users first
    print("👥 Loading users...")
    try:
        subprocess.run(['python3', 'manage.py', 'loaddata', str(backup_dir / 'auth_user.json')], check=True)
        print("   ✅ Users loaded")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to load users: {e}")
        return False
    
    # Load categories
    print("📂 Loading categories...")
    try:
        subprocess.run(['python3', 'manage.py', 'loaddata', str(backup_dir / 'habits_category.json')], check=True)
        print("   ✅ Categories loaded")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to load categories: {e}")
        return False
    
    # Load profiles manually to avoid conflicts
    print("👤 Loading profiles...")
    try:
        with open(backup_dir / 'habits_profile.json', 'r') as f:
            profile_data = json.load(f)
        
        subprocess.run([
            'python3', 'manage.py', 'shell', '-c',
            f'''
from django.contrib.auth.models import User
from habits.models import Profile

# Create profiles manually
profiles_data = {profile_data}
for profile_info in profiles_data:
    user_id = profile_info['fields']['user']
    try:
        user = User.objects.get(id=user_id)
        Profile.objects.get_or_create(
            user=user,
            defaults={{
                'bio': profile_info['fields'].get('bio', ''),
                'email': profile_info['fields'].get('email'),
                'weekly_stats_enabled': profile_info['fields'].get('weekly_stats_enabled', True)
            }}
        )
        print(f"  - Created profile for user {{user.username}}")
    except User.DoesNotExist:
        print(f"  - User {{user_id}} not found, skipping profile")
    except Exception as e:
        print(f"  - Error creating profile for user {{user_id}}: {{e}}")

print("✅ Profiles loaded!")
'''
        ], check=True)
        print("   ✅ Profiles loaded")
    except Exception as e:
        print(f"   ❌ Failed to load profiles: {e}")
        return False
    
    # Load habits
    print("🎯 Loading habits...")
    try:
        subprocess.run(['python3', 'manage.py', 'loaddata', str(backup_dir / 'habits_habit.json')], check=True)
        print("   ✅ Habits loaded")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to load habits: {e}")
        return False
    
    # Load habit days
    print("📅 Loading habit days...")
    try:
        subprocess.run(['python3', 'manage.py', 'loaddata', str(backup_dir / 'habits_habitday.json')], check=True)
        print("   ✅ Habit days loaded")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed to load habit days: {e}")
        return False
    
    return True

def migrate_to_railway():
    """Migrate data to Railway"""
    print("🔄 Migrating to Railway PostgreSQL...")
    
    # Setup Django with Railway database
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
    django.setup()
    
    # Run migrations
    print("📋 Running migrations...")
    try:
        subprocess.run(['python3', 'manage.py', 'migrate'], check=True)
        print("✅ Migrations completed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    # Clear all existing data
    if not clear_all_data():
        return False
    
    # Load data without conflicts
    if not load_data_without_conflicts():
        return False
    
    return True

def verify_migration():
    """Verify the migration"""
    print("🔍 Verifying migration...")
    
    try:
        result = subprocess.run([
            'python3', 'manage.py', 'shell', '-c',
            '''
from django.contrib.auth.models import User
from habits.models import Category, Habit, HabitDay, Profile
print(f"Users: {User.objects.count()}")
print(f"Categories: {Category.objects.count()}")
print(f"Habits: {Habit.objects.count()}")
print(f"HabitDays: {HabitDay.objects.count()}")
print(f"Profiles: {Profile.objects.count()}")

# Test relationships
print("\\n🔗 Testing relationships:")
for user in User.objects.all():
    habits = Habit.objects.all()
    profile = Profile.objects.filter(user=user).first()
    print(f"  - User {user.username}: {habits.count()} habits, profile: {'Yes' if profile else 'No'}")
'''
        ], capture_output=True, text=True, check=True)
        
        print("📊 Migration results:")
        print(result.stdout)
        print("✅ Migration verification completed!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Verification failed: {e.stderr}")

def main():
    """Main function"""
    if not check_database_url():
        sys.exit(1)
    
    if migrate_to_railway():
        verify_migration()
        print("🎉 Migration completed successfully!")
        print("✅ Your data is now on Railway PostgreSQL!")
    else:
        print("❌ Migration failed!")
        sys.exit(1)

if __name__ == '__main__':
    main() 