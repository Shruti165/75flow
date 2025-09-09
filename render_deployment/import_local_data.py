#!/usr/bin/env python3
"""
Import local data into Render deployment
This script imports users, categories, and habits from local export
"""

import os
import sys
import django
import json
from datetime import datetime, date
from django.utils import timezone

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay, Streak
from django.core.files.base import ContentFile

def load_export_data():
    """Load data from the JSON export file"""
    print("📁 Loading data from local_data_export.json...")
    
    try:
        with open('local_data_export.json', 'r') as f:
            data = json.load(f)
        
        print(f"  ✅ Loaded data from {data.get('export_date', 'unknown date')}")
        return data
    except FileNotFoundError:
        print("  ❌ local_data_export.json not found!")
        return None
    except json.JSONDecodeError as e:
        print(f"  ❌ Error parsing JSON: {e}")
        return None

def import_categories(export_data):
    """Import categories from export data"""
    print("📥 Importing categories...")
    
    categories_data = export_data.get('categories', [])
    imported_count = 0
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'color': cat_data['color']}
        )
        
        if created:
            print(f"  ✅ Created category: {category.name}")
            imported_count += 1
        else:
            print(f"  ℹ️  Category already exists: {category.name}")

    print(f"  ✅ Categories: {imported_count} new, {Category.objects.count()} total")
    return Category.objects.all()

def import_users(export_data):
    """Import users and profiles from export data"""
    print("📥 Importing users and profiles...")
    
    users_data = export_data.get('users', [])
    imported_count = 0
    
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
                'is_active': user_data['is_active'],
                'date_joined': timezone.datetime.fromisoformat(user_data['date_joined'].replace('Z', '+00:00'))
            }
        )
        
        if created:
            print(f"  ✅ Created user: {user.username}")
            imported_count += 1
        else:
            print(f"  ℹ️  User already exists: {user.username}")
        
        # Set password to username for easy access
        user.set_password(user.username)
        user.save()
        
        # Create or get profile
        profile_data = user_data.get('profile', {})
        profile, profile_created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'date_of_birth': timezone.datetime.fromisoformat(profile_data['date_of_birth']).date() if profile_data.get('date_of_birth') else None,
                'email': profile_data.get('email'),
                'weekly_stats_enabled': profile_data.get('weekly_stats_enabled', True)
            }
        )
        
        if profile_created:
            print(f"    ✅ Created profile for: {user.username}")
        else:
            print(f"    ℹ️  Profile already exists for: {user.username}")

    print(f"  ✅ Users: {imported_count} new, {User.objects.count()} total")
    return User.objects.all()

def import_habits(export_data):
    """Import habits from export data (now global)"""
    print("📥 Importing habits...")
    
    habits_data = export_data.get('habits', [])
    imported_count = 0
    
    for habit_data in habits_data:
        try:
            # Get the user who created this habit (if specified)
            created_by = None
            if habit_data.get('created_by'):
                try:
                    created_by = User.objects.get(username=habit_data['created_by'])
                except User.DoesNotExist:
                    print(f"  ⚠️  User {habit_data['created_by']} not found, creating habit without creator")
            
            category = None
            if habit_data.get('category'):
                try:
                    category = Category.objects.get(name=habit_data['category'])
                except Category.DoesNotExist:
                    print(f"  ⚠️  Category {habit_data['category']} not found")
            
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
                start_date=datetime.fromisoformat(habit_data['start_date']).date() if habit_data.get('start_date') else date.today()
            )
            
            print(f"  ✅ Created habit: {habit.name}")
            imported_count += 1
                
        except Exception as e:
            print(f"  ❌ Error creating habit {habit_data.get('name', 'Unknown')}: {e}")
    
    print(f"  ✅ Habits: {imported_count} new, {Habit.objects.count()} total")
    return Habit.objects.all()

def import_habit_days(export_data):
    """Import habit completion records from export data"""
    print("📥 Importing habit completion records...")
    
    habit_days_data = export_data.get('habit_days', [])
    imported_count = 0
    
    for habit_day_data in habit_days_data:
        try:
            habit = Habit.objects.filter(name=habit_day_data['habit']).first()
            if not habit:
                print(f"  ❌ Habit not found: {habit_day_data['habit']}")
                continue
                
            user = User.objects.get(username=habit_day_data['user'])
            
            # Convert date to day number (1-75)
            habit_date = datetime.fromisoformat(habit_day_data['date']).date()
            start_date = date(2025, 7, 15)  # Challenge start date
            day_number = (habit_date - start_date).days + 1
            
            # Only import if day is within challenge range
            if 1 <= day_number <= 75:
                habit_day, created = HabitDay.objects.get_or_create(
                    habit=habit,
                user=user,
                    day=day_number,
                defaults={
                        'completed': habit_day_data['completed']
                }
            )
            
            if created:
                    imported_count += 1
            else:
                print(f"  ⚠️  Skipping day {day_number} (outside challenge range)")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_day_data['user']}")
        except Exception as e:
            print(f"  ❌ Error importing habit day: {e}")
    
    print(f"  ✅ Habit Days: {imported_count} new, {HabitDay.objects.count()} total")
    return HabitDay.objects.all()

def import_streaks(export_data):
    """Import streak records from export data"""
    print("📥 Importing streak records...")
    
    streaks_data = export_data.get('streaks', [])
    imported_count = 0
    
    for streak_data in streaks_data:
        try:
            user = User.objects.get(username=streak_data['user'])
            
            streak, created = Streak.objects.get_or_create(
                user=user,
                defaults={
                    'current_streak': streak_data['current_streak'],
                    'best_streak': streak_data['best_streak'],
                    'last_reset_date': timezone.datetime.fromisoformat(streak_data['last_reset_date'].replace('Z', '+00:00')) if streak_data.get('last_reset_date') else timezone.now()
                }
            )
            
            if created:
                print(f"  ✅ Created streak for: {user.username}")
                imported_count += 1
            else:
                print(f"  ℹ️  Streak already exists for: {user.username}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {streak_data['user']}")
        except Exception as e:
            print(f"  ❌ Error creating streak: {e}")
    
    print(f"  ✅ Streaks: {imported_count} new, {Streak.objects.count()} total")
    return Streak.objects.all()

def main():
    """Main import function"""
    print("🚀 Starting data import from local_data_export.json...")
    print("=" * 60)
    
    # Load export data
    export_data = load_export_data()
    if not export_data:
        print("❌ Failed to load export data. Exiting.")
        return
    
    try:
        # Import all data
        import_categories(export_data)
        print()
        import_users(export_data)
        print()
        import_habits(export_data)
        print()
        import_habit_days(export_data)
        print()
        import_streaks(export_data)
        print()
        
        print("🎉 Data import completed successfully!")
        print("\n📊 Final Summary:")
        print(f"  Users: {User.objects.count()}")
        print(f"  Categories: {Category.objects.count()}")
        print(f"  Habits: {Habit.objects.count()}")
        print(f"  Habit Days: {HabitDay.objects.count()}")
        print(f"  Streaks: {Streak.objects.count()}")
        
    except Exception as e:
        print(f"❌ Error during import: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
