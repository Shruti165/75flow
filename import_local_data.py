#!/usr/bin/env python3
"""
Import local data into Render deployment
This script imports users, categories, and habits from local export
"""

import os
import sys
import django
from datetime import datetime

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flow75.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models import Profile, Category, Habit, HabitDay, Streak
from django.core.files.base import ContentFile

# Import data from local export
USERS_DATA = [
  {
    "username": "shruti",
    "email": "shruti@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:17.360721+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "sidd",
    "email": "sidd@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:41.622628+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "sanju",
    "email": "sanju@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:51.800532+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "mahi",
    "email": "mahi@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:52.153512+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "anurag",
    "email": "anurag@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:52.489115+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "pooja",
    "email": "pooja@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:52.824705+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "sachin",
    "email": "sachin@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:53.159832+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  },
  {
    "username": "defni",
    "email": "defni@example.com",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-09-08T17:36:53.492932+00:00",
    "profile": {
      "bio": "",
      "profile_image": None,
      "date_of_birth": None,
      "email": None,
      "weekly_stats_enabled": True
    }
  }
]

CATEGORIES_DATA = [
  {
    "name": "Fitness",
    "color": "#FF6B6B"
  },
  {
    "name": "Nutrition",
    "color": "#4ECDC4"
  },
  {
    "name": "Reading",
    "color": "#45B7D1"
  },
  {
    "name": "Wealth",
    "color": "#96CEB4"
  },
  {
    "name": "Spiritual",
    "color": "#FFEAA7"
  },
  {
    "name": "Fun",
    "color": "#DDA0DD"
  }
]

HABITS_DATA = [
  {
    "name": "7 Minute HIIT",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.553029+00:00"
  },
  {
    "name": "Dance",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.519952+00:00"
  },
  {
    "name": "Evening Walk",
    "description": "Take a 20-minute walk after dinner",
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.676455+00:00"
  },
  {
    "name": "Football",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.542751+00:00"
  },
  {
    "name": "Go To The Park",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.530924+00:00"
  },
  {
    "name": "Gym",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.527808+00:00"
  },
  {
    "name": "Hand Stand / Pull Up / Pole Session",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.549179+00:00"
  },
  {
    "name": "Morning Workout",
    "description": "Start your day with 30 minutes of exercise",
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.673252+00:00"
  },
  {
    "name": "Run",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.513388+00:00"
  },
  {
    "name": "Swim",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.509645+00:00"
  },
  {
    "name": "Walk (7k/10k)",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.537909+00:00"
  },
  {
    "name": "Yoga / Stretch",
    "description": null,
    "category": "Fitness",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.524439+00:00"
  },
  {
    "name": "Consume Leaves",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.565324+00:00"
  },
  {
    "name": "Drink 8 Glasses of Water",
    "description": "Stay hydrated throughout the day",
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.679509+00:00"
  },
  {
    "name": "Drink Coconut Water",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.569331+00:00"
  },
  {
    "name": "Drink Matcha",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.559035+00:00"
  },
  {
    "name": "Drink Vegetable Juice",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.581374+00:00"
  },
  {
    "name": "Drink Water",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.577664+00:00"
  },
  {
    "name": "Eat 5 Servings of Fruits/Veggies",
    "description": "Include colorful fruits and vegetables",
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.682997+00:00"
  },
  {
    "name": "Have Fruits",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.574991+00:00"
  },
  {
    "name": "Prepare Meal / Cook Dinner",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.587029+00:00"
  },
  {
    "name": "Take Chia Seeds",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.591367+00:00"
  },
  {
    "name": "Take Supplements",
    "description": null,
    "category": "Nutrition",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.572426+00:00"
  },
  {
    "name": "Fiction",
    "description": null,
    "category": "Reading",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.499090+00:00"
  },
  {
    "name": "Journal Writing",
    "description": "Write about your day and thoughts",
    "category": "Reading",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.689279+00:00"
  },
  {
    "name": "Non-Fiction",
    "description": null,
    "category": "Reading",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.504232+00:00"
  },
  {
    "name": "Read 30 Minutes",
    "description": "Read books, articles, or educational content",
    "category": "Reading",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.685779+00:00"
  },
  {
    "name": "Spiritual",
    "description": null,
    "category": "Reading",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.506671+00:00"
  },
  {
    "name": "Align High Income Job Offers",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.595103+00:00"
  },
  {
    "name": "Create Content",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.617732+00:00"
  },
  {
    "name": "Deep Work",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.627045+00:00"
  },
  {
    "name": "Get Leads",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.603778+00:00"
  },
  {
    "name": "Go To The Office",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.623888+00:00"
  },
  {
    "name": "Learn About Finance",
    "description": "Read or watch content about money management",
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.698062+00:00"
  },
  {
    "name": "Optimise Linkedin",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.597912+00:00"
  },
  {
    "name": "Passion Projects",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.608845+00:00"
  },
  {
    "name": "Track Expenses",
    "description": "Log all daily expenses",
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.695396+00:00"
  },
  {
    "name": "Upskill",
    "description": null,
    "category": "Wealth",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.612482+00:00"
  },
  {
    "name": "Chanting",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.630526+00:00"
  },
  {
    "name": "Gratitude Practice",
    "description": "Write down 3 things you are grateful for",
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.704707+00:00"
  },
  {
    "name": "Grounding",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.648206+00:00"
  },
  {
    "name": "Journal",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.636894+00:00"
  },
  {
    "name": "Meditate",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.643763+00:00"
  },
  {
    "name": "Meditation",
    "description": "Practice 10 minutes of mindfulness",
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.701022+00:00"
  },
  {
    "name": "Sleep Well / Binaural Beats",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.654143+00:00"
  },
  {
    "name": "Sungazing/Moongazing",
    "description": null,
    "category": "Spiritual",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.659829+00:00"
  },
  {
    "name": "Attend an Event",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.664260+00:00"
  },
  {
    "name": "Community Meet",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.679258+00:00"
  },
  {
    "name": "Creative Activity",
    "description": "Engage in drawing, music, or any creative pursuit",
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.707675+00:00"
  },
  {
    "name": "Dance",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.699124+00:00"
  },
  {
    "name": "DeclutterPlanning for Tomorrow",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.693403+00:00"
  },
  {
    "name": "Gardening",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.676033+00:00"
  },
  {
    "name": "Hackathons",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.669949+00:00"
  },
  {
    "name": "Music",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.683765+00:00"
  },
  {
    "name": "Painitng Sketch",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.690300+00:00"
  },
  {
    "name": "Social Connection",
    "description": "Connect with friends or family",
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T17:42:47.713372+00:00"
  },
  {
    "name": "Social Service",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.705836+00:00"
  },
  {
    "name": "Time with pets",
    "description": null,
    "category": "Fun",
    "created_by": "shruti",
    "start_date": "2025-07-15",
    "updated_at": "2025-09-08T18:00:23.695991+00:00"
  }
]

HABIT_DAYS_DATA = [
  {
    "habit": "7 Minute HIIT",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Align High Income Job Offers",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Attend an Event",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Chanting",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Community Meet",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Consume Leaves",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Create Content",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Dance",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Drink 8 Glasses of Water",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Fiction",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Gratitude Practice",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  },
  {
    "habit": "Journal Writing",
    "user": "sidd",
    "date": "2025-09-09",
    "completed": True,
    "day": 57
  }
]

STREAKS_DATA = [
  {
    "user": "defni",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:55:08.163366+00:00",
    "created_at": "2025-09-08T17:55:08.163414+00:00",
    "updated_at": "2025-09-09T04:39:20.251883+00:00"
  },
  {
    "user": "sachin",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:55:05.754969+00:00",
    "created_at": "2025-09-08T17:55:05.755020+00:00",
    "updated_at": "2025-09-09T04:39:19.957640+00:00"
  },
  {
    "user": "pooja",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:55:03.822290+00:00",
    "created_at": "2025-09-08T17:55:03.822333+00:00",
    "updated_at": "2025-09-09T04:39:19.664745+00:00"
  },
  {
    "user": "anurag",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:55:02.331492+00:00",
    "created_at": "2025-09-08T17:55:02.331560+00:00",
    "updated_at": "2025-09-09T04:39:19.349838+00:00"
  },
  {
    "user": "mahi",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:55:00.802271+00:00",
    "created_at": "2025-09-08T17:55:00.802307+00:00",
    "updated_at": "2025-09-09T04:39:19.061011+00:00"
  },
  {
    "user": "sanju",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:54:59.729067+00:00",
    "created_at": "2025-09-08T17:54:59.729211+00:00",
    "updated_at": "2025-09-09T04:39:17.947223+00:00"
  },
  {
    "user": "sidd",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-09T04:23:17.558180+00:00",
    "created_at": "2025-09-08T17:38:46.630339+00:00",
    "updated_at": "2025-09-09T04:39:17.078232+00:00"
  },
  {
    "user": "shruti",
    "current_streak": 1,
    "best_streak": 1,
    "last_reset_date": "2025-09-08T17:43:58.609445+00:00",
    "created_at": "2025-09-08T17:43:58.609480+00:00",
    "updated_at": "2025-09-09T04:39:15.959259+00:00"
  }
]

def import_categories():
    """Import categories"""
    print("📥 Importing categories...")
    
    for cat_data in CATEGORIES_DATA:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'color': cat_data['color']
            }
        )
        if created:
            print(f"  ✅ Created category: {category.name}")
        else:
            print(f"  ℹ️  Category already exists: {category.name}")

def import_users():
    """Import users and profiles"""
    print("📥 Importing users and profiles...")
    
    for user_data in USERS_DATA:
        # Create or get user
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'is_staff': user_data['is_staff'],
                'is_superuser': user_data['is_superuser'],
                'is_active': user_data['is_active']
            }
        )
        
        if created:
            print(f"  ✅ Created user: {user.username}")
        else:
            print(f"  ℹ️  User already exists: {user.username}")
        
        # Create or update profile
        profile, profile_created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': user_data['profile']['bio'],
                'date_of_birth': datetime.fromisoformat(user_data['profile']['date_of_birth']).date() if user_data['profile']['date_of_birth'] else None,
                'email': user_data['profile']['email'],
                'weekly_stats_enabled': user_data['profile']['weekly_stats_enabled']
            }
        )
        
        if profile_created:
            print(f"    ✅ Created profile for: {user.username}")
        else:
            print(f"    ℹ️  Profile already exists for: {user.username}")

def import_habits():
    """Import habits"""
    print("📥 Importing habits...")
    
    for habit_data in HABITS_DATA:
        try:
            created_by = User.objects.get(username=habit_data['created_by']) if habit_data['created_by'] else None
            category = Category.objects.get(name=habit_data['category']) if habit_data['category'] else None
            
            habit, created = Habit.objects.get_or_create(
                name=habit_data['name'],
                category=category,
                defaults={
                    'description': habit_data['description'],
                    'created_by': created_by,
                    'start_date': datetime.fromisoformat(habit_data['start_date']).date()
                }
            )
            
            if created:
                print(f"  ✅ Created habit: {habit.name}")
            else:
                print(f"  ℹ️  Habit already exists: {habit.name}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_data['created_by']}")
        except Category.DoesNotExist:
            print(f"  ❌ Category not found: {habit_data['category']}")

def import_habit_days():
    """Import habit completion records"""
    print("📥 Importing habit completion records...")
    
    imported_count = 0
    for habit_day_data in HABIT_DAYS_DATA:
        try:
            habit = Habit.objects.get(name=habit_day_data['habit'])
            user = User.objects.get(username=habit_day_data['user'])
            date = datetime.fromisoformat(habit_day_data['date']).date()
            
            habit_day, created = HabitDay.objects.get_or_create(
                habit=habit,
                user=user,
                day=habit_day_data['day'],
                defaults={
                    'completed': habit_day_data['completed'],
                    'date': date
                }
            )
            
            if created:
                imported_count += 1
                
        except Habit.DoesNotExist:
            print(f"  ❌ Habit not found: {habit_day_data['habit']}")
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_day_data['user']}")
    
    print(f"  ✅ Imported {imported_count} habit completion records")

def import_streaks():
    """Import streak records"""
    print("📥 Importing streak records...")
    
    imported_count = 0
    for streak_data in STREAKS_DATA:
        try:
            user = User.objects.get(username=streak_data['user'])
            
            streak, created = Streak.objects.get_or_create(
                user=user,
                defaults={
                    'current_streak': streak_data['current_streak'],
                    'best_streak': streak_data['best_streak'],
                    'last_reset_date': datetime.fromisoformat(streak_data['last_reset_date'])
                }
            )
            
            if created:
                imported_count += 1
                print(f"  ✅ Created streak for: {user.username}")
            else:
                print(f"  ℹ️  Streak already exists for: {user.username}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {streak_data['user']}")
    
    print(f"  ✅ Imported {imported_count} streak records")

def main():
    """Main import function"""
    print("🚀 Starting data import...")
    
    try:
        import_categories()
        print()
        import_users()
        print()
        import_habits()
        print()
        import_habit_days()
        print()
        import_streaks()
        print()
        
        print("🎉 Data import completed successfully!")
        print("\n📊 Summary:")
        print(f"  Users: {len(USERS_DATA)}")
        print(f"  Categories: {len(CATEGORIES_DATA)}")
        print(f"  Habits: {len(HABITS_DATA)}")
        print(f"  Habit Days: {len(HABIT_DAYS_DATA)}")
        print(f"  Streaks: {len(STREAKS_DATA)}")
        
    except Exception as e:
        print(f"❌ Error during import: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
