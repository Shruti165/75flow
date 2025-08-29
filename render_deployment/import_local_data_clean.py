#!/usr/bin/env python3
"""
Import local data into Render deployment
This script imports users, categories, and habits from local export
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

# Import data from local export
USERS_DATA = [
    {
        "username": "Sid",
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
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
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
        "profile": {
            "bio": "",
            "profile_image": None,
            "date_of_birth": None,
            "email": None,
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
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
        "profile": {
            "bio": "",
            "profile_image": None,
            "date_of_birth": None,
            "email": None,
            "weekly_stats_enabled": True
        }
    },
    {
        "username": "admin",
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_staff": True,
        "is_superuser": True,
        "is_active": True,
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
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
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
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
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
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
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
        "date_joined": "2025-08-29T07:15:29.000000+00:00",
        "profile": {
            "bio": "",
            "profile_image": None,
            "date_of_birth": None,
            "email": None,
            "weekly_stats_enabled": True
        }
    }
]

CATEGORIES_DATA = [
    {"name": "Reading", "color": "#2196f3"},
    {"name": "Fitness", "color": "#2196f3"},
    {"name": "Nutrition", "color": "#2196f3"},
    {"name": "Wealth", "color": "#2196f3"},
    {"name": "Spiritual", "color": "#2196f3"},
    {"name": "Fun", "color": "#2196f3"}
]

def import_categories():
    """Import categories"""
    print("📥 Importing categories...")
    
    for cat_data in CATEGORIES_DATA:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'color': cat_data['color']
            }
        )
        if created:
            print(f"  ✅ Created category: {category.name}")
        else:
            print(f"  ℹ️  Category already exists: {category.name}")

def import_users():
    """Import users and profiles"""
    print("📥 Importing users and profiles...")
    
    for user_data in USERS_DATA:
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

def create_sample_habits():
    """Create sample habits for each user"""
    print("📥 Creating sample habits...")
    
    # Get categories
    reading_cat = Category.objects.get(name='Reading')
    fitness_cat = Category.objects.get(name='Fitness')
    nutrition_cat = Category.objects.get(name='Nutrition')
    wealth_cat = Category.objects.get(name='Wealth')
    spiritual_cat = Category.objects.get(name='Spiritual')
    fun_cat = Category.objects.get(name='Fun')
    
    # Sample habits for each user
    sample_habits = [
        # Shruti's habits
        {'user': 'Shruti', 'name': 'Read 30 minutes', 'category': reading_cat},
        {'user': 'Shruti', 'name': 'Morning workout', 'category': fitness_cat},
        {'user': 'Shruti', 'name': 'Drink 8 glasses water', 'category': nutrition_cat},
        {'user': 'Shruti', 'name': 'Track expenses', 'category': wealth_cat},
        {'user': 'Shruti', 'name': 'Meditation', 'category': spiritual_cat},
        {'user': 'Shruti', 'name': 'Play guitar', 'category': fun_cat},
        
        # Admin's habits
        {'user': 'admin', 'name': 'Gym workout', 'category': fitness_cat},
        {'user': 'admin', 'name': 'Drink water', 'category': nutrition_cat},
        {'user': 'admin', 'name': 'Track investments', 'category': wealth_cat},
        {'user': 'admin', 'name': 'Prayer time', 'category': spiritual_cat},
        {'user': 'admin', 'name': 'Photography', 'category': fun_cat},
        
        # Other users get basic habits
        {'user': 'Sid', 'name': 'Read business books', 'category': reading_cat},
        {'user': 'Sid', 'name': 'Running', 'category': fitness_cat},
        {'user': 'Sid', 'name': 'Eat healthy meals', 'category': nutrition_cat},
        {'user': 'Sid', 'name': 'Save money', 'category': wealth_cat},
        {'user': 'Sid', 'name': 'Coding practice', 'category': fun_cat},
    ]
    
    for habit_data in sample_habits:
        try:
            user = User.objects.get(username=habit_data['user'])
            
            habit, created = Habit.objects.get_or_create(
                name=habit_data['name'],
                user=user,
                defaults={
                    'description': f"Daily {habit_data['name'].lower()}",
                    'category': habit_data['category']
                }
            )
            
            if created:
                print(f"  ✅ Created habit: {habit.name} for {user.username}")
            else:
                print(f"  ℹ️  Habit already exists: {habit.name} for {user.username}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_data['user']}")

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
    """Main import function"""
    print("🚀 Starting data import...")
    
    try:
        import_categories()
        print()
        import_users()
        print()
        create_sample_habits()
        print()
        reset_passwords()
        print()
        
        print("🎉 Data import completed successfully!")
        print("\n📊 Summary:")
        print(f"  Users: {len(USERS_DATA)}")
        print(f"  Categories: {len(CATEGORIES_DATA)}")
        print("\n🔑 Login Credentials:")
        print("  Username: Shruti, Password: Shruti")
        print("  Username: admin, Password: admin")
        print("  Username: Sid, Password: Sid")
        print("  And so on...")
        
    except Exception as e:
        print(f"❌ Error during import: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
