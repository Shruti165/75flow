from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.http import JsonResponse
from .models import Habit, HabitDay, Category, Profile
from .forms import CategoryForm, HabitForm, ProfileForm

# Create your views here.

@login_required
def home(request):
    """Home page view for logged in users"""
    user_categories = Category.objects.all()
    user_habits = Habit.objects.filter(user=request.user)
    context = {
        'categories': user_categories,
        'habits': user_habits,
        'user': request.user
    }
    return render(request, 'habits/home.html', context)

@login_required
def profile(request):
    """User profile view for editing profile information"""
    # Ensure user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Profile updated successfully!')
            return redirect('habits:home')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'habits/profile.html', context)

@login_required
def scoreboard(request):
    """Scoreboard showing all participants' progress with daily, weekly, and overall stats"""
    today = timezone.now().date()
    challenge_start_date = date(2025, 7, 15)  # July 15th, 2025
    
    # Calculate current day of the challenge
    if today >= challenge_start_date:
        current_day = (today - challenge_start_date).days + 1
        if current_day > 75:
            current_day = 75  # Cap at 75 days
    else:
        current_day = 0  # Challenge hasn't started yet
    
    # Calculate week start and end based on challenge start date
    days_since_start = (today - challenge_start_date).days if today >= challenge_start_date else 0
    current_week = (days_since_start // 7) + 1
    week_start_day = ((current_week - 1) * 7) + 1
    week_end_day = min(week_start_day + 6, 75)
    
    # Get all users with their habit statistics
    users_with_stats = []
    
    for user in User.objects.all():
        # Get user's habits
        habits = Habit.objects.filter(user=user)
        total_habits = habits.count()
        
        # Calculate category-based scoring (2 activities per category = full points)
        total_completed_days = 0
        total_possible_days = 0
        
        # Get category-specific stats with new scoring
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
                    
                    # If user completed 2 or more activities from this category, count as full day
                    if completed_in_category >= 2:
                        category_completed_days += 1
                        total_completed_days += 1
                
                # Each category contributes 1 day per actual day (not per habit)
                category_total_days = min(current_day, 75)
                total_possible_days += category_total_days
                
                category_percentage = (category_completed_days / category_total_days * 100) if category_total_days > 0 else 0
                
                category_stats.append({
                    'category': category,
                    'completed': category_completed_days,
                    'total': category_total_days,
                    'percentage': category_percentage,
                    'habit_count': category_habit_count
                })
        
        # Overall completion percentage based on category days
        overall_completion_percentage = (total_completed_days / total_possible_days * 100) if total_possible_days > 0 else 0
        
        # Weekly stats (current week) - category-based
        weekly_completed = 0
        weekly_possible = 0
        for category in Category.objects.all():
            category_habits = habits.filter(category=category)
            if category_habits.exists():
                for day_num in range(week_start_day, week_end_day + 1):
                    completed_in_category = HabitDay.objects.filter(
                        habit__in=category_habits,
                        day=day_num,
                        completed=True
                    ).count()
                    
                    if completed_in_category >= 2:
                        weekly_completed += 1
                    weekly_possible += 1
        
        weekly_completion_percentage = (weekly_completed / weekly_possible * 100) if weekly_possible > 0 else 0
        
        # Daily stats (today's categories completed)
        daily_completed_categories = 0
        daily_total_categories = 0
        for category in Category.objects.all():
            category_habits = habits.filter(category=category)
            if category_habits.exists():
                daily_total_categories += 1
                completed_in_category = HabitDay.objects.filter(
                    habit__in=category_habits,
                    day=current_day,
                    completed=True
                ).count()
                
                if completed_in_category >= 2:
                    daily_completed_categories += 1
        
        daily_completion_percentage = (daily_completed_categories / daily_total_categories * 100) if daily_total_categories > 0 else 0
        
        # Calculate current streak (category-based)
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
        
        users_with_stats.append({
            'user': user,
            'total_habits': total_habits,
            'total_completed_days': total_completed_days,
            'overall_completion_percentage': overall_completion_percentage,
            'weekly_completed': weekly_completed,
            'weekly_completion_percentage': weekly_completion_percentage,
            'daily_completed': daily_completed_categories,
            'daily_completion_percentage': daily_completion_percentage,
            'current_streak': current_streak,
            'category_stats': category_stats,
            'total_categories': daily_total_categories
        })
    
    # Sort by different criteria
    overall_rankings = sorted(users_with_stats, key=lambda x: x['overall_completion_percentage'], reverse=True)
    weekly_rankings = sorted(users_with_stats, key=lambda x: x['weekly_completion_percentage'], reverse=True)
    daily_rankings = sorted(users_with_stats, key=lambda x: x['daily_completion_percentage'], reverse=True)
    streak_rankings = sorted(users_with_stats, key=lambda x: x['current_streak'], reverse=True)
    
    # Find category winners
    category_winners = {}
    for category in Category.objects.all():
        best_user = None
        best_percentage = 0
        
        for user_stat in users_with_stats:
            for cat_stat in user_stat['category_stats']:
                if cat_stat['category'] == category and cat_stat['percentage'] > best_percentage:
                    best_percentage = cat_stat['percentage']
                    best_user = user_stat['user']
        
        if best_user:
            category_winners[category] = {
                'user': best_user,
                'percentage': best_percentage
            }
    
    # Create category breakdown data structure
    category_breakdown = []
    for category in Category.objects.all():
        category_users = []
        total_participants = 0
        total_days = 0
        total_completed = 0
        
        for user_stat in users_with_stats:
            for cat_stat in user_stat['category_stats']:
                if cat_stat['category'] == category:
                    # Calculate remaining days
                    remaining_days = cat_stat['total'] - cat_stat['completed']
                    
                    category_users.append({
                        'user': user_stat['user'],
                        'completed': cat_stat['completed'],
                        'total': cat_stat['total'],
                        'percentage': cat_stat['percentage'],
                        'habit_count': cat_stat['habit_count'],
                        'remaining_days': remaining_days
                    })
                    total_participants += 1
                    total_days += cat_stat['total']
                    total_completed += cat_stat['completed']
                    break
        
        # Sort users by percentage for this category
        category_users.sort(key=lambda x: x['percentage'], reverse=True)
        
        # Get the best performer for this category
        best_performer = category_users[0] if category_users else None
        
        category_breakdown.append({
            'category': category,
            'users': category_users,
            'total_participants': total_participants,
            'total_days': total_days,
            'total_completed': total_completed,
            'best_performer': best_performer,
            'winner': category_winners.get(category)
        })
    
    # Calculate challenge statistics
    challenge_stats = {
        'total_participants': len(users_with_stats),
        'total_habits_across_all': sum(u['total_habits'] for u in users_with_stats),
        'total_days_completed': sum(u['total_completed_days'] for u in users_with_stats),
        'average_completion': sum(u['overall_completion_percentage'] for u in users_with_stats) / len(users_with_stats) if users_with_stats else 0,
        'best_streak': max(u['current_streak'] for u in users_with_stats) if users_with_stats else 0,
        'current_day': current_day,
        'current_week': current_week,
        'week_start_day': week_start_day,
        'week_end_day': week_end_day,
        'challenge_start_date': challenge_start_date
    }
    
    # Add category statistics to each user for the new breakdown
    for user_stat in users_with_stats:
        user_stat['category_stats'] = []
        for category in Category.objects.all():
            # Get user's habits for this category
            user_habits = Habit.objects.filter(user=user_stat['user'], category=category)
            
            # Find this user's stats for this category
            category_found = False
            for cat_stat in user_stat.get('category_stats', []):
                if cat_stat['category'] == category:
                    # Calculate remaining days
                    remaining_days = 75 - cat_stat['completed']
                    user_stat['category_stats'].append({
                        'category': category,
                        'completed': cat_stat['completed'],
                        'total': 75,  # Always 75 days
                        'percentage': cat_stat['percentage'],
                        'remaining': remaining_days,
                        'habits': [
                            {
                                'id': habit.id,
                                'name': habit.name,
                                'description': habit.description,
                                'start_date': habit.start_date
                            }
                            for habit in user_habits
                        ],
                        'habit_count': user_habits.count()
                    })
                    category_found = True
                    break
            
            if not category_found:
                # User has no stats for this category
                user_stat['category_stats'].append({
                    'category': category,
                    'completed': 0,
                    'total': 75,
                    'percentage': 0.0,
                    'remaining': 75,
                    'habits': [
                        {
                            'id': habit.id,
                            'name': habit.name,
                            'description': habit.description,
                            'start_date': habit.start_date
                        }
                        for habit in user_habits
                    ],
                    'habit_count': user_habits.count()
                })
    
    # Prepare habit completion data for 75-day viewer
    habit_completion_data = {}
    for user in User.objects.all():
        # Ensure user has a profile
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)
            
        user_habits = Habit.objects.filter(user=user)
        user_completions = {}
        
        for day_num in range(1, 76):
            day_completions = HabitDay.objects.filter(
                habit__user=user,
                day=day_num,
                completed=True
            ).select_related('habit')
            
            user_completions[day_num] = [
                {
                    'id': completion.habit.id,
                    'name': completion.habit.name,
                    'category': completion.habit.category.name if completion.habit.category else 'Uncategorized'
                }
                for completion in day_completions
            ]
        
        habit_completion_data[user.id] = {
            'habits': [
                {
                    'id': habit.id,
                    'name': habit.name,
                    'category': habit.category.name if habit.category else 'Uncategorized'
                }
                for habit in user_habits
            ],
            'daily_completions': user_completions
        }
    
    context = {
        'users_with_stats': users_with_stats,
        'overall_rankings': overall_rankings,
        'weekly_rankings': weekly_rankings,
        'daily_rankings': daily_rankings,
        'streak_rankings': streak_rankings,
        'category_winners': category_winners,
        'category_breakdown': category_breakdown,
        'categories': Category.objects.all(),
        'challenge_stats': challenge_stats,
        'today': today,
        'habit_completion_data': habit_completion_data
    }
    return render(request, 'habits/scoreboard.html', context)

@login_required
def daily_tracking(request):
    """Daily habit tracking page where users can check off completed habits"""
    today = timezone.now().date()
    challenge_start_date = date(2025, 7, 15)  # July 15th, 2025
    
    # Calculate current day of the challenge
    if today >= challenge_start_date:
        current_day = (today - challenge_start_date).days + 1
        if current_day > 75:
            current_day = 75  # Cap at 75 days
    else:
        current_day = 0  # Challenge hasn't started yet
    
    # Get user's habits organized by category
    user_categories = Category.objects.all()
    user_habits = Habit.objects.filter(user=request.user)
    
    # Handle form submission
    if request.method == 'POST':
        completed_habits = request.POST.getlist('completed_habits')
        
        # Clear all existing completions for today
        HabitDay.objects.filter(
            habit__user=request.user,
            day=current_day
        ).delete()
        
        # Mark selected habits as completed
        for habit_id in completed_habits:
            try:
                habit = Habit.objects.get(id=habit_id, user=request.user)
                HabitDay.objects.create(
                    habit=habit,
                    day=current_day,
                    completed=True
                )
            except Habit.DoesNotExist:
                pass
        
        messages.success(request, f'✅ Day {current_day} habits updated successfully!')
        return redirect('habits:scoreboard')
    
    # Get current completion status for today
    completed_today = HabitDay.objects.filter(
        habit__user=request.user,
        day=current_day,
        completed=True
    ).values_list('habit_id', flat=True)
    
    # Organize habits by category for display with new scoring
    habits_by_category = []
    total_categories = 0
    completed_categories = 0
    
    for category in user_categories:
        category_habits = user_habits.filter(category=category)
        if category_habits.exists():
            total_categories += 1
            completed_in_category = category_habits.filter(id__in=completed_today).count()
            
            # Check if category is completed (2 or more activities)
            category_completed = completed_in_category >= 2
            if category_completed:
                completed_categories += 1
            
            habits_by_category.append({
                'category': category,
                'habits': category_habits,
                'completed_count': completed_in_category,
                'total_count': category_habits.count(),
                'category_completed': category_completed,
                'needed_for_completion': max(0, 2 - completed_in_category)
            })
    
    # Handle habits without category
    uncategorized_habits = user_habits.filter(category__isnull=True)
    if uncategorized_habits.exists():
        total_categories += 1
        completed_in_uncategorized = uncategorized_habits.filter(id__in=completed_today).count()
        uncategorized_completed = completed_in_uncategorized >= 2
        if uncategorized_completed:
            completed_categories += 1
            
        habits_by_category.append({
            'category': {'name': 'Uncategorized', 'color': '#6c757d'},
            'habits': uncategorized_habits,
            'completed_count': completed_in_uncategorized,
            'total_count': uncategorized_habits.count(),
            'category_completed': uncategorized_completed,
            'needed_for_completion': max(0, 2 - completed_in_uncategorized)
        })
    
    # Calculate overall completion percentage based on categories
    completion_percentage = (completed_categories / total_categories * 100) if total_categories > 0 else 0
    
    context = {
        'habits_by_category': habits_by_category,
        'current_day': current_day,
        'today': today,
        'challenge_start_date': challenge_start_date,
        'completed_today': completed_today,
        'total_habits': user_habits.count(),
        'completed_count': len(completed_today),
        'completion_percentage': completion_percentage,
        'total_categories': total_categories,
        'completed_categories': completed_categories
    }
    return render(request, 'habits/daily_tracking.html', context)

@login_required
def toggle_habit(request, habit_id):
    """AJAX endpoint to toggle habit completion for current day"""
    if request.method == 'POST':
        today = timezone.now().date()
        challenge_start_date = date(2025, 7, 15)
        
        if today >= challenge_start_date:
            current_day = (today - challenge_start_date).days + 1
            if current_day > 75:
                current_day = 75
        else:
            return JsonResponse({'error': 'Challenge has not started yet'}, status=400)
        
        try:
            habit = Habit.objects.get(id=habit_id, user=request.user)
            habit_day, created = HabitDay.objects.get_or_create(
                habit=habit,
                day=current_day,
                defaults={'completed': False}
            )
            
            # Toggle completion status
            habit_day.completed = not habit_day.completed
            habit_day.save()
            
            return JsonResponse({
                'success': True,
                'completed': habit_day.completed,
                'habit_id': habit_id,
                'day': current_day
            })
        except Habit.DoesNotExist:
            return JsonResponse({'error': 'Habit not found'}, status=404)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def create_category(request):
    """Create a new category"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            # No user assignment
            category.save()
            messages.success(request, f'Category "{category.name}" created successfully!')
            return redirect('habits:home')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Create Category'
    }
    return render(request, 'habits/category_form.html', context)

@login_required
def create_habit(request):
    """Create a new habit"""
    if request.method == 'POST':
        form = HabitForm(request.POST, user=request.user)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, f'Habit "{habit.name}" created successfully!')
            return redirect('habits:home')
    else:
        form = HabitForm(user=request.user)
    
    context = {
        'form': form,
        'title': 'Create Habit'
    }
    return render(request, 'habits/habit_form.html', context)

def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('login')
