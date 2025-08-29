from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Reset all participant passwords to their usernames (excluding admin)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirm that you want to reset all passwords',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(
                    '⚠️  This will reset ALL participant passwords to their usernames!\n'
                    '⚠️  This action cannot be undone!\n\n'
                    'To proceed, run: python manage.py reset_participant_passwords --confirm'
                )
            )
            return

        # Get all users except admin
        participants = User.objects.exclude(username='admin')
        
        if not participants.exists():
            self.stdout.write(
                self.style.WARNING('No participants found in the system.')
            )
            return

        self.stdout.write(
            self.style.SUCCESS(f'Found {participants.count()} participants to reset passwords for.')
        )

        # Show current participants
        self.stdout.write('\n📋 Current participants:')
        for participant in participants:
            self.stdout.write(f'  • {participant.username} ({participant.get_full_name() or "No name"})')

        # Confirm again
        self.stdout.write('\n⚠️  Are you sure you want to reset all passwords? (yes/no): ', ending='')
        confirm = input().lower().strip()

        if confirm not in ['yes', 'y']:
            self.stdout.write(
                self.style.WARNING('Password reset cancelled.')
            )
            return

        # Reset passwords
        updated_count = 0
        for participant in participants:
            old_password = participant.password
            new_password = participant.username
            
            # Set new password
            participant.password = make_password(new_password)
            participant.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ {participant.username}: Password reset to "{new_password}"')
            )
            updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'\n🎉 Successfully reset passwords for {updated_count} participants!')
        )
        
        self.stdout.write(
            self.style.WARNING(
                '\n📝 New login credentials:\n'
                'Participants can now log in using:\n'
                '• Username: their username\n'
                '• Password: their username\n\n'
                '⚠️  Please inform participants to change their passwords after first login!'
            )
        )
