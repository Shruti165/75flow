#!/usr/bin/env python3
"""
Complete production deployment script
This script sets up everything needed for production
"""

import os
import sys
import django
from datetime import datetime, date

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay, Streak
from django.utils import timezone

def create_categories():
    """Create all required categories"""
    print("📁 Creating categories...")
    
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
    
    print(f"📊 Categories: {created_count} new, {Category.objects.count()} total")
    return Category.objects.all()

def create_users():
    """Create all required users"""
    print("\n👥 Creating users...")
    
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
    users = {}
    
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
        
        users[user.username] = user
        
        # Create profile
        Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': '',
                'weekly_stats_enabled': True
            }
        )
        
        # Create streak record
        Streak.objects.get_or_create(
            user=user,
            defaults={
                'current_streak': 0,
                'best_streak': 0,
                'last_reset_date': timezone.now()
            }
        )
    
    print(f"📊 Users: {created_count} new, {User.objects.count()} total")
    return users

def create_habits(categories):
    """Create all required habits"""
    print("\n🎯 Creating habits...")
    
    habits_data = [
        # Fitness
        {'name': '7 Minute HIIT', 'category': 'Fitness', 'description': 'High-intensity interval training'},
        {'name': 'Dance', 'category': 'Fitness', 'description': 'Dancing for fitness and fun'},
        {'name': 'Evening Walk', 'category': 'Fitness', 'description': 'Evening walk for relaxation'},
        {'name': 'Football', 'category': 'Fitness', 'description': 'Playing football'},
        {'name': 'Go To The Park', 'category': 'Fitness', 'description': 'Visit the park for outdoor activity'},
        {'name': 'Gym', 'category': 'Fitness', 'description': 'Gym workout session'},
        {'name': 'Hand Stand / Pull Up / Pole Session', 'category': 'Fitness', 'description': 'Strength training exercises'},
        {'name': 'Morning Workout', 'category': 'Fitness', 'description': 'Morning exercise routine'},
        {'name': 'Run', 'category': 'Fitness', 'description': 'Running for cardio'},
        {'name': 'Swim', 'category': 'Fitness', 'description': 'Swimming workout'},
        {'name': 'Walk (7k/10k)', 'category': 'Fitness', 'description': 'Long distance walking'},
        {'name': 'Yoga / Stretch', 'category': 'Fitness', 'description': 'Yoga and stretching exercises'},
        
        # Nutrition
        {'name': 'Consume Leaves', 'category': 'Nutrition', 'description': 'Eat leafy green vegetables'},
        {'name': 'Drink 8 Glasses of Water', 'category': 'Nutrition', 'description': 'Stay hydrated with water'},
        {'name': 'Drink Coconut Water', 'category': 'Nutrition', 'description': 'Natural electrolyte drink'},
        {'name': 'Drink Matcha', 'category': 'Nutrition', 'description': 'Healthy green tea'},
        {'name': 'Drink Vegetable Juice', 'category': 'Nutrition', 'description': 'Fresh vegetable juice'},
        {'name': 'Drink Water', 'category': 'Nutrition', 'description': 'Regular water intake'},
        {'name': 'Eat 5 Servings of Fruits/Veggies', 'category': 'Nutrition', 'description': 'Daily fruit and vegetable intake'},
        {'name': 'Have Fruits', 'category': 'Nutrition', 'description': 'Eat fresh fruits'},
        {'name': 'Prepare Meal / Cook Dinner', 'category': 'Nutrition', 'description': 'Cook healthy meals'},
        {'name': 'Take Chia Seeds', 'category': 'Nutrition', 'description': 'Superfood nutrition'},
        {'name': 'Take Supplements', 'category': 'Nutrition', 'description': 'Essential vitamins and minerals'},
        
        # Reading
        {'name': 'Fiction', 'category': 'Reading', 'description': 'Read fiction books'},
        {'name': 'Journal Writing', 'category': 'Reading', 'description': 'Write in personal journal'},
        {'name': 'Non-Fiction', 'category': 'Reading', 'description': 'Read non-fiction books'},
        {'name': 'Read 30 Minutes', 'category': 'Reading', 'description': 'Daily reading habit'},
        {'name': 'Spiritual', 'category': 'Reading', 'description': 'Read spiritual texts'},
        
        # Wealth
        {'name': 'Align High Income Job Offers', 'category': 'Wealth', 'description': 'Work on career advancement'},
        {'name': 'Create Content', 'category': 'Wealth', 'description': 'Create valuable content'},
        {'name': 'Deep Work', 'category': 'Wealth', 'description': 'Focused work sessions'},
        {'name': 'Get Leads', 'category': 'Wealth', 'description': 'Generate business leads'},
        {'name': 'Go To The Office', 'category': 'Wealth', 'description': 'Professional work environment'},
        {'name': 'Learn About Finance', 'category': 'Wealth', 'description': 'Financial education'},
        {'name': 'Optimise Linkedin', 'category': 'Wealth', 'description': 'Professional networking'},
        {'name': 'Passion Projects', 'category': 'Wealth', 'description': 'Work on passion projects'},
        {'name': 'Track Expenses', 'category': 'Wealth', 'description': 'Monitor spending habits'},
        {'name': 'Upskill', 'category': 'Wealth', 'description': 'Learn new skills'},
        
        # Spiritual
        {'name': 'Chanting', 'category': 'Spiritual', 'description': 'Spiritual chanting practice'},
        {'name': 'Gratitude Practice', 'category': 'Spiritual', 'description': 'Daily gratitude journaling'},
        {'name': 'Grounding', 'category': 'Spiritual', 'description': 'Grounding meditation'},
        {'name': 'Journal', 'category': 'Spiritual', 'description': 'Spiritual journaling'},
        {'name': 'Meditate', 'category': 'Spiritual', 'description': 'Meditation practice'},
        {'name': 'Meditation', 'category': 'Spiritual', 'description': 'Mindfulness meditation'},
        {'name': 'Sleep Well / Binaural Beats', 'category': 'Spiritual', 'description': 'Quality sleep with binaural beats'},
        {'name': 'Sungazing/Moongazing', 'category': 'Spiritual', 'description': 'Sun and moon gazing practice'},
        
        # Fun
        {'name': 'Attend an Event', 'category': 'Fun', 'description': 'Attend social events'},
        {'name': 'Community Meet', 'category': 'Fun', 'description': 'Community gatherings'},
        {'name': 'Creative Activity', 'category': 'Fun', 'description': 'Creative pursuits'},
        {'name': 'Dance', 'category': 'Fun', 'description': 'Dancing for fun'},
        {'name': 'DeclutterPlanning for Tomorrow', 'category': 'Fun', 'description': 'Declutter and plan ahead'},
        {'name': 'Gardening', 'category': 'Fun', 'description': 'Garden and plant care'},
        {'name': 'Hackathons', 'category': 'Fun', 'description': 'Participate in hackathons'},
        {'name': 'Music', 'category': 'Fun', 'description': 'Listen to or create music'},
        {'name': 'Painitng Sketch', 'category': 'Fun', 'description': 'Artistic painting and sketching'},
        {'name': 'Social Connection', 'category': 'Fun', 'description': 'Social interactions'},
        {'name': 'Social Service', 'category': 'Fun', 'description': 'Community service'},
        {'name': 'Time with pets', 'category': 'Fun', 'description': 'Spend time with pets'},
    ]
    
    created_count = 0
    category_map = {cat.name: cat for cat in categories}
    
    for habit_data in habits_data:
        category = category_map.get(habit_data['category'])
        
        # Check if habit already exists
        existing_habits = Habit.objects.filter(name=habit_data['name'])
        if existing_habits.exists():
            print(f"  ℹ️  Habit already exists: {habit_data['name']}")
            continue
            
        # Create new habit
        habit = Habit.objects.create(
            name=habit_data['name'],
            category=category,
            description=habit_data['description'],
            start_date=date(2025, 7, 15)
        )
        
        print(f"  ✅ Created habit: {habit.name}")
        created_count += 1
    
    print(f"📊 Habits: {created_count} new, {Habit.objects.count()} total")

def main():
    """Main deployment function"""
    print("🚀 Starting complete production deployment...")
    print("=" * 60)
    
    try:
        # Create categories
        categories = create_categories()
        
        # Create users
        users = create_users()
        
        # Create habits
        create_habits(categories)
        
        print("\n🎉 Production deployment completed successfully!")
        print("=" * 60)
        print("📊 Final Summary:")
        print(f"  👥 Users: {User.objects.count()}")
        print(f"  📁 Categories: {Category.objects.count()}")
        print(f"  🎯 Habits: {Habit.objects.count()}")
        print(f"  📊 Profiles: {Profile.objects.count()}")
        print(f"  🔥 Streaks: {Streak.objects.count()}")
        print("\n✅ All users can now login with username as password!")
        
    except Exception as e:
        print(f"\n❌ Error during deployment: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
