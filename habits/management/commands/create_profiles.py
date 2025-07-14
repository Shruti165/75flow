from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from habits.models import Profile

class Command(BaseCommand):
    help = 'Create Profile objects for all existing users who do not have profiles'

    def handle(self, *args, **options):
        users_without_profiles = []
        
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                users_without_profiles.append(user)
        
        if users_without_profiles:
            self.stdout.write(f"Creating profiles for {len(users_without_profiles)} users...")
            
            for user in users_without_profiles:
                Profile.objects.create(user=user)
                self.stdout.write(f"Created profile for user: {user.username}")
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {len(users_without_profiles)} profiles!')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('All users already have profiles!')
            ) 