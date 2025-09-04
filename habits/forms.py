from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Habit, Category, Profile, Feedback, BugReport
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

class FeedbackForm(forms.ModelForm):
    """Form for submitting feedback and suggestions"""
    
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'title', 'description', 'priority']
        widgets = {
            'feedback_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Brief title for your feedback'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Please provide detailed feedback...'
            }),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['title'].required = True

class BugReportForm(forms.ModelForm):
    """Form for reporting bugs"""
    
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'steps_to_reproduce', 'expected_behavior', 
                 'actual_behavior', 'severity', 'browser_info', 'device_info', 'screenshot']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Brief description of the bug'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'What happened?'
            }),
            'steps_to_reproduce': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': '1. Go to...\n2. Click on...\n3. See error...'
            }),
            'expected_behavior': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'What should have happened?'
            }),
            'actual_behavior': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'What actually happened?'
            }),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'browser_info': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Chrome 120, Firefox 119'
            }),
            'device_info': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Windows 11, iPhone 15, MacBook Pro'
            }),
            'screenshot': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['screenshot'].required = False
        self.fields['browser_info'].required = False
        self.fields['device_info'].required = False
    
    def clean_screenshot(self):
        """Validate screenshot upload"""
        screenshot = self.cleaned_data.get('screenshot')
        
        if screenshot:
            # Check file size (10MB limit for bug reports)
            if screenshot.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise ValidationError("Screenshot file size must be under 10MB.")
            
            # Check file extension
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            file_extension = os.path.splitext(screenshot.name)[1].lower()
            
            if file_extension not in allowed_extensions:
                raise ValidationError("Please upload a valid image file (JPG, PNG, GIF, or WebP).")
        
        return screenshot