#!/usr/bin/env python3
"""
Data Migration Script: SQLite to Railway PostgreSQL
This script migrates all data from local SQLite database to Railway PostgreSQL database.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line
from django.db import connections
from django.contrib.auth.models import User
from habits.models import Category, Habit, HabitDay, Profile
import json
from datetime import datetime

def setup_django():
    """Set up Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
    django.setup()

def backup_sqlite_data():
    """Create a backup of current SQLite data"""
    print("📦 Creating backup of current SQLite data...")
    
    # Backup Users
    users_data = []
    for user in User.objects.all():
        users_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
            'date_joined': user.date_joined.isoformat(),
            'last_login': user.last_login.isoformat() if user.last_login else None,
        })
    
    # Backup Categories
    categories_data = []
    for category in Category.objects.all():
        categories_data.append({
            'id': category.id,
            'name': category.name,
            'color': category.color,
            'description': category.description,
        })
    
    # Backup Habits
    habits_data = []
    for habit in Habit.objects.all():
        habits_data.append({
            'id': habit.id,
            'name': habit.name,
            'description': habit.description,
            'user_id': habit.user.id,
            'category_id': habit.category.id if habit.category else None,
            'start_date': habit.start_date.isoformat() if habit.start_date else None,
            'created_at': habit.created_at.isoformat() if habit.created_at else None,
        })
    
    # Backup HabitDays
    habit_days_data = []
    for habit_day in HabitDay.objects.all():
        habit_days_data.append({
            'id': habit_day.id,
            'habit_id': habit_day.habit.id,
            'day': habit_day.day,
            'completed': habit_day.completed,
            'completed_at': habit_day.completed_at.isoformat() if habit_day.completed_at else None,
        })
    
    # Backup Profiles
    profiles_data = []
    for profile in Profile.objects.all():
        profiles_data.append({
            'id': profile.id,
            'user_id': profile.user.id,
            'bio': profile.bio,
            'avatar': str(profile.avatar) if profile.avatar else None,
            'created_at': profile.created_at.isoformat() if profile.created_at else None,
            'updated_at': profile.updated_at.isoformat() if profile.updated_at else None,
        })
    
    # Save backup to JSON file
    backup_data = {
        'timestamp': datetime.now().isoformat(),
        'users': users_data,
        'categories': categories_data,
        'habits': habits_data,
        'habit_days': habit_days_data,
        'profiles': profiles_data,
    }
    
    with open('sqlite_backup.json', 'w') as f:
        json.dump(backup_data, f, indent=2)
    
    print(f"✅ Backup created: sqlite_backup.json")
    print(f"📊 Data summary:")
    print(f"   - Users: {len(users_data)}")
    print(f"   - Categories: {len(categories_data)}")
    print(f"   - Habits: {len(habits_data)}")
    print(f"   - Habit Days: {len(habit_days_data)}")
    print(f"   - Profiles: {len(profiles_data)}")
    
    return backup_data

def setup_railway_database():
    """Set up Railway PostgreSQL database"""
    print("🚀 Setting up Railway PostgreSQL database...")
    
    # Set Railway database URL
    railway_db_url = "postgresql://postgres:password@mainline.proxy.rlwy.net:22310/railway"
    os.environ['DATABASE_URL'] = railway_db_url
    
    # Re-setup Django with new database
    django.setup()
    
    print("✅ Railway database connection established")

def migrate_data_to_railway(backup_data):
    """Migrate data from backup to Railway PostgreSQL"""
    print("🔄 Migrating data to Railway PostgreSQL...")
    
    # Clear existing data (if any)
    print("🧹 Clearing existing data...")
    HabitDay.objects.all().delete()
    Habit.objects.all().delete()
    Profile.objects.all().delete()
    Category.objects.all().delete()
    User.objects.all().delete()
    
    # Migrate Users
    print("👥 Migrating users...")
    user_id_mapping = {}  # Map old IDs to new IDs
    for user_data in backup_data['users']:
        old_id = user_data['id']
        user_data.pop('id')  # Remove ID to let Django create new one
        
        # Handle last_login
        if user_data['last_login']:
            user_data['last_login'] = datetime.fromisoformat(user_data['last_login'])
        else:
            user_data['last_login'] = None
        
        # Handle date_joined
        user_data['date_joined'] = datetime.fromisoformat(user_data['date_joined'])
        
        user = User.objects.create(**user_data)
        user_id_mapping[old_id] = user.id
        print(f"   ✅ Created user: {user.username}")
    
    # Migrate Categories
    print("📂 Migrating categories...")
    category_id_mapping = {}  # Map old IDs to new IDs
    for category_data in backup_data['categories']:
        old_id = category_data['id']
        category_data.pop('id')  # Remove ID to let Django create new one
        
        category = Category.objects.create(**category_data)
        category_id_mapping[old_id] = category.id
        print(f"   ✅ Created category: {category.name}")
    
    # Migrate Habits
    print("🎯 Migrating habits...")
    habit_id_mapping = {}  # Map old IDs to new IDs
    for habit_data in backup_data['habits']:
        old_id = habit_data['id']
        habit_data.pop('id')  # Remove ID to let Django create new one
        
        # Map user and category IDs
        habit_data['user_id'] = user_id_mapping[habit_data['user_id']]
        if habit_data['category_id']:
            habit_data['category_id'] = category_id_mapping[habit_data['category_id']]
        
        # Handle dates
        if habit_data['start_date']:
            habit_data['start_date'] = datetime.fromisoformat(habit_data['start_date'])
        if habit_data['created_at']:
            habit_data['created_at'] = datetime.fromisoformat(habit_data['created_at'])
        
        habit = Habit.objects.create(**habit_data)
        habit_id_mapping[old_id] = habit.id
        print(f"   ✅ Created habit: {habit.name}")
    
    # Migrate HabitDays
    print("📅 Migrating habit days...")
    for habit_day_data in backup_data['habit_days']:
        habit_day_data.pop('id')  # Remove ID to let Django create new one
        
        # Map habit ID
        habit_day_data['habit_id'] = habit_id_mapping[habit_day_data['habit_id']]
        
        # Handle completed_at date
        if habit_day_data['completed_at']:
            habit_day_data['completed_at'] = datetime.fromisoformat(habit_day_data['completed_at'])
        
        HabitDay.objects.create(**habit_day_data)
    
    print(f"   ✅ Created {len(backup_data['habit_days'])} habit day records")
    
    # Migrate Profiles
    print("👤 Migrating profiles...")
    for profile_data in backup_data['profiles']:
        profile_data.pop('id')  # Remove ID to let Django create new one
        
        # Map user ID
        profile_data['user_id'] = user_id_mapping[profile_data['user_id']]
        
        # Handle dates
        if profile_data['created_at']:
            profile_data['created_at'] = datetime.fromisoformat(profile_data['created_at'])
        if profile_data['updated_at']:
            profile_data['updated_at'] = datetime.fromisoformat(profile_data['updated_at'])
        
        Profile.objects.create(**profile_data)
    
    print(f"   ✅ Created {len(backup_data['profiles'])} profiles")
    
    print("🎉 Data migration completed successfully!")

def verify_migration():
    """Verify that all data was migrated correctly"""
    print("🔍 Verifying migration...")
    
    # Count records
    user_count = User.objects.count()
    category_count = Category.objects.count()
    habit_count = Habit.objects.count()
    habit_day_count = HabitDay.objects.count()
    profile_count = Profile.objects.count()
    
    print(f"📊 Migration verification:")
    print(f"   - Users: {user_count}")
    print(f"   - Categories: {category_count}")
    print(f"   - Habits: {habit_count}")
    print(f"   - Habit Days: {habit_day_count}")
    print(f"   - Profiles: {profile_count}")
    
    # Test some relationships
    print("🔗 Testing relationships...")
    for user in User.objects.all():
        habits = Habit.objects.filter(user=user)
        print(f"   - User {user.username}: {habits.count()} habits")
        
        for habit in habits[:3]:  # Show first 3 habits
            completions = HabitDay.objects.filter(habit=habit, completed=True).count()
            print(f"     - {habit.name}: {completions} completions")
    
    print("✅ Migration verification completed!")

def main():
    """Main migration function"""
    print("🚀 Starting SQLite to Railway PostgreSQL Migration")
    print("=" * 50)
    
    try:
        # Step 1: Setup Django with SQLite
        print("📋 Step 1: Setting up Django with SQLite...")
        setup_django()
        
        # Step 2: Backup SQLite data
        print("\n📋 Step 2: Backing up SQLite data...")
        backup_data = backup_sqlite_data()
        
        # Step 3: Setup Railway database
        print("\n📋 Step 3: Setting up Railway database...")
        setup_railway_database()
        
        # Step 4: Migrate data
        print("\n📋 Step 4: Migrating data...")
        migrate_data_to_railway(backup_data)
        
        # Step 5: Verify migration
        print("\n📋 Step 5: Verifying migration...")
        verify_migration()
        
        print("\n🎉 Migration completed successfully!")
        print("✅ Your data is now available on Railway PostgreSQL!")
        print("📝 Backup file: sqlite_backup.json")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main() 