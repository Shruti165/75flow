from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Check if users exist in the database'

    def handle(self, *args, **options):
        self.stdout.write("🔍 Checking users in database...")
        
        users = User.objects.all()
        self.stdout.write(f"Total users found: {users.count()}")
        
        if users.count() > 0:
            self.stdout.write("Users:")
            for user in users:
                self.stdout.write(f"  - {user.username} (active: {user.is_active})")
        else:
            self.stdout.write("❌ No users found in database!")
            self.stdout.write("💡 Run: python manage.py setup_railway")
        
        # Check if Shruti exists specifically
        try:
            shruti = User.objects.get(username='Shruti')
            self.stdout.write(f"✅ Shruti found! Active: {shruti.is_active}")
        except User.DoesNotExist:
            self.stdout.write("❌ Shruti user not found!")
            self.stdout.write("💡 Run: python manage.py setup_railway") 