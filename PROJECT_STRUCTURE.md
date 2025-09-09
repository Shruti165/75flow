# 📁 75Flow Project Structure

A comprehensive Django web application for configurable habit tracking challenges.

## 🏗️ Project Overview

```
75Flow/
├── 📁 flow75/                    # Django project settings
│   ├── __init__.py
│   ├── settings.py              # Main settings with configurable challenge parameters
│   ├── settings_production.py   # Production-specific settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── 📁 habits/                    # Main Django app
│   ├── models.py                # Database models (User, Profile, Habit, HabitDay, Streak, etc.)
│   ├── views.py                 # View functions and logic
│   ├── forms.py                 # Django forms for user input
│   ├── urls.py                  # App-specific URL patterns
│   ├── utils.py                 # Utility functions with configurable challenge settings
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py                  # App configuration
│   ├── tests.py                 # Unit tests
│   │
│   ├── 📁 management/           # Custom Django management commands
│   │   └── commands/
│   │       ├── create_default_users.py
│   │       ├── populate_dummy_data.py
│   │       └── setup_railway.py
│   │
│   ├── 📁 migrations/           # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_habit_description_category.py
│   │   └── ... (other migration files)
│   │
│   └── 📁 templatetags/         # Custom template tags
│       ├── __init__.py
│       └── habit_filters.py
│
├── 📁 templates/                # HTML templates
│   ├── base.html               # Base template with navigation
│   ├── habits/                 # App-specific templates
│   │   ├── home.html          # Dashboard/home page
│   │   ├── habits.html        # Habits tracking page
│   │   ├── profile.html       # User profile page
│   │   ├── scoreboard.html    # Leaderboard
│   │   ├── feedback.html      # Feedback and bug reporting
│   │   └── ... (other templates)
│   └── registration/
│       └── login.html         # Login page
│
├── 📁 static/                   # Static files (CSS, JS, images)
│   ├── css/                    # Stylesheets
│   │   ├── base.css
│   │   ├── home.css
│   │   ├── habits.css
│   │   └── ... (other CSS files)
│   ├── js/                     # JavaScript files
│   │   ├── habits.js
│   │   └── home.js
│   └── images/                 # Static images
│       ├── logo.jpg
│       └── default_avatar.png
│
├── 📁 media/                    # User-uploaded files
│   └── profile_images/         # User profile pictures
│
├── 📁 render_deployment/        # Render deployment configuration
│   ├── build.sh               # Build script for Render
│   ├── Procfile               # Process definition
│   ├── render.yaml            # Render service configuration
│   ├── runtime.txt            # Python version specification
│   ├── packages.txt           # System dependencies
│   ├── requirements.txt       # Python dependencies
│   ├── requirements-dev.txt   # Development dependencies
│   ├── requirements-py313.txt # Python 3.13 optimized dependencies
│   │
│   ├── 📄 import_local_data.py    # Data import script
│   ├── 📄 refresh_data.py         # Data refresh script
│   ├── 📄 reset_passwords.py      # Password reset script
│   ├── 📄 local_data_export.json  # Exported local data
│   │
│   ├── 📄 README.md               # Render deployment documentation
│   ├── 📄 DEPLOYMENT_GUIDE.md     # Step-by-step deployment guide
│   └── 📄 AUTO_DATA_REFRESH.md    # Automatic data refresh documentation
│
├── 📁 logs/                     # Application logs
│   └── django.log
│
├── 📄 manage.py                 # Django management script
├── 📄 requirements.txt          # Python dependencies
├── 📄 db.sqlite3               # SQLite database (development)
├── 📄 local_data_export.json   # Local data export
├── 📄 README.md                # Main project documentation
└── 📄 PROJECT_STRUCTURE.md     # This file
```

## ⚙️ Configuration Features

### **Challenge Settings**
The application supports configurable challenge parameters through environment variables:

- `CHALLENGE_START_DATE`: Challenge start date (default: 2025-07-15)
- `CHALLENGE_DURATION_DAYS`: Challenge duration in days (default: 75)
- `CHALLENGE_NAME`: Display name for the challenge (default: 75Flow Challenge)

### **Environment Configuration**
- **Development**: Uses SQLite database and local settings
- **Production**: Uses PostgreSQL and production-optimized settings
- **Render Deployment**: Automated deployment with data import

## 🗄️ Database Models

### **Core Models**
- **User**: Django's built-in user model
- **Profile**: Extended user information (bio, avatar, settings)
- **Category**: Habit categories (Reading, Fitness, Nutrition, etc.)
- **Habit**: Global habits shared by all users
- **HabitDay**: User-specific habit completion records
- **Streak**: User streak tracking (current and best)
- **Feedback**: User feedback submissions
- **BugReport**: Bug report submissions

### **Key Features**
- **Global Habits**: All users can track the same habits
- **User-Specific Progress**: Each user has their own completion records
- **Streak Calculation**: Automatic streak tracking based on category completion
- **Configurable Duration**: Challenge length can be customized

## 🚀 Deployment

### **Render Deployment**
- **Automated Build**: Uses `build.sh` for dependency installation
- **Data Import**: Automatically imports local data on deployment
- **Environment Variables**: Configurable challenge settings
- **Static Files**: Automatic collection and serving

### **Development**
- **SQLite Database**: Easy local development
- **Django Dev Server**: `python manage.py runserver`
- **Media Files**: Local file storage for development

## 📱 Features

### **User Interface**
- **Responsive Design**: Mobile-friendly Bootstrap interface
- **Modern UI**: Clean, intuitive design with Remix Icons
- **Real-time Updates**: Dynamic progress tracking
- **Profile Management**: Avatar uploads and personalization

### **Habit Tracking**
- **Multi-Category Support**: 6 main categories with 90+ habits
- **Daily Progress**: Check off completed habits daily
- **Streak Tracking**: Monitor current and best streaks
- **Category Analysis**: Detailed performance breakdown

### **Social Features**
- **Leaderboard**: Real-time scoreboard with rankings
- **User Profiles**: View other participants' progress
- **Feedback System**: Submit feedback and bug reports

## 🔧 Technical Stack

- **Backend**: Django 5.2.4 (Python 3.8+)
- **Frontend**: Bootstrap 5, Remix Icons, Custom CSS/JS
- **Database**: SQLite (dev), PostgreSQL (production)
- **Deployment**: Render (PaaS)
- **Media Storage**: Local filesystem (dev), Render persistent disk (production)

## 📚 Documentation

- **README.md**: Main project documentation with setup instructions
- **render_deployment/README.md**: Render-specific deployment guide
- **render_deployment/DEPLOYMENT_GUIDE.md**: Step-by-step deployment process
- **render_deployment/AUTO_DATA_REFRESH.md**: Automatic data refresh documentation
- **PROJECT_STRUCTURE.md**: This file - project structure overview