from django.contrib import admin
from .models import Habit, HabitDay, Category

admin.site.register(Category)
admin.site.register(Habit)
admin.site.register(HabitDay)
