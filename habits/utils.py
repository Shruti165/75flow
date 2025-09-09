from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.conf import settings
from .models import Habit, HabitDay, Category, Streak

def get_challenge_start_date():
    """Get the challenge start date from settings"""
    return date.fromisoformat(settings.CHALLENGE_START_DATE)

def get_challenge_duration():
    """Get the challenge duration in days from settings"""
    return settings.CHALLENGE_DURATION_DAYS

def get_user_stats(user):
    """Get comprehensive user statistics"""
    today = timezone.now().date()
    challenge_start_date = get_challenge_start_date()
    challenge_duration = get_challenge_duration()
    
    # Calculate current day of the challenge
    if today >= challenge_start_date:
        current_day = (today - challenge_start_date).days + 1
        if current_day > challenge_duration:
            current_day = challenge_duration
    else:
        current_day = 0
    
    # Get all habits (now global)
    habits = Habit.objects.all()
    total_habits = habits.count()
    
    # Calculate category-based scoring
    total_completed_days = 0
    total_possible_days = 0
    completed_categories = 0
    
    # Get category-specific stats
    category_stats = []
    for category in Category.objects.all():
        category_habits = habits.filter(category=category)
        category_habit_count = category_habits.count()
        
        if category_habit_count > 0:
            # Calculate days where user completed at least 2 activities from this category
            category_completed_days = 0
            for day_num in range(1, min(current_day + 1, challenge_duration + 1)):
                completed_in_category = HabitDay.objects.filter(
                    habit__in=category_habits,
                    day=day_num,
                    completed=True
                ).count()
                
                if completed_in_category >= 2:
                    category_completed_days += 1
                    total_completed_days += 1
            
            category_total_days = min(current_day, challenge_duration)
            total_possible_days += category_total_days
            
            category_percentage = (category_completed_days / category_total_days * 100) if category_total_days > 0 else 0
            
            if category_completed_days > 0:
                completed_categories += 1
            
            category_stats.append({
                'category': category,
                'completed': category_completed_days,
                'total': category_total_days,
                'percentage': category_percentage,
                'habit_count': category_habit_count
            })
    
    # Overall completion percentage
    overall_completion_percentage = (total_completed_days / total_possible_days * 100) if total_possible_days > 0 else 0
    
    # Calculate current streak
    current_streak = 0
    for day_num in range(current_day, 0, -1):
        day_categories_completed = 0
        day_total_categories = 0
        
        for category in Category.objects.all():
            category_habits = habits.filter(category=category)
            if category_habits.exists():
                day_total_categories += 1
                completed_in_category = HabitDay.objects.filter(
                    habit__in=category_habits,
                    day=day_num,
                    completed=True
                ).count()
                
                if completed_in_category >= 2:
                    day_categories_completed += 1
        
        if day_categories_completed > 0:
            current_streak += 1
        else:
            break
    
    # Calculate best streak
    best_streak = 0
    temp_streak = 0
    for day_num in range(1, min(current_day + 1, challenge_duration + 1)):
        day_categories_completed = 0
        
        for category in Category.objects.all():
            category_habits = habits.filter(category=category)
            if category_habits.exists():
                completed_in_category = HabitDay.objects.filter(
                    habit__in=category_habits,
                    day=day_num,
                    completed=True
                ).count()
                
                if completed_in_category >= 2:
                    day_categories_completed += 1
        
        if day_categories_completed > 0:
            temp_streak += 1
            best_streak = max(best_streak, temp_streak)
        else:
            temp_streak = 0
    
    return {
        'total_habits': total_habits,
        'total_completed_days': total_completed_days,
        'total_possible_days': total_possible_days,
        'overall_completion_percentage': overall_completion_percentage,
        'current_streak': current_streak,
        'best_streak': best_streak,
        'completed_categories': completed_categories,
        'total_categories': Category.objects.count(),
        'category_stats': category_stats,
        'current_day': current_day,
    }