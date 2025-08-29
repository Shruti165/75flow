from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Create default users for Render deployment'

    def handle(self, *args, **options):
        try:
            # Create admin user
            if not User.objects.filter(username='admin').exists():
                admin_user = User.objects.create_user(
                    username='admin',
                    email='admin@75flow.com',
                    password='admin123',
                    is_staff=True,
                    is_superuser=True
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created admin user: {admin_user.username} (password: admin123)'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Admin user already exists')
                )

            # Create Shruti user
            if not User.objects.filter(username='Shruti').exists():
                shruti_user = User.objects.create_user(
                    username='Shruti',
                    email='shruti@75flow.com',
                    password='Shruti',
                    is_staff=False,
                    is_superuser=False
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created Shruti user: {shruti_user.username} (password: Shruti)'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Shruti user already exists')
                )

            # Create a few more test users
            test_users = [
                {'username': 'John', 'email': 'john@75flow.com', 'password': 'John'},
                {'username': 'Sarah', 'email': 'sarah@75flow.com', 'password': 'Sarah'},
                {'username': 'Mike', 'email': 'mike@75flow.com', 'password': 'Mike'},
            ]

            for user_data in test_users:
                if not User.objects.filter(username=user_data['username']).exists():
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password'],
                        is_staff=False,
                        is_superuser=False
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Created user: {user.username} (password: {user_data["password"]})'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'User {user_data["username"]} already exists')
                    )

            self.stdout.write(
                self.style.SUCCESS('Default users created successfully!')
            )
            self.stdout.write(
                self.style.WARNING('Please change passwords after first login!')
            )

        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating users: {e}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Unexpected error: {e}')
            )
