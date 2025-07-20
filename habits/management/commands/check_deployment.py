from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from habits.models import Category, Habit, Profile

class Command(BaseCommand):
    help = 'Check deployment status and database setup'

    def handle(self, *args, **options):
        self.stdout.write("🔍 Checking deployment status...")
        
        # Check environment
        self.stdout.write(f"Environment: {getattr(settings, 'ENVIRONMENT', 'Not set')}")
        self.stdout.write(f"DEBUG: {settings.DEBUG}")
        self.stdout.write(f"Database: {settings.DATABASES['default']['ENGINE']}")
        
        # Check database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                db_version = cursor.fetchone()
                self.stdout.write(f"Database connected: {db_version[0]}")
        except Exception as e:
            self.stdout.write(f"❌ Database connection failed: {e}")
            return
        
        # Check users
        user_count = User.objects.count()
        self.stdout.write(f"Users in database: {user_count}")
        
        if user_count > 0:
            users = User.objects.all()[:5]  # Show first 5 users
            for user in users:
                self.stdout.write(f"  - {user.username} (active: {user.is_active})")
        
        # Check categories
        category_count = Category.objects.count()
        self.stdout.write(f"Categories: {category_count}")
        
        # Check habits
        habit_count = Habit.objects.count()
        self.stdout.write(f"Habits: {habit_count}")
        
        # Check profiles
        profile_count = Profile.objects.count()
        self.stdout.write(f"Profiles: {profile_count}")
        
        # Check static files
        self.stdout.write(f"Static URL: {settings.STATIC_URL}")
        self.stdout.write(f"Static Root: {settings.STATIC_ROOT}")
        self.stdout.write(f"Media URL: {settings.MEDIA_URL}")
        self.stdout.write(f"Media Root: {settings.MEDIA_ROOT}")
        
        # Check allowed hosts
        self.stdout.write(f"Allowed Hosts: {settings.ALLOWED_HOSTS}")
        
        self.stdout.write("✅ Deployment check completed!") 