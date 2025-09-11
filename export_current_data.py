#!/usr/bin/env python3
"""
Export current database data for production deployment
"""

import os
import sys
import django
import json
from datetime import datetime, date
from django.utils import timezone

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay, Streak, Feedback, BugReport

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
    
    print(f"  ✅ Exported {len(categories_data)} categories")
    return categories_data

def export_users():
    """Export all users and their profiles"""
    print("📤 Exporting users and profiles...")
    users_data = []
    
    for user in User.objects.all():
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = None
        
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined.isoformat() if user.date_joined else None,
            'profile': {
                'bio': profile.bio if profile else '',
                'email': profile.email if profile else None,
                'weekly_stats_enabled': profile.weekly_stats_enabled if profile else True,
                'date_of_birth': profile.date_of_birth.isoformat() if profile and profile.date_of_birth else None
            } if profile else None
        }
        users_data.append(user_data)
    
    print(f"  ✅ Exported {len(users_data)} users")
    return users_data

def export_habits():
    """Export all habits"""
    print("📤 Exporting habits...")
    habits_data = []
    
    for habit in Habit.objects.all():
        habit_data = {
            'name': habit.name,
            'description': habit.description or '',
            'category': habit.category.name if habit.category else None,
            'created_by': habit.created_by.username if habit.created_by else None,
            'start_date': habit.start_date.isoformat() if habit.start_date else None
        }
        habits_data.append(habit_data)
    
    print(f"  ✅ Exported {len(habits_data)} habits")
    return habits_data

def export_habit_days():
    """Export all habit completion records"""
    print("📤 Exporting habit completion records...")
    habit_days_data = []
    
    for habit_day in HabitDay.objects.all():
        habit_day_data = {
            'user': habit_day.user.username,
            'habit': habit_day.habit.name,
            'day': habit_day.day,
            'completed': habit_day.completed,
            'date': habit_day.date.isoformat() if habit_day.date else None
        }
        habit_days_data.append(habit_day_data)
    
    print(f"  ✅ Exported {len(habit_days_data)} habit completion records")
    return habit_days_data

def export_streaks():
    """Export all streak records"""
    print("📤 Exporting streak records...")
    streaks_data = []
    
    for streak in Streak.objects.all():
        streak_data = {
            'user': streak.user.username,
            'current_streak': streak.current_streak,
            'best_streak': streak.best_streak,
            'last_reset_date': streak.last_reset_date.isoformat() if streak.last_reset_date else None
        }
        streaks_data.append(streak_data)
    
    print(f"  ✅ Exported {len(streaks_data)} streak records")
    return streaks_data

def export_feedback():
    """Export all feedback records"""
    print("📤 Exporting feedback records...")
    feedback_data = []
    
    for feedback in Feedback.objects.all():
        feedback_data_item = {
            'user': feedback.user.username,
            'title': feedback.title,
            'message': feedback.message,
            'created_at': feedback.created_at.isoformat() if feedback.created_at else None
        }
        feedback_data.append(feedback_data_item)
    
    print(f"  ✅ Exported {len(feedback_data)} feedback records")
    return feedback_data

def export_bug_reports():
    """Export all bug report records"""
    print("📤 Exporting bug report records...")
    bug_reports_data = []
    
    for bug_report in BugReport.objects.all():
        bug_report_data = {
            'user': bug_report.user.username,
            'title': bug_report.title,
            'description': bug_report.description,
            'steps_to_reproduce': bug_report.steps_to_reproduce,
            'expected_behavior': bug_report.expected_behavior,
            'actual_behavior': bug_report.actual_behavior,
            'created_at': bug_report.created_at.isoformat() if bug_report.created_at else None
        }
        bug_reports_data.append(bug_report_data)
    
    print(f"  ✅ Exported {len(bug_reports_data)} bug report records")
    return bug_reports_data

def main():
    """Main export function"""
    print("🚀 Starting database export for production deployment...")
    print("=" * 60)
    
    # Export all data
    categories_data = export_categories()
    users_data = export_users()
    habits_data = export_habits()
    habit_days_data = export_habit_days()
    streaks_data = export_streaks()
    feedback_data = export_feedback()
    bug_reports_data = export_bug_reports()
    
    # Create comprehensive export data
    export_data = {
        'timestamp': datetime.now().isoformat(),
        'export_info': {
            'total_categories': len(categories_data),
            'total_users': len(users_data),
            'total_habits': len(habits_data),
            'total_habit_days': len(habit_days_data),
            'total_streaks': len(streaks_data),
            'total_feedback': len(feedback_data),
            'total_bug_reports': len(bug_reports_data)
        },
        'categories': categories_data,
        'users': users_data,
        'habits': habits_data,
        'habit_days': habit_days_data,
        'streaks': streaks_data,
        'feedback': feedback_data,
        'bug_reports': bug_reports_data
    }
    
    # Save to JSON file
    export_filename = 'local_data_export.json'
    with open(export_filename, 'w') as f:
        json.dump(export_data, f, indent=2, default=str)
    
    # Also save to render_deployment directory
    render_export_filename = 'render_deployment/local_data_export.json'
    with open(render_export_filename, 'w') as f:
        json.dump(export_data, f, indent=2, default=str)
    
    print("\n🎉 Export completed successfully!")
    print("=" * 60)
    print(f"📁 Files created:")
    print(f"  - {export_filename}")
    print(f"  - {render_export_filename}")
    print(f"\n📊 Export summary:")
    print(f"  Categories: {len(categories_data)}")
    print(f"  Users: {len(users_data)}")
    print(f"  Habits: {len(habits_data)}")
    print(f"  Habit Days: {len(habit_days_data)}")
    print(f"  Streaks: {len(streaks_data)}")
    print(f"  Feedback: {len(feedback_data)}")
    print(f"  Bug Reports: {len(bug_reports_data)}")
    print(f"\n✅ Ready for production deployment!")

if __name__ == "__main__":
    main()
