from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from habits.models import Category, Habit, Profile
from datetime import date

class Command(BaseCommand):
    help = 'Set up Railway database with initial data'

    def handle(self, *args, **options):
        self.stdout.write("🚀 Setting up Railway database...")
        
        # Create users if they don't exist
        users_data = [
            {'username': 'Shruti', 'password': 'shruti'},
            {'username': 'Sid', 'password': 'sid'},
            {'username': 'Sanju', 'password': 'sanju'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'password': make_password(user_data['password']),
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f"✅ Created user: {user.username}")
            else:
                self.stdout.write(f"ℹ️  User already exists: {user.username}")
            
            # Ensure user has a profile
            profile, profile_created = Profile.objects.get_or_create(user=user)
            if profile_created:
                self.stdout.write(f"✅ Created profile for: {user.username}")
        
        # Create categories if they don't exist
        categories_data = [
            {'name': 'Health', 'color': '#28a745'},
            {'name': 'Wealth', 'color': '#007bff'},
            {'name': 'Relationships', 'color': '#dc3545'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'color': cat_data['color']}
            )
            if created:
                self.stdout.write(f"✅ Created category: {category.name}")
            else:
                self.stdout.write(f"ℹ️  Category already exists: {category.name}")
        
        # Create some sample habits for each user
        habits_data = [
            {'name': 'Morning Exercise', 'description': '30 minutes of cardio', 'category_name': 'Health'},
            {'name': 'Read 30 minutes', 'description': 'Read a book or article', 'category_name': 'Wealth'},
            {'name': 'Call family', 'description': 'Call a family member', 'category_name': 'Relationships'},
            {'name': 'Drink 8 glasses water', 'description': 'Stay hydrated', 'category_name': 'Health'},
            {'name': 'Save money', 'description': 'Save $10 today', 'category_name': 'Wealth'},
        ]
        
        for user in User.objects.all():
            for habit_info in habits_data:
                category = Category.objects.get(name=habit_info['category_name'])
                habit, created = Habit.objects.get_or_create(
                    user=user,
                    name=habit_info['name'],
                    defaults={
                        'description': habit_info['description'],
                        'category': category,
                        'start_date': date(2025, 7, 15)
                    }
                )
                if created:
                    self.stdout.write(f"✅ Created habit '{habit.name}' for {user.username}")
        
        self.stdout.write("🎉 Railway database setup completed!")
        self.stdout.write("📊 Summary:")
        self.stdout.write(f"  - Users: {User.objects.count()}")
        self.stdout.write(f"  - Categories: {Category.objects.count()}")
        self.stdout.write(f"  - Habits: {Habit.objects.count()}")
        self.stdout.write(f"  - Profiles: {Profile.objects.count()}")
        
        self.stdout.write("\n🔑 Login Credentials:")
        for user_data in users_data:
            self.stdout.write(f"  - Username: {user_data['username']}, Password: {user_data['password']}") 