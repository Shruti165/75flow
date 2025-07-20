from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Migrate from SQLite to PostgreSQL for Railway deployment'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting migration to PostgreSQL...'))
        
        # Check if we're using PostgreSQL
        if not settings.DATABASES['default']['ENGINE'].startswith('django.db.backends.postgresql'):
            self.stdout.write(self.style.ERROR('Not using PostgreSQL. Skipping migration.'))
            return
        
        try:
            # Run migrations
            self.stdout.write('Running migrations...')
            call_command('migrate', verbosity=1)
            
            # Create superuser if it doesn't exist
            self.stdout.write('Checking for superuser...')
            from django.contrib.auth.models import User
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write('Creating superuser...')
                call_command('createsuperuser', interactive=False)
            
            # Load dummy data if needed
            self.stdout.write('Loading dummy data...')
            call_command('populate_dummy_data', verbosity=1)
            
            self.stdout.write(self.style.SUCCESS('Successfully migrated to PostgreSQL!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during migration: {e}'))
            raise 