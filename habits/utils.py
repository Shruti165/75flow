from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth.models import User
from .models import Habit, HabitDay, Category, Notification, Achievement

def get_user_stats(user):
    """Get comprehensive user statistics"""
    today = timezone.now().date()
    challenge_start_date = date(2025, 7, 15)
    
    # Calculate current day of the challenge
    if today >= challenge_start_date:
        current_day = (today - challenge_start_date).days + 1
        if current_day > 75:
            current_day = 75
    else:
        current_day = 0
    
    # Get user's habits
    habits = Habit.objects.filter(user=user)
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
            for day_num in range(1, min(current_day + 1, 76)):
                completed_in_category = HabitDay.objects.filter(
                    habit__in=category_habits,
                    day=day_num,
                    completed=True
                ).count()
                
                if completed_in_category >= 2:
                    category_completed_days += 1
                    total_completed_days += 1
            
            category_total_days = min(current_day, 75)
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
    for day_num in range(1, min(current_day + 1, 76)):
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

def check_and_create_achievements(user):
    """Check if user has earned new achievements and create notifications"""
    stats = get_user_stats(user)
    achievements = Achievement.objects.all()
    
    for achievement in achievements:
        # Check if user has already been notified about this achievement
        existing_notification = Notification.objects.filter(
            user=user,
            notification_type='achievement',
            data__achievement_id=achievement.id
        ).exists()
        
        if not existing_notification and achievement.is_earned_by_user(user):
            # Create achievement notification
            Notification.objects.create(
                user=user,
                notification_type='achievement',
                title=f"🏆 Achievement Unlocked: {achievement.name}",
                message=achievement.description,
                data={'achievement_id': achievement.id, 'achievement_name': achievement.name}
            )

def create_streak_notification(user, streak_count):
    """Create streak milestone notifications"""
    streak_milestones = [3, 7, 14, 21, 30, 50, 75]
    
    if streak_count in streak_milestones:
        # Check if notification already exists
        existing_notification = Notification.objects.filter(
            user=user,
            notification_type='streak',
            data__streak_count=streak_count
        ).exists()
        
        if not existing_notification:
            messages = {
                3: "🔥 3-day streak! You're building momentum!",
                7: "🌟 7-day streak! A full week of consistency!",
                14: "💪 14-day streak! Two weeks strong!",
                21: "🎯 21-day streak! You're forming lasting habits!",
                30: "🏆 30-day streak! A full month of dedication!",
                50: "🚀 50-day streak! You're unstoppable!",
                75: "👑 75-day streak! You've completed the challenge!"
            }
            
            Notification.objects.create(
                user=user,
                notification_type='streak',
                title=f"🔥 {streak_count}-Day Streak!",
                message=messages.get(streak_count, f"Amazing {streak_count}-day streak!"),
                data={'streak_count': streak_count}
            )

def get_user_achievements(user):
    """Get all achievements earned by a user"""
    stats = get_user_stats(user)
    achievements = Achievement.objects.all()
    earned_achievements = []
    
    for achievement in achievements:
        if achievement.is_earned_by_user(user):
            earned_achievements.append(achievement)
    
    return earned_achievements

def get_unread_notifications_count(user):
    """Get count of unread notifications for a user"""
    return Notification.objects.filter(user=user, is_read=False).count()

def mark_notifications_as_read(user, notification_ids=None):
    """Mark notifications as read"""
    if notification_ids:
        Notification.objects.filter(user=user, id__in=notification_ids).update(is_read=True)
    else:
        Notification.objects.filter(user=user).update(is_read=True) 