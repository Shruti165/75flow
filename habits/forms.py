from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Habit, Category, Profile
from django.core.exceptions import ValidationError
import os

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        }

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter habit name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe your habit (optional)'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(HabitForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

class ProfileForm(forms.ModelForm):
    """Form for editing user profile information"""
    
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio', 'date_of_birth', 'email', 'weekly_stats_enabled']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Tell us about yourself...'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'weekly_stats_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*',
            'data-max-size': '5MB'
        })
        self.fields['profile_image'].help_text = "Upload a profile picture (JPG, PNG, GIF up to 5MB)"
    
    def clean_profile_image(self):
        """Validate profile image upload"""
        image = self.cleaned_data.get('profile_image')
        
        if image:
            # Check file size (5MB limit)
            if image.size > 5 * 1024 * 1024:  # 5MB in bytes
                raise ValidationError("Image file size must be under 5MB.")
            
            # Check file extension
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            file_extension = os.path.splitext(image.name)[1].lower()
            
            if file_extension not in allowed_extensions:
                raise ValidationError("Please upload a valid image file (JPG, PNG, or GIF).")
            
            # Check if it's actually an image
            try:
                from PIL import Image
                img = Image.open(image)
                img.verify()  # Verify it's a valid image
            except Exception:
                raise ValidationError("Please upload a valid image file.")
        
        return image 