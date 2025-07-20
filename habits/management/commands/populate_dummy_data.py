from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
import random
from habits.models import Category, Habit, HabitDay, Profile

class Command(BaseCommand):
    help = 'Populate database with dummy data for 75-day challenge starting July 15th, 2025'

    def handle(self, *args, **options):
        self.stdout.write('Creating dummy data for 75-day challenge...')
        
        # Create categories if they don't exist
        categories_data = [
            {'name': 'Reading', 'color': '#667eea', 'description': 'Reading books and articles'},
            {'name': 'Fitness', 'color': '#86efac', 'description': 'Exercise and physical activity'},
            {'name': 'Nutrition', 'color': '#fca5a5', 'description': 'Healthy eating habits'},
            {'name': 'Wealth', 'color': '#7dd3fc', 'description': 'Financial planning and investment'},
            {'name': 'Spiritual', 'color': '#c084fc', 'description': 'Meditation and mindfulness'},
            {'name': 'Fun', 'color': '#fbbf24', 'description': 'Hobbies and entertainment'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'color': cat_data['color'],
                    'description': cat_data['description']
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create users if they don't exist
        users_data = [
            {'username': 'Sid', 'email': 'sid@example.com', 'first_name': 'Sid', 'last_name': 'Kumar'},
            {'username': 'Shruti', 'email': 'shruti@example.com', 'first_name': 'Shruti', 'last_name': 'Gupta'},
            {'username': 'Sanju', 'email': 'sanju@example.com', 'first_name': 'Sanju', 'last_name': 'Patel'},
        ]
        
        users = {}
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'is_active': True
                }
            )
            if created:
                user.set_password(user_data['username'])  # Password same as username
                user.save()
                # Create profile if it doesn't exist
                Profile.objects.get_or_create(user=user)
                self.stdout.write(f'Created user: {user.username}')
            else:
                # Ensure profile exists for existing users
                Profile.objects.get_or_create(user=user)
            users[user_data['username']] = user
        
        # Create habits for each user
        habits_data = [
            {'name': 'Read 30 minutes', 'category': 'Reading', 'description': 'Read books or articles'},
            {'name': 'Morning workout', 'category': 'Fitness', 'description': '30 minutes exercise'},
            {'name': 'Drink 8 glasses water', 'category': 'Nutrition', 'description': 'Stay hydrated'},
            {'name': 'Track expenses', 'category': 'Wealth', 'description': 'Log daily spending'},
            {'name': 'Meditation', 'category': 'Spiritual', 'description': '10 minutes mindfulness'},
            {'name': 'Play guitar', 'category': 'Fun', 'description': 'Practice music'},
            {'name': 'Read tech blogs', 'category': 'Reading', 'description': 'Read technology articles'},
            {'name': 'Gym workout', 'category': 'Fitness', 'description': 'Weight training session'},
            {'name': 'Eat healthy meals', 'category': 'Nutrition', 'description': 'Balanced nutrition'},
            {'name': 'Save money', 'category': 'Wealth', 'description': 'Daily savings habit'},
            {'name': 'Prayer time', 'category': 'Spiritual', 'description': 'Daily prayers'},
            {'name': 'Photography', 'category': 'Fun', 'description': 'Take photos and edit'},
            {'name': 'Read business books', 'category': 'Reading', 'description': 'Business and leadership books'},
            {'name': 'Running', 'category': 'Fitness', 'description': 'Daily run or jog'},
            {'name': 'Protein intake', 'category': 'Nutrition', 'description': 'Track protein consumption'},
            {'name': 'Investment research', 'category': 'Wealth', 'description': 'Study market trends'},
            {'name': 'Journaling', 'category': 'Spiritual', 'description': 'Write daily thoughts'},
            {'name': 'Coding practice', 'category': 'Fun', 'description': 'Work on side projects'},
        ]
        
        # Create all habits and assign them to all users
        all_habits = []
        for habit_data in habits_data:
            # Create the habit for each user
            for username, user in users.items():
                habit, created = Habit.objects.get_or_create(
                    user=user,
                    name=habit_data['name'],
                    defaults={
                        'description': habit_data['description'],
                        'category': categories[habit_data['category']],
                        'start_date': date(2025, 7, 15)
                    }
                )
                if created:
                    self.stdout.write(f'Created habit for {username}: {habit.name}')
                all_habits.append(habit)
        
        # Group habits by user for completion data
        user_habits = {}
        for username, user in users.items():
            user_habits[username] = Habit.objects.filter(user=user)
        
        # Create habit completion data for the past days (July 15th to today)
        challenge_start = date(2025, 7, 15)
        today = timezone.now().date()
        
        # Calculate days since challenge start
        if today >= challenge_start:
            days_since_start = (today - challenge_start).days
        else:
            days_since_start = 0
        
        # Create realistic completion patterns for each user
        completion_patterns = {
            'Sid': {
                'consistency': 0.80,  # 80% consistency
                'categories_focus': ['Fitness', 'Wealth', 'Fun'],
                'streak_breaks': [12, 25, 40, 55]  # Days where they might miss
            },
            'Shruti': {
                'consistency': 0.85,  # 85% consistency
                'categories_focus': ['Reading', 'Fitness', 'Nutrition'],
                'streak_breaks': [15, 30, 45]  # Days where they might miss
            },
            'Sanju': {
                'consistency': 0.90,  # 90% consistency (high performer)
                'categories_focus': ['Spiritual', 'Nutrition', 'Reading'],
                'streak_breaks': [20, 35]  # Fewer streak breaks
            },
        }
        
        self.stdout.write('Creating habit completion data...')
        
        for username, pattern in completion_patterns.items():
            user = users[username]
            habits = Habit.objects.filter(user=user)
            
            for day_num in range(1, min(days_since_start + 1, 76)):
                # Determine if user completes habits on this day
                base_completion_chance = pattern['consistency']
                
                # Reduce chance on streak break days
                if day_num in pattern['streak_breaks']:
                    base_completion_chance *= 0.3
                
                # Random variation
                completion_chance = base_completion_chance + random.uniform(-0.1, 0.1)
                completion_chance = max(0.1, min(0.95, completion_chance))
                
                # Decide if user completes habits today
                if random.random() < completion_chance:
                    # User completes some habits today
                    completed_habits = random.sample(list(habits), random.randint(2, min(4, len(habits))))
                    
                    for habit in completed_habits:
                        HabitDay.objects.get_or_create(
                            habit=habit,
                            day=day_num,
                            defaults={'completed': True}
                        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created dummy data!\n'
                f'Challenge started: {challenge_start}\n'
                f'Days since start: {days_since_start}\n'
                f'Users created: {len(users)}\n'
                f'Categories created: {len(categories)}\n'
                f'Habits created: {Habit.objects.count()}\n'
                f'Completion records: {HabitDay.objects.count()}'
            )
        ) 