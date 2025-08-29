#!/usr/bin/env python3
"""
Data refresh script for Render deployment
This script can be run manually or automatically to refresh data
"""

import os
import sys
import django
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay

def clear_existing_data():
    """Clear existing data to ensure clean import"""
    print("🧹 Clearing existing data...")
    
    # Clear habit completion records
    HabitDay.objects.all().delete()
    print("  ✅ Cleared habit completion records")
    
    # Clear habits
    Habit.objects.all().delete()
    print("  ✅ Cleared habits")
    
    # Clear profiles (but keep users)
    Profile.objects.all().delete()
    print("  ✅ Cleared profiles")
    
    # Clear categories
    Category.objects.all().delete()
    print("  ✅ Cleared categories")
    
    # Clear users (except admin)
    User.objects.exclude(username='admin').delete()
    print("  ✅ Cleared non-admin users")

def create_admin_if_not_exists():
    """Ensure admin user exists"""
    print("👑 Ensuring admin user exists...")
    
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@75flow.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }
    )
    
    if created:
        admin_user.set_password('admin')
        admin_user.save()
        print("  ✅ Created admin user")
    else:
        print("  ℹ️  Admin user already exists")

def import_categories():
    """Import categories"""
    print("📥 Importing categories...")
    
    categories_data = [
        {"name": "Reading", "color": "#2196f3"},
        {"name": "Fitness", "color": "#4caf50"},
        {"name": "Nutrition", "color": "#ff9800"},
        {"name": "Wealth", "color": "#9c27b0"},
        {"name": "Spiritual", "color": "#e91e63"},
        {"name": "Fun", "color": "#00bcd4"}
    ]
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'color': cat_data['color']}
        )
        if created:
            print(f"  ✅ Created category: {category.name}")
        else:
            print(f"  ℹ️  Category already exists: {category.name}")

def import_users():
    """Import users and profiles"""
    print("📥 Importing users and profiles...")
    
    users_data = [
        {
            "username": "Sid",
            "email": "",
            "first_name": "",
            "last_name": "",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "",
                "profile_image": None,
                "date_of_birth": None,
                "email": None,
                "weekly_stats_enabled": True
            }
        },
        {
            "username": "Shruti",
            "email": "",
            "first_name": "",
            "last_name": "",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "hello",
                "profile_image": None,
                "date_of_birth": None,
                "email": "strength.shruti@gmail.com",
                "weekly_stats_enabled": True
            }
        },
        {
            "username": "Sanju",
            "email": "",
            "first_name": "",
            "last_name": "",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "",
                "profile_image": None,
                "date_of_birth": None,
                "email": None,
                "weekly_stats_enabled": True
            }
        },
        {
            "username": "Sachin",
            "email": "sachin@gmail.com",
            "first_name": "Sachin",
            "last_name": "Test",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "",
                "profile_image": None,
                "date_of_birth": None,
                "email": None,
                "weekly_stats_enabled": True
            }
        },
        {
            "username": "Defni",
            "email": "defni@gmail.com",
            "first_name": "Defni",
            "last_name": "Defni",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "",
                "profile_image": None,
                "date_of_birth": None,
                "email": None,
                "weekly_stats_enabled": True
            }
        },
        {
            "username": "Pooja",
            "email": "pooja@gmail.com",
            "first_name": "Pooja",
            "last_name": "Pooja",
            "is_staff": False,
            "is_superuser": False,
            "is_active": True,
            "profile": {
                "bio": "",
                "profile_image": None,
                "date_of_birth": None,
                "email": None,
                "weekly_stats_enabled": True
            }
        }
    ]
    
    for user_data in users_data:
        # Create or get user
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'is_staff': user_data['is_staff'],
                'is_superuser': user_data['is_superuser'],
                'is_active': user_data['is_active']
            }
        )
        
        if created:
            print(f"  ✅ Created user: {user.username}")
        else:
            print(f"  ℹ️  User already exists: {user.username}")
        
        # Create or update profile
        profile, profile_created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': user_data['profile']['bio'],
                'date_of_birth': None,
                'email': user_data['profile']['email'],
                'weekly_stats_enabled': user_data['profile']['weekly_stats_enabled']
            }
        )
        
        if profile_created:
            print(f"    ✅ Created profile for: {user.username}")
        else:
            print(f"    ℹ️  Profile already exists for: {user.username}")

def import_all_habits():
    """Import ALL habits from local data"""
    print("📥 Importing ALL habits...")
    
    # Comprehensive habit data for all users
    all_habits_data = [
        # Shruti's habits
        {'user': 'Shruti', 'name': 'Fiction', 'category': 'Reading'},
        {'user': 'Shruti', 'name': 'Non-Fiction', 'category': 'Reading'},
        {'user': 'Shruti', 'name': 'Spiritual', 'category': 'Reading'},
        {'user': 'Shruti', 'name': 'Swim', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Run', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Dance', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Yoga / Stretch', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Gym', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Go To The Park', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Walk', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Football', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Hand Stand / Pull Up / Pole Session', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': '7 Minute HIIT', 'category': 'Fitness'},
        {'user': 'Shruti', 'name': 'Drink Matcha', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Consume Leaves', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Drink Coconut Water', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Take Supplements', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Have Fruits', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Drink Water', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Drink Vegetable Juice', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Prepare Meal / Cook Dinner', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Take Chia Seeds', 'category': 'Nutrition'},
        {'user': 'Shruti', 'name': 'Mantra Chanting', 'category': 'Spiritual'},
        {'user': 'Shruti', 'name': 'Get Aligned High Income Job Offers', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Optimise Linkedin', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'AI Projects', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Passion Projects', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Upskill', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Create Content', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Go To The Office', 'category': 'Wealth'},
        {'user': 'Shruti', 'name': 'Chanting', 'category': 'Spiritual'},
        {'user': 'Shruti', 'name': 'Journal', 'category': 'Spiritual'},
        {'user': 'Shruti', 'name': 'Grounding', 'category': 'Spiritual'},
        {'user': 'Shruti', 'name': 'Sleep Well / Binaural Beats', 'category': 'Spiritual'},
        {'user': 'Shruti', 'name': 'Attend an Event', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Social Club Meet', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Community Service', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Visit Orphanage/ Old Age Home', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Music Jam', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Painitng, Gardening, Sketch', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Declutter / Organise', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Planning for Tomorrow', 'category': 'Fun'},
        {'user': 'Shruti', 'name': 'Feed The Dogs', 'category': 'Fun'},
        
        # Admin's habits (same as Shruti)
        {'user': 'admin', 'name': 'Fiction', 'category': 'Reading'},
        {'user': 'admin', 'name': 'Non-Fiction', 'category': 'Reading'},
        {'user': 'admin', 'name': 'Spiritual', 'category': 'Reading'},
        {'user': 'admin', 'name': 'Swim', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Run', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Dance', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Yoga / Stretch', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Gym', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Go To The Park', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Walk', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Football', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Hand Stand / Pull Up / Pole Session', 'category': 'Fitness'},
        {'user': 'admin', 'name': '7 Minute HIIT', 'category': 'Fitness'},
        {'user': 'admin', 'name': 'Drink Matcha', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Consume Leaves', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Drink Coconut Water', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Take Supplements', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Have Fruits', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Drink Water', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Drink Vegetable Juice', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Prepare Meal / Cook Dinner', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Take Chia Seeds', 'category': 'Nutrition'},
        {'user': 'admin', 'name': 'Mantra Chanting', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Get Aligned High Income Job Offers', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Optimise Linkedin', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'AI Projects', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Passion Projects', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Upskill', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Create Content', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Go To The Office', 'category': 'Wealth'},
        {'user': 'admin', 'name': 'Chanting', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Journal', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Meditate', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Grounding', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Sleep Well / Binaural Beats', 'category': 'Spiritual'},
        {'user': 'admin', 'name': 'Attend an Event', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Hackathons', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Social Club Meet', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Community Service', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Visit Orphanage/ Old Age Home', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Music Jam', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Painitng, Gardening, Sketch', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Declutter / Organise', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Planning for Tomorrow', 'category': 'Fun'},
        {'user': 'admin', 'name': 'Feed The Dogs', 'category': 'Fun'},
        
        # Other users' habits
        {'user': 'Sid', 'name': 'Study fintech', 'category': 'Reading'},
        {'user': 'Sid', 'name': 'Read 30 minutes', 'category': 'Reading'},
        {'user': 'Sid', 'name': 'Morning workout', 'category': 'Fitness'},
        {'user': 'Sid', 'name': 'Drink 8 glasses water', 'category': 'Nutrition'},
        {'user': 'Sid', 'name': 'Track expenses', 'category': 'Wealth'},
        {'user': 'Sid', 'name': 'Meditation', 'category': 'Spiritual'},
        {'user': 'Sid', 'name': 'Play guitar', 'category': 'Fun'},
        {'user': 'Sid', 'name': 'Gym workout', 'category': 'Fitness'},
        {'user': 'Sid', 'name': 'Drink water', 'category': 'Nutrition'},
        {'user': 'Sid', 'name': 'Track investments', 'category': 'Wealth'},
        {'user': 'Sid', 'name': 'Coding practice', 'category': 'Fun'},
        {'user': 'Sid', 'name': 'Read business books', 'category': 'Reading'},
        {'user': 'Sid', 'name': 'Running', 'category': 'Fitness'},
        {'user': 'Sid', 'name': 'Eat healthy meals', 'category': 'Nutrition'},
        {'user': 'Sid', 'name': 'Save money', 'category': 'Wealth'},
        {'user': 'Sid', 'name': 'Prayer time', 'category': 'Spiritual'},
        {'user': 'Sid', 'name': 'Photography', 'category': 'Fun'},
        
        # Additional habits for other users
        {'user': 'Sanju', 'name': 'Read 30 minutes', 'category': 'Reading'},
        {'user': 'Sanju', 'name': 'Morning workout', 'category': 'Fitness'},
        {'user': 'Sanju', 'name': 'Drink 8 glasses water', 'category': 'Nutrition'},
        {'user': 'Sanju', 'name': 'Track expenses', 'category': 'Wealth'},
        {'user': 'Sanju', 'name': 'Meditation', 'category': 'Spiritual'},
        {'user': 'Sanju', 'name': 'Play guitar', 'category': 'Fun'},
        {'user': 'Sanju', 'name': 'Read tech blogs', 'category': 'Reading'},
        {'user': 'Sanju', 'name': 'Gym workout', 'category': 'Fitness'},
        {'user': 'Sanju', 'name': 'Eat healthy meals', 'category': 'Nutrition'},
        {'user': 'Sanju', 'name': 'Save money', 'category': 'Wealth'},
        {'user': 'Sanju', 'name': 'Prayer time', 'category': 'Spiritual'},
        {'user': 'Sanju', 'name': 'Photography', 'category': 'Fun'},
        {'user': 'Sanju', 'name': 'Running', 'category': 'Fitness'},
        {'user': 'Sanju', 'name': 'Protein intake', 'category': 'Nutrition'},
        {'user': 'Sanju', 'name': 'Investment research', 'category': 'Wealth'},
        {'user': 'Sanju', 'name': 'Journaling', 'category': 'Spiritual'},
        {'user': 'Sanju', 'name': 'Coding practice', 'category': 'Fun'},
        
        # Sachin's habits
        {'user': 'Sachin', 'name': 'Read 30 minutes', 'category': 'Reading'},
        {'user': 'Sachin', 'name': 'Morning workout', 'category': 'Fitness'},
        {'user': 'Sachin', 'name': 'Drink 8 glasses water', 'category': 'Nutrition'},
        {'user': 'Sachin', 'name': 'Track expenses', 'category': 'Wealth'},
        {'user': 'Sachin', 'name': 'Meditation', 'category': 'Spiritual'},
        {'user': 'Sachin', 'name': 'Play guitar', 'category': 'Fun'},
        {'user': 'Sachin', 'name': 'Read tech blogs', 'category': 'Reading'},
        {'user': 'Sachin', 'name': 'Gym workout', 'category': 'Fitness'},
        {'user': 'Sachin', 'name': 'Eat healthy meals', 'category': 'Nutrition'},
        {'user': 'Sachin', 'name': 'Save money', 'category': 'Wealth'},
        {'user': 'Sachin', 'name': 'Prayer time', 'category': 'Spiritual'},
        {'user': 'Sachin', 'name': 'Photography', 'category': 'Fun'},
        {'user': 'Sachin', 'name': 'Running', 'category': 'Fitness'},
        {'user': 'Sachin', 'name': 'Protein intake', 'category': 'Nutrition'},
        {'user': 'Sachin', 'name': 'Investment research', 'category': 'Wealth'},
        {'user': 'Sachin', 'name': 'Journaling', 'category': 'Spiritual'},
        {'user': 'Sachin', 'name': 'Coding practice', 'category': 'Fun'},
        
        # Defni's habits
        {'user': 'Defni', 'name': 'Read 30 minutes', 'category': 'Reading'},
        {'user': 'Defni', 'name': 'Morning workout', 'category': 'Fitness'},
        {'user': 'Defni', 'name': 'Drink 8 glasses water', 'category': 'Nutrition'},
        {'user': 'Defni', 'name': 'Track expenses', 'category': 'Wealth'},
        {'user': 'Defni', 'name': 'Meditation', 'category': 'Spiritual'},
        {'user': 'Defni', 'name': 'Play guitar', 'category': 'Fun'},
        {'user': 'Defni', 'name': 'Read tech blogs', 'category': 'Reading'},
        {'user': 'Defni', 'name': 'Gym workout', 'category': 'Fitness'},
        {'user': 'Defni', 'name': 'Eat healthy meals', 'category': 'Nutrition'},
        {'user': 'Defni', 'name': 'Save money', 'category': 'Wealth'},
        {'user': 'Defni', 'name': 'Prayer time', 'category': 'Spiritual'},
        {'user': 'Defni', 'name': 'Photography', 'category': 'Fun'},
        {'user': 'Defni', 'name': 'Running', 'category': 'Fitness'},
        {'user': 'Defni', 'name': 'Protein intake', 'category': 'Nutrition'},
        {'user': 'Defni', 'name': 'Investment research', 'category': 'Wealth'},
        {'user': 'Defni', 'name': 'Journaling', 'category': 'Spiritual'},
        {'user': 'Defni', 'name': 'Coding practice', 'category': 'Fun'},
        
        # Pooja's habits
        {'user': 'Pooja', 'name': 'Read 30 minutes', 'category': 'Reading'},
        {'user': 'Pooja', 'name': 'Morning workout', 'category': 'Fitness'},
        {'user': 'Pooja', 'name': 'Drink 8 glasses water', 'category': 'Nutrition'},
        {'user': 'Pooja', 'name': 'Track expenses', 'category': 'Wealth'},
        {'user': 'Pooja', 'name': 'Meditation', 'category': 'Spiritual'},
        {'user': 'Pooja', 'name': 'Play guitar', 'category': 'Fun'},
        {'user': 'Pooja', 'name': 'Read tech blogs', 'category': 'Reading'},
        {'user': 'Pooja', 'name': 'Gym workout', 'category': 'Fitness'},
        {'user': 'Pooja', 'name': 'Eat healthy meals', 'category': 'Nutrition'},
        {'user': 'Pooja', 'name': 'Save money', 'category': 'Wealth'},
        {'user': 'Pooja', 'name': 'Prayer time', 'category': 'Spiritual'},
        {'user': 'Pooja', 'name': 'Photography', 'category': 'Fun'},
        {'user': 'Pooja', 'name': 'Running', 'category': 'Fitness'},
        {'user': 'Pooja', 'name': 'Protein intake', 'category': 'Nutrition'},
        {'user': 'Pooja', 'name': 'Investment research', 'category': 'Wealth'},
        {'user': 'Pooja', 'name': 'Journaling', 'category': 'Spiritual'},
        {'user': 'Pooja', 'name': 'Coding practice', 'category': 'Fun'},
    ]
    
    imported_count = 0
    for habit_data in all_habits_data:
        try:
            user = User.objects.get(username=habit_data['user'])
            category = Category.objects.get(name=habit_data['category'])
            
            habit, created = Habit.objects.get_or_create(
                name=habit_data['name'],
                user=user,
                defaults={
                    'description': f"Daily {habit_data['name'].lower()}",
                    'category': category
                }
            )
            
            if created:
                imported_count += 1
                print(f"  ✅ Created habit: {habit.name} for {user.username}")
            else:
                print(f"  ℹ️  Habit already exists: {habit.name} for {user.username}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_data['user']}")
        except Category.DoesNotExist:
            print(f"  ❌ Category not found: {habit_data['category']}")
    
    print(f"  🎯 Total habits imported: {imported_count}")

def reset_passwords():
    """Reset all user passwords to usernames"""
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

def main():
    """Main refresh function"""
    print("🔄 Starting data refresh...")
    print("=" * 60)
    print(f"🕐 Refresh started at: {datetime.now()}")
    print("=" * 60)
    
    try:
        # Clear existing data
        clear_existing_data()
        print()
        
        # Ensure admin exists
        create_admin_if_not_exists()
        print()
        
        # Import fresh data
        import_categories()
        print()
        import_users()
        print()
        import_all_habits()
        print()
        reset_passwords()
        print()
        
        print("=" * 60)
        print("🎉 Data refresh completed successfully!")
        print(f"🕐 Refresh completed at: {datetime.now()}")
        print("\n📊 Summary:")
        print("  ✅ All existing data cleared")
        print("  ✅ Fresh data imported")
        print("  ✅ Passwords reset")
        print("\n🔑 Login Credentials:")
        print("  Username: Shruti, Password: Shruti")
        print("  Username: admin, Password: admin")
        print("  Username: Sid, Password: Sid")
        print("  And so on...")
        print("\n📝 Note: This script runs automatically on every deploy/restart!")
        
    except Exception as e:
        print(f"❌ Error during refresh: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
