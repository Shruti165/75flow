from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True, help_text="Email for weekly stats notifications")
    weekly_stats_enabled = models.BooleanField(default=True, help_text="Receive weekly stats emails")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def profile_image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        return None
    
    @property
    def notification_email(self):
        """Return the email to use for notifications (profile email or user email)"""
        return self.email or self.user.email

# Signal to automatically create a profile when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#2196f3')  # Hex color code
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='habits', null=True, blank=True)
    start_date = models.DateField(default=date(2025, 7, 15))  # July 15th, 2025
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class HabitDay(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    day = models.IntegerField()  # Day number in the 75-day challenge
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('habit', 'day')
    
    def __str__(self):
        return f"{self.habit.name} - Day {self.day} ({'Completed' if self.completed else 'Not Completed'})"
