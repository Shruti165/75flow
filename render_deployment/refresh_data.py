#!/usr/bin/env python3
"""
Data refresh script for Render deployment
This script can be run manually or automatically to refresh data
"""

import os
import sys
import django
from datetime import datetime, date

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
    
    # Comprehensive habit data (now global, no user field)
    all_habits_data = [
        # Reading habits
        {'name': 'Fiction', 'category': 'Reading'},
        {'name': 'Non-Fiction', 'category': 'Reading'},
        {'name': 'Spiritual', 'category': 'Reading'},
        {'name': 'Read 30 Minutes', 'category': 'Reading'},
        {'name': 'Journal Writing', 'category': 'Reading'},
        
        # Fitness habits
        {'name': 'Swim', 'category': 'Fitness'},
        {'name': 'Run', 'category': 'Fitness'},
        {'name': 'Dance', 'category': 'Fitness'},
        {'name': 'Yoga / Stretch', 'category': 'Fitness'},
        {'name': 'Gym', 'category': 'Fitness'},
        {'name': 'Go To The Park', 'category': 'Fitness'},
        {'name': 'Walk (7k/10k)', 'category': 'Fitness'},
        {'name': 'Football', 'category': 'Fitness'},
        {'name': 'Hand Stand / Pull Up / Pole Session', 'category': 'Fitness'},
        {'name': '7 Minute HIIT', 'category': 'Fitness'},
        {'name': 'Morning Workout', 'category': 'Fitness'},
        {'name': 'Evening Walk', 'category': 'Fitness'},
        
        # Nutrition habits
        {'name': 'Drink Matcha', 'category': 'Nutrition'},
        {'name': 'Consume Leaves', 'category': 'Nutrition'},
        {'name': 'Drink Coconut Water', 'category': 'Nutrition'},
        {'name': 'Take Supplements', 'category': 'Nutrition'},
        {'name': 'Have Fruits', 'category': 'Nutrition'},
        {'name': 'Drink Water', 'category': 'Nutrition'},
        {'name': 'Drink Vegetable Juice', 'category': 'Nutrition'},
        {'name': 'Prepare Meal / Cook Dinner', 'category': 'Nutrition'},
        {'name': 'Take Chia Seeds', 'category': 'Nutrition'},
        {'name': 'Drink 8 Glasses of Water', 'category': 'Nutrition'},
        {'name': 'Eat 5 Servings of Fruits/Veggies', 'category': 'Nutrition'},
        
        # Spiritual habits
        {'name': 'Chanting', 'category': 'Spiritual'},
        {'name': 'Meditate', 'category': 'Spiritual'},
        {'name': 'Meditation', 'category': 'Spiritual'},
        {'name': 'Journal', 'category': 'Spiritual'},
        {'name': 'Grounding', 'category': 'Spiritual'},
        {'name': 'Gratitude Practice', 'category': 'Spiritual'},
        {'name': 'Sleep Well / Binaural Beats', 'category': 'Spiritual'},
        {'name': 'Sungazing/Moongazing', 'category': 'Spiritual'},
        
        # Wealth habits
        {'name': 'Align High Income Job Offers', 'category': 'Wealth'},
        {'name': 'Optimise Linkedin', 'category': 'Wealth'},
        {'name': 'Get Leads', 'category': 'Wealth'},
        {'name': 'Passion Projects', 'category': 'Wealth'},
        {'name': 'Upskill', 'category': 'Wealth'},
        {'name': 'Create Content', 'category': 'Wealth'},
        {'name': 'Go To The Office', 'category': 'Wealth'},
        {'name': 'Deep Work', 'category': 'Wealth'},
        {'name': 'Learn About Finance', 'category': 'Wealth'},
        {'name': 'Track Expenses', 'category': 'Wealth'},
        
        # Fun habits
        {'name': 'Attend an Event', 'category': 'Fun'},
        {'name': 'Hackathons', 'category': 'Fun'},
        {'name': 'Gardening', 'category': 'Fun'},
        {'name': 'Community Meet', 'category': 'Fun'},
        {'name': 'Music', 'category': 'Fun'},
        {'name': 'Painitng Sketch', 'category': 'Fun'},
        {'name': 'DeclutterPlanning for Tomorrow', 'category': 'Fun'},
        {'name': 'Time with pets', 'category': 'Fun'},
        {'name': 'Social Service', 'category': 'Fun'},
        {'name': 'Social Connection', 'category': 'Fun'},
        {'name': 'Creative Activity', 'category': 'Fun'},
    ]
    
    # Import habits
    for habit_data in all_habits_data:
        try:
            # Get the user who created this habit (if specified)
            created_by = None
            if 'user' in habit_data and habit_data['user']:
                try:
                    created_by = User.objects.get(username=habit_data['user'])
                except User.DoesNotExist:
                    print(f"  ⚠️  User {habit_data['user']} not found, creating habit without creator")
            
            category = Category.objects.get(name=habit_data['category']) if habit_data['category'] else None
            
            # Check if habit already exists (global habits)
            existing_habits = Habit.objects.filter(name=habit_data['name'])
            if existing_habits.exists():
                print(f"  ℹ️  Habit already exists: {habit_data['name']}")
                continue
            
            # Create new global habit
            habit = Habit.objects.create(
                name=habit_data['name'],
                description=habit_data.get('description', ''),
                category=category,
                created_by=created_by,
                start_date=date.today()
            )
            
            print(f"  ✅ Created habit: {habit.name}")
            
        except Category.DoesNotExist:
            print(f"  ❌ Category not found: {habit_data['category']}")
        except Exception as e:
            print(f"  ❌ Error importing habit {habit_data.get('name', 'Unknown')}: {e}")
    
    print(f"  🎯 Total habits imported: {len(all_habits_data)}")

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

def main():
    """Main refresh function"""
    try:
        print("🔄 Starting data refresh...")
        print("=" * 50)
        
        # Clear existing data
        clear_existing_data()
        
        # Create admin user
        create_admin_if_not_exists()
        
        # Import fresh data
        import_categories()
        import_users()
        import_all_habits()
        reset_passwords()
        
        print("\n🎉 Data refresh completed successfully!")
        print("\n📝 Note: This script runs automatically on every deploy/restart!")
        
    except Exception as e:
        print(f"❌ Error during refresh: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
