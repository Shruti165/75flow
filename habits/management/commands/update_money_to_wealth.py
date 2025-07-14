from django.core.management.base import BaseCommand
from habits.models import Category

class Command(BaseCommand):
    help = 'Update existing "Money" categories to "Wealth"'

    def handle(self, *args, **options):
        # Find all categories named "Money"
        money_categories = Category.objects.filter(name="Money")
        
        if money_categories.exists():
            # Update them to "Wealth"
            updated_count = money_categories.update(name="Wealth")
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully updated {updated_count} "Money" categories to "Wealth"'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    'No "Money" categories found in the database'
                )
            ) 