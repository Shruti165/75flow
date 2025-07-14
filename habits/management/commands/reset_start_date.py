from django.core.management.base import BaseCommand
from django.utils import timezone
from habits.models import Habit
from datetime import date

class Command(BaseCommand):
    help = 'Reset start date for all habits to July 15th, 2025'

    def handle(self, *args, **options):
        target_date = date(2025, 7, 15)
        habits = Habit.objects.all()
        
        updated_count = 0
        for habit in habits:
            if habit.start_date != target_date:
                habit.start_date = target_date
                habit.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated habit "{habit.name}" start date to {target_date}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {updated_count} habits to start date {target_date}')
        ) 