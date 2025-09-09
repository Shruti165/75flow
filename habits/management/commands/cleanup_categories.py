from django.core.management.base import BaseCommand
from habits.models import Category, Habit
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Clean up duplicate categories and create shared categories'

    def handle(self, *args, **options):
        # Define the 6 standard categories
        standard_categories = [
            {'name': 'Reading', 'color': '#4CAF50'},
            {'name': 'Fitness', 'color': '#FF5722'},
            {'name': 'Nutrition', 'color': '#FF9800'},
            {'name': 'Wealth', 'color': '#2196F3'},
            {'name': 'Spiritual', 'color': '#9C27B0'},
            {'name': 'Fun', 'color': '#E91E63'},
        ]
        
        # Get all users
        users = User.objects.all()
        
        # Create shared categories (one set for all users)
        shared_categories = []
        for cat_data in standard_categories:
            # Create category for the first user (this will be our shared category)
            first_user = users.first()
            if first_user:
                category, created = Category.objects.get_or_create(
                    user=first_user,
                    name=cat_data['name'],
                    defaults={'color': cat_data['color']}
                )
                shared_categories.append(category)
                if created:
                    self.stdout.write(f"Created shared category: {category.name}")
                else:
                    self.stdout.write(f"Found existing shared category: {category.name}")
        
        # Update all habits to use the shared categories
        for habit in Habit.objects.all():
            if habit.category:
                # Find the corresponding shared category
                shared_category = None
                for shared_cat in shared_categories:
                    if shared_cat.name == habit.category.name:
                        shared_category = shared_cat
                        break
                
                if shared_category and habit.category != shared_category:
                    old_category = habit.category
                    habit.category = shared_category
                    habit.save()
                    self.stdout.write(f"Updated habit '{habit.name}' from category '{old_category.name}' to shared category '{shared_category.name}'")
        
        # Delete duplicate categories (keep only the shared ones)
        categories_to_delete = Category.objects.exclude(id__in=[cat.id for cat in shared_categories])
        deleted_count = categories_to_delete.count()
        categories_to_delete.delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully cleaned up categories. Deleted {deleted_count} duplicate categories. '
                f'Now have {len(shared_categories)} shared categories.'
            )
        ) 