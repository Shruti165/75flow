from django.core.management.base import BaseCommand
from habits.models import Achievement

class Command(BaseCommand):
    help = 'Populate default achievements for the 75Flow application'

    def handle(self, *args, **options):
        achievements_data = [
            # Streak Achievements
            {
                'name': 'Getting Started',
                'description': 'Complete your first 3-day streak',
                'achievement_type': 'streak',
                'icon': 'ri-fire-line',
                'color': '#ff6b6b',
                'requirement_value': 3,
                'requirement_type': 'streak'
            },
            {
                'name': 'Week Warrior',
                'description': 'Maintain a 7-day streak',
                'achievement_type': 'streak',
                'icon': 'ri-fire-line',
                'color': '#ff8e53',
                'requirement_value': 7,
                'requirement_type': 'streak'
            },
            {
                'name': 'Habit Hero',
                'description': 'Maintain a 21-day streak',
                'achievement_type': 'streak',
                'icon': 'ri-fire-line',
                'color': '#ffb74d',
                'requirement_value': 21,
                'requirement_type': 'streak'
            },
            {
                'name': 'Monthly Master',
                'description': 'Complete a 30-day streak',
                'achievement_type': 'streak',
                'icon': 'ri-fire-line',
                'color': '#ffcc02',
                'requirement_value': 30,
                'requirement_type': 'streak'
            },
            
            # Completion Achievements
            {
                'name': 'First Steps',
                'description': 'Complete your first 10 days',
                'achievement_type': 'completion',
                'icon': 'ri-check-double-line',
                'color': '#4caf50',
                'requirement_value': 10,
                'requirement_type': 'days'
            },
            {
                'name': 'Halfway Hero',
                'description': 'Complete 37 days (halfway point)',
                'achievement_type': 'completion',
                'icon': 'ri-check-double-line',
                'color': '#81c784',
                'requirement_value': 37,
                'requirement_type': 'days'
            },
            
            # Milestone Achievements
            {
                'name': 'Category Explorer',
                'description': 'Complete habits in 2 different categories',
                'achievement_type': 'milestone',
                'icon': 'ri-flag-line',
                'color': '#9c27b0',
                'requirement_value': 2,
                'requirement_type': 'categories_completed'
            },
            {
                'name': 'Consistency King',
                'description': 'Achieve 80% overall completion rate',
                'achievement_type': 'milestone',
                'icon': 'ri-flag-line',
                'color': '#ce93d8',
                'requirement_value': 80,
                'requirement_type': 'completion_percentage'
            },
        ]

        created_count = 0
        updated_count = 0

        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                name=achievement_data['name'],
                defaults=achievement_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created achievement: {achievement.name}')
                )
            else:
                # Update existing achievement with new data
                for key, value in achievement_data.items():
                    setattr(achievement, key, value)
                achievement.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated achievement: {achievement.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated achievements! '
                f'Created: {created_count}, Updated: {updated_count}'
            )
        ) 