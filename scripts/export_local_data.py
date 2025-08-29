#!/usr/bin/env python3
"""
Export local database data for Render deployment
This script exports users, profiles, categories, and habits from local database
"""

import os
import sys
import django
import json
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay
from django.core import serializers

def export_users():
    """Export all users with their profiles"""
    print("📤 Exporting users and profiles...")
    
    users_data = []
    for user in User.objects.all():
        try:
            profile = Profile.objects.get(user=user)
            user_data = {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat(),
                'profile': {
                    'bio': profile.bio,
                    'profile_image': str(profile.profile_image) if profile.profile_image else None,
                    'date_of_birth': profile.date_of_birth.isoformat() if profile.date_of_birth else None,
                    'email': profile.email,
                    'weekly_stats_enabled': profile.weekly_stats_enabled
                }
            }
            users_data.append(user_data)
            print(f"  ✅ Exported user: {user.username}")
        except Profile.DoesNotExist:
            print(f"  ⚠️  User {user.username} has no profile")
    
    return users_data

def export_categories():
    """Export all categories"""
    print("📤 Exporting categories...")
    
    categories_data = []
    for category in Category.objects.all():
        category_data = {
            'name': category.name,
            'color': category.color
        }
        categories_data.append(category_data)
        print(f"  ✅ Exported category: {category.name}")
    
    return categories_data

def export_habits():
    """Export all habits"""
    print("📤 Exporting habits...")
    
    habits_data = []
    for habit in Habit.objects.all():
        habit_data = {
            'name': habit.name,
            'description': habit.description,
            'category': habit.category.name if habit.category else None,
            'user': habit.user.username,
            'start_date': habit.start_date.isoformat()
        }
        habits_data.append(habit_data)
        print(f"  ✅ Exported habit: {habit.name}")
    
    return habits_data

def export_habit_days():
    """Export all habit completion records"""
    print("📤 Exporting habit completion records...")
    
    habit_days_data = []
    for habit_day in HabitDay.objects.all():
        habit_day_data = {
            'habit': habit_day.habit.name,
            'user': habit_day.habit.user.username,
            'date': habit_day.date.isoformat(),
            'completed': habit_day.completed,
            'day': habit_day.day
        }
        habit_days_data.append(habit_day_data)
    
    print(f"  ✅ Exported {len(habit_days_data)} habit completion records")
    return habit_days_data

def create_password_reset_script(users_data):
    """Create a script to reset passwords on Render"""
    print("📝 Creating password reset script...")
    
    script_content = """#!/usr/bin/env python3
\"\"\"
Reset user passwords on Render deployment
This script resets passwords to usernames for easy access
\"\"\"

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
    \"\"\"Reset all user passwords to their usernames\"\"\"
    print("🔐 Resetting user passwords...")
    
    for user in User.objects.all():
        try:
            user.set_password(user.username)
            user.save()
            print(f"  ✅ Reset password for: {user.username}")
        except Exception as e:
            print(f"  ❌ Error resetting password for {user.username}: {e}")
    
    print("\\n🎉 Password reset complete!")
    print("All users can now login with:")
    print("Username: their_username")
    print("Password: their_username")

if __name__ == "__main__":
    reset_passwords()
"""
    
    with open('render_deployment/reset_passwords.py', 'w') as f:
        f.write(script_content)
    
    print("  ✅ Created reset_passwords.py")

def create_import_script(users_data, categories_data, habits_data, habit_days_data):
    """Create a script to import data on Render"""
    print("📝 Creating data import script...")
    
    script_content = f"""#!/usr/bin/env python3
\"\"\"
Import local data into Render deployment
This script imports users, categories, and habits from local export
\"\"\"

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
from django.core.files.base import ContentFile

# Import data from local export
USERS_DATA = {json.dumps(users_data, indent=2)}

CATEGORIES_DATA = {json.dumps(categories_data, indent=2)}

HABITS_DATA = {json.dumps(habits_data, indent=2)}

HABIT_DAYS_DATA = {json.dumps(habit_days_data, indent=2)}

def import_categories():
    \"\"\"Import categories\"\"\"
    print("📥 Importing categories...")
    
    for cat_data in CATEGORIES_DATA:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={{
                'color': cat_data['color']
            }}
        )
        if created:
            print(f"  ✅ Created category: {{category.name}}")
        else:
            print(f"  ℹ️  Category already exists: {{category.name}}")

def import_users():
    \"\"\"Import users and profiles\"\"\"
    print("📥 Importing users and profiles...")
    
    for user_data in USERS_DATA:
        # Create or get user
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={{
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'is_staff': user_data['is_staff'],
                'is_superuser': user_data['is_superuser'],
                'is_active': user_data['is_active']
            }}
        )
        
        if created:
            print(f"  ✅ Created user: {{user.username}}")
        else:
            print(f"  ℹ️  User already exists: {{user.username}}")
        
                 # Create or update profile
         profile, profile_created = Profile.objects.get_or_create(
             user=user,
             defaults={{
                 'bio': user_data['profile']['bio'],
                 'date_of_birth': datetime.fromisoformat(user_data['profile']['date_of_birth']).date() if user_data['profile']['date_of_birth'] else None,
                 'email': user_data['profile']['email'],
                 'weekly_stats_enabled': user_data['profile']['weekly_stats_enabled']
             }}
         )
        
        if profile_created:
            print(f"    ✅ Created profile for: {{user.username}}")
        else:
            print(f"    ℹ️  Profile already exists for: {{user.username}}")

def import_habits():
    \"\"\"Import habits\"\"\"
    print("📥 Importing habits...")
    
    for habit_data in HABITS_DATA:
        try:
            user = User.objects.get(username=habit_data['user'])
            category = Category.objects.get(name=habit_data['category']) if habit_data['category'] else None
            
            habit, created = Habit.objects.get_or_create(
                name=habit_data['name'],
                user=user,
                defaults={{
                    'description': habit_data['description'],
                    'category': category
                }}
            )
            
            if created:
                print(f"  ✅ Created habit: {{habit.name}} for {{user.username}}")
            else:
                print(f"  ℹ️  Habit already exists: {{habit.name}} for {{user.username}}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {{habit_data['user']}}")
        except Category.DoesNotExist:
            print(f"  ❌ Category not found: {{habit_data['category']}}")

def import_habit_days():
    \"\"\"Import habit completion records\"\"\"
    print("📥 Importing habit completion records...")
    
    imported_count = 0
    for habit_day_data in HABIT_DAYS_DATA:
        try:
            habit = Habit.objects.get(name=habit_day_data['habit'])
            date = datetime.fromisoformat(habit_day_data['date']).date()
            
            habit_day, created = HabitDay.objects.get_or_create(
                habit=habit,
                date=date,
                defaults={{
                    'completed': habit_day_data['completed']
                }}
            )
            
            if created:
                imported_count += 1
                
        except Habit.DoesNotExist:
            print(f"  ❌ Habit not found: {{habit_day_data['habit']}}")
    
    print(f"  ✅ Imported {{imported_count}} habit completion records")

def main():
    \"\"\"Main import function\"\"\"
    print("🚀 Starting data import...")
    
    try:
        import_categories()
        print()
        import_users()
        print()
        import_habits()
        print()
        import_habit_days()
        print()
        
        print("🎉 Data import completed successfully!")
        print("\\n📊 Summary:")
        print(f"  Users: {{len(USERS_DATA)}}")
        print(f"  Categories: {{len(CATEGORIES_DATA)}}")
        print(f"  Habits: {{len(HABITS_DATA)}}")
        print(f"  Habit Days: {{len(HABIT_DAYS_DATA)}}")
        
    except Exception as e:
        print(f"❌ Error during import: {{e}}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
"""
    
    with open('render_deployment/import_local_data.py', 'w') as f:
        f.write(script_content)
    
    print("  ✅ Created import_local_data.py")

def main():
    """Main export function"""
    print("🚀 Starting local data export...")
    print("=" * 50)
    
    try:
        # Export all data
        users_data = export_users()
        print()
        
        categories_data = export_categories()
        print()
        
        habits_data = export_habits()
        print()
        
        habit_days_data = export_habit_days()
        print()
        
        # Create scripts
        create_password_reset_script(users_data)
        create_import_script(users_data, categories_data, habits_data, habit_days_data)
        
        # Save raw data
        export_data = {
            'exported_at': datetime.now().isoformat(),
            'users': users_data,
            'categories': categories_data,
            'habits': habits_data,
            'habit_days': habit_days_data
        }
        
        with open('render_deployment/local_data_export.json', 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print("=" * 50)
        print("🎉 Export completed successfully!")
        print(f"📊 Exported data:")
        print(f"  Users: {len(users_data)}")
        print(f"  Categories: {len(categories_data)}")
        print(f"  Habits: {len(habits_data)}")
        print(f"  Habit Days: {len(habit_days_data)}")
        print()
        print("📁 Files created:")
        print("  render_deployment/local_data_export.json")
        print("  render_deployment/import_local_data.py")
        print("  render_deployment/reset_passwords.py")
        print()
        print("🚀 Next steps:")
        print("  1. Push these files to GitHub")
        print("  2. Deploy to Render")
        print("  3. Run import_local_data.py on Render")
        print("  4. Run reset_passwords.py on Render")
        
    except Exception as e:
        print(f"❌ Error during export: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
