from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Create a default admin user for Render deployment'

    def handle(self, *args, **options):
        try:
            # Check if admin user already exists
            if User.objects.filter(username='admin').exists():
                self.stdout.write(
                    self.style.WARNING('Admin user already exists')
                )
                return

            # Create admin user
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@75flow.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created admin user: {admin_user.username}'
                )
            )
            self.stdout.write(
                self.style.SUCCESS('Password: admin123')
            )
            self.stdout.write(
                self.style.WARNING(
                    'Please change the password after first login!'
                )
            )

        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating admin user: {e}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Unexpected error: {e}')
            )
