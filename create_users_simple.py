#!/usr/bin/env python3
"""
Simple user creation script for production
This script creates users without any complex dependencies
"""

import os
import sys
import django
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, Streak
from django.utils import timezone

def create_users():
    """Create all required users"""
    print("🚀 Creating users for production...")
    
    # User data
    users_data = [
        {'username': 'shruti', 'email': 'shruti@example.com', 'first_name': 'Shruti', 'last_name': 'Gupta'},
        {'username': 'sidd', 'email': 'sidd@example.com', 'first_name': 'Sidd', 'last_name': 'Kumar'},
        {'username': 'sanju', 'email': 'sanju@example.com', 'first_name': 'Sanju', 'last_name': 'Patel'},
        {'username': 'mahi', 'email': 'mahi@example.com', 'first_name': 'Mahi', 'last_name': 'Singh'},
        {'username': 'anurag', 'email': 'anurag@example.com', 'first_name': 'Anurag', 'last_name': 'Sharma'},
        {'username': 'pooja', 'email': 'pooja@example.com', 'first_name': 'Pooja', 'last_name': 'Verma'},
        {'username': 'sachin', 'email': 'sachin@example.com', 'first_name': 'Sachin', 'last_name': 'Yadav'},
        {'username': 'defni', 'email': 'defni@example.com', 'first_name': 'Defni', 'last_name': 'Kumar'},
    ]
    
    created_count = 0
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'is_active': True,
                'date_joined': timezone.now()
            }
        )
        
        if created:
            # Set password same as username
            user.set_password(user_data['username'])
            user.save()
            print(f"  ✅ Created user: {user.username}")
            created_count += 1
        else:
            print(f"  ℹ️  User already exists: {user.username}")
        
        # Create profile
        profile, profile_created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': '',
                'weekly_stats_enabled': True
            }
        )
        
        if profile_created:
            print(f"  ✅ Created profile for: {user.username}")
        
        # Create streak record
        streak, streak_created = Streak.objects.get_or_create(
            user=user,
            defaults={
                'current_streak': 0,
                'best_streak': 0,
                'last_reset_date': timezone.now()
            }
        )
        
        if streak_created:
            print(f"  ✅ Created streak record for: {user.username}")
    
    print(f"\n🎉 User creation completed!")
    print(f"📊 Summary: {created_count} new users created")
    print(f"📊 Total users: {User.objects.count()}")
    print(f"📊 Total profiles: {Profile.objects.count()}")
    print(f"📊 Total streaks: {Streak.objects.count()}")

def create_categories():
    """Create default categories"""
    print("\n📁 Creating categories...")
    
    categories_data = [
        {'name': 'Fitness', 'color': '#86efac', 'description': 'Exercise and physical activity'},
        {'name': 'Nutrition', 'color': '#fca5a5', 'description': 'Healthy eating habits'},
        {'name': 'Reading', 'color': '#667eea', 'description': 'Reading books and articles'},
        {'name': 'Wealth', 'color': '#7dd3fc', 'description': 'Financial planning and investment'},
        {'name': 'Spiritual', 'color': '#c084fc', 'description': 'Meditation and mindfulness'},
        {'name': 'Fun', 'color': '#fbbf24', 'description': 'Hobbies and entertainment'},
    ]
    
    created_count = 0
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'color': cat_data['color'],
                'description': cat_data['description']
            }
        )
        
        if created:
            print(f"  ✅ Created category: {category.name}")
            created_count += 1
        else:
            print(f"  ℹ️  Category already exists: {category.name}")
    
    print(f"📊 Categories created: {created_count}")
    print(f"📊 Total categories: {Category.objects.count()}")

def main():
    """Main function"""
    print("🚀 Starting simple user creation for production...")
    print("=" * 50)
    
    try:
        create_categories()
        create_users()
        print("\n✅ All operations completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
