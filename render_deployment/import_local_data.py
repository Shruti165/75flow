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
from habits.models import Profile, Category, Habit, HabitDay
from django.core.files.base import ContentFile

# Import data from local export
USERS_DATA = [
  {
    "username": "Sid",
    "email": "",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-07-13T20:08:29.586041+00:00",
    "profile": {
      "bio": "",
      "profile_image": "profile_images/Sid_1_MD4DgkD.png",
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "Shruti",
    "email": "",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-07-13T20:08:30.048332+00:00",
    "profile": {
      "bio": "hello",
      "profile_image": "profile_images/Shruti_5lA8J6j.png",
      "date_of_birth": null,
      "email": "strength.shruti@gmail.com",
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "Sanju",
    "email": "",
    "first_name": "",
    "last_name": "",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-07-13T20:08:30.563520+00:00",
    "profile": {
      "bio": "",
      "profile_image": "profile_images/Sanjh.png",
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "admin",
    "email": "",
    "first_name": "",
    "last_name": "",
    "is_staff": True,
    "is_superuser": True,
    "is_active": True,
    "date_joined": "2025-08-01T10:05:04.306733+00:00",
    "profile": {
      "bio": "",
      "profile_image": null,
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "Sachin",
    "email": "sachin@gmail.com",
    "first_name": "Sachin",
    "last_name": "Test",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-08-29T07:14:49.929459+00:00",
    "profile": {
      "bio": "",
      "profile_image": null,
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "Defni",
    "email": "defni@gmail.com",
    "first_name": "Defni",
    "last_name": "Defni",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-08-29T07:16:41.919444+00:00",
    "profile": {
      "bio": "",
      "profile_image": null,
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  },
  {
    "username": "Pooja",
    "email": "pooja@gmail.com",
    "first_name": "Pooja",
    "last_name": "Pooja",
    "is_staff": False,
    "is_superuser": False,
    "is_active": True,
    "date_joined": "2025-08-29T08:08:52.775112+00:00",
    "profile": {
      "bio": "",
      "profile_image": null,
      "date_of_birth": null,
      "email": null,
      "weekly_stats_enabled": true
    }
  }
]

CATEGORIES_DATA = [
  {
    "name": "Reading",
    "color": "#2196f3"
  },
  {
    "name": "Fitness",
    "color": "#4caf50"
  },
  {
    "name": "Nutrition",
    "color": "#ff9800"
  },
  {
    "name": "Wealth",
    "color": "#9c27b0"
  },
  {
    "name": "Spiritual",
    "color": "#e91e63"
  },
  {
    "name": "Fun",
    "color": "#00bcd4"
  }
]

HABITS_DATA = [
  {
    "name": "Fiction",
    "description": "Daily fiction habit",
    "category": "Reading",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Non-Fiction",
    "description": "Daily non-fiction habit",
    "category": "Reading",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Spiritual",
    "description": "Daily spiritual habit",
    "category": "Reading",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Swim",
    "description": "Daily swim habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Run",
    "description": "Daily run habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Dance",
    "description": "Daily dance habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Yoga / Stretch",
    "description": "Daily yoga / stretch habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym",
    "description": "Daily gym habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Park",
    "description": "Daily go to the park habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Walk",
    "description": "Daily walk habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Football",
    "description": "Daily football habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Hand Stand / Pull Up / Pole Session",
    "description": "Daily hand stand / pull up / pole session habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "7 Minute HIIT",
    "description": "Daily 7 minute hiit habit",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Matcha",
    "description": "Daily drink matcha habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Consume Leaves",
    "description": "Daily consume leaves habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Coconut Water",
    "description": "Daily drink coconut water habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Supplements",
    "description": "Daily take supplements habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Have Fruits",
    "description": "Daily have fruits habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Water",
    "description": "Daily drink water habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Vegetable Juice",
    "description": "Daily drink vegetable juice habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prepare Meal / Cook Dinner",
    "description": "Daily prepare meal / cook dinner habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Chia Seeds",
    "description": "Daily take chia seeds habit",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Mantra Chanting",
    "description": "Daily mantra chanting habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Get Aligned High Income Job Offers",
    "description": "Daily get aligned high income job offers habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Optimise Linkedin",
    "description": "Daily optimise linkedin habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "AI Projects",
    "description": "Daily ai projects habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Passion Projects",
    "description": "Daily passion projects habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Upskill",
    "description": "Daily upskill habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Create Content",
    "description": "Daily create content habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Office",
    "description": "Daily go to the office habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Chanting",
    "description": "Daily chanting habit",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journal",
    "description": "Daily journal habit",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Grounding",
    "description": "Daily grounding habit",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Sleep Well / Binaural Beats",
    "description": "Daily sleep well / binaural beats habit",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Attend an Event",
    "description": "Daily attend an event habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Social Club Meet",
    "description": "Daily social club meet habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Community Service",
    "description": "Daily community service habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Visit Orphanage/ Old Age Home",
    "description": "Daily visit orphanage/ old age home habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Music Jam",
    "description": "Daily music jam habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Painitng, Gardening, Sketch",
    "description": "Daily painitng, gardening, sketch habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Declutter / Organise",
    "description": "Daily declutter / organise habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Planning for Tomorrow",
    "description": "Daily planning for tomorrow habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Feed The Dogs",
    "description": "Daily feed the dogs habit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Fiction",
    "description": "Daily fiction habit",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Non-Fiction",
    "description": "Daily non-fiction habit",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Spiritual",
    "description": "Daily spiritual habit",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Swim",
    "description": "Daily swim habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Run",
    "description": "Daily run habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Dance",
    "description": "Daily dance habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Yoga / Stretch",
    "description": "Daily yoga / stretch habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym",
    "description": "Daily gym habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Park",
    "description": "Daily go to the park habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Walk",
    "description": "Daily walk habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Football",
    "description": "Daily football habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Hand Stand / Pull Up / Pole Session",
    "description": "Daily hand stand / pull up / pole session habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "7 Minute HIIT",
    "description": "Daily 7 minute hiit habit",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Matcha",
    "description": "Daily drink matcha habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Consume Leaves",
    "description": "Daily consume leaves habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Coconut Water",
    "description": "Daily drink coconut water habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Supplements",
    "description": "Daily take supplements habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Have Fruits",
    "description": "Daily have fruits habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Water",
    "description": "Daily drink water habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Vegetable Juice",
    "description": "Daily drink vegetable juice habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prepare Meal / Cook Dinner",
    "description": "Daily prepare meal / cook dinner habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Chia Seeds",
    "description": "Daily take chia seeds habit",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Mantra Chanting",
    "description": "Daily mantra chanting habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Get Aligned High Income Job Offers",
    "description": "Daily get aligned high income job offers habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Optimise Linkedin",
    "description": "Daily optimise linkedin habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "AI Projects",
    "description": "Daily ai projects habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Passion Projects",
    "description": "Daily passion projects habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Upskill",
    "description": "Daily upskill habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Create Content",
    "description": "Daily create content habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Office",
    "description": "Daily go to the office habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Chanting",
    "description": "Daily chanting habit",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journal",
    "description": "Daily journal habit",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Meditate",
    "description": "Daily meditate habit",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Grounding",
    "description": "Daily grounding habit",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Sleep Well / Binaural Beats",
    "description": "Daily sleep well / binaural beats habit",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Attend an Event",
    "description": "Daily attend an event habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Hackathons",
    "description": "Daily hackathons habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Social Club Meet",
    "description": "Daily social club meet habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Community Service",
    "description": "Daily community service habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Visit Orphanage/ Old Age Home",
    "description": "Daily visit orphanage/ old age home habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Music Jam",
    "description": "Daily music jam habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Painitng, Gardening, Sketch",
    "description": "Daily painitng, gardening, sketch habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Declutter / Organise",
    "description": "Daily declutter / organise habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Planning for Tomorrow",
    "description": "Daily planning for tomorrow habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Feed The Dogs",
    "description": "Daily feed the dogs habit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Fiction",
    "description": "Daily fiction habit",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Non-Fiction",
    "description": "Daily non-fiction habit",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Spiritual",
    "description": "Daily spiritual habit",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Swim",
    "description": "Daily swim habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Run",
    "description": "Daily run habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Dance",
    "description": "Daily dance habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Yoga / Stretch",
    "description": "Daily yoga / stretch habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym",
    "description": "Daily gym habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Park",
    "description": "Daily go to the park habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Walk",
    "description": "Daily walk habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Football",
    "description": "Daily football habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Hand Stand / Pull Up / Pole Session",
    "description": "Daily hand stand / pull up / pole session habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "7 Minute HIIT",
    "description": "Daily 7 minute hiit habit",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Matcha",
    "description": "Daily drink matcha habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Consume Leaves",
    "description": "Daily consume leaves habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Coconut Water",
    "description": "Daily drink coconut water habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Supplements",
    "description": "Daily take supplements habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Have Fruits",
    "description": "Daily have fruits habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Water",
    "description": "Daily drink water habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink Vegetable Juice",
    "description": "Daily drink vegetable juice habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prepare Meal / Cook Dinner",
    "description": "Daily prepare meal / cook dinner habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Take Chia Seeds",
    "description": "Daily take chia seeds habit",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Mantra Chanting",
    "description": "Daily mantra chanting habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Get Aligned High Income Job Offers",
    "description": "Daily get aligned high income job offers habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Optimise Linkedin",
    "description": "Daily optimise linkedin habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "AI Projects",
    "description": "Daily ai projects habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Passion Projects",
    "description": "Daily passion projects habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Upskill",
    "description": "Daily upskill habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Create Content",
    "description": "Daily create content habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Go To The Office",
    "description": "Daily go to the office habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Chanting",
    "description": "Daily chanting habit",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journal",
    "description": "Daily journal habit",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Meditate",
    "description": "Daily meditate habit",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Grounding",
    "description": "Daily grounding habit",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Sleep Well / Binaural Beats",
    "description": "Daily sleep well / binaural beats habit",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Attend an Event",
    "description": "Daily attend an event habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Hackathons",
    "description": "Daily hackathons habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Social Club Meet",
    "description": "Daily social club meet habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Community Service",
    "description": "Daily community service habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Visit Orphanage/ Old Age Home",
    "description": "Daily visit orphanage/ old age home habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Music Jam",
    "description": "Daily music jam habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Painitng, Gardening, Sketch",
    "description": "Daily painitng, gardening, sketch habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Declutter / Organise",
    "description": "Daily declutter / organise habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Planning for Tomorrow",
    "description": "Daily planning for tomorrow habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Feed The Dogs",
    "description": "Daily feed the dogs habit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Study fintech",
    "description": "Increase knowledge base",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read 30 minutes",
    "description": "Read books or articles",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Morning workout",
    "description": "30 minutes exercise",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink 8 glasses water",
    "description": "Stay hydrated",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Track expenses",
    "description": "Log daily spending",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Meditation",
    "description": "10 minutes mindfulness",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Play guitar",
    "description": "Practice music",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym workout",
    "description": "Weight training session",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink water",
    "description": "Stay hydrated throughout day",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Track investments",
    "description": "Monitor portfolio",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Meditation",
    "description": "15 minutes mindfulness",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Coding practice",
    "description": "Work on side projects",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read business books",
    "description": "Business and leadership books",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Running",
    "description": "Daily run or jog",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Eat healthy meals",
    "description": "Balanced nutrition",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Save money",
    "description": "Daily savings habit",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prayer time",
    "description": "Daily prayers",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Photography",
    "description": "Take photos and edit",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read 30 minutes",
    "description": "Read books or articles",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Morning workout",
    "description": "30 minutes exercise",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Morning workout",
    "description": "30 minutes exercise",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink 8 glasses water",
    "description": "Stay hydrated",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Drink 8 glasses water",
    "description": "Stay hydrated",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Track expenses",
    "description": "Log daily spending",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Track expenses",
    "description": "Log daily spending",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Meditation",
    "description": "10 minutes mindfulness",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Play guitar",
    "description": "Practice music",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Play guitar",
    "description": "Practice music",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read tech blogs",
    "description": "Read technology articles",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read tech blogs",
    "description": "Read technology articles",
    "category": "Reading",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym workout",
    "description": "Weight training session",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Gym workout",
    "description": "Weight training session",
    "category": "Fitness",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Eat healthy meals",
    "description": "Balanced nutrition",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Eat healthy meals",
    "description": "Balanced nutrition",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Save money",
    "description": "Daily savings habit",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Save money",
    "description": "Daily savings habit",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prayer time",
    "description": "Daily prayers",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Prayer time",
    "description": "Daily prayers",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Photography",
    "description": "Take photos and edit",
    "category": "Fun",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Photography",
    "description": "Take photos and edit",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Read business books",
    "description": "Business and leadership books",
    "category": "Reading",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Running",
    "description": "Daily run or jog",
    "category": "Fitness",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Running",
    "description": "Daily run or jog",
    "category": "Fitness",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Protein intake",
    "description": "Track protein consumption",
    "category": "Nutrition",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Protein intake",
    "description": "Track protein consumption",
    "category": "Nutrition",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Protein intake",
    "description": "Track protein consumption",
    "category": "Nutrition",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Investment research",
    "description": "Study market trends",
    "category": "Wealth",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Investment research",
    "description": "Study market trends",
    "category": "Wealth",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Investment research",
    "description": "Study market trends",
    "category": "Wealth",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journaling",
    "description": "Write daily thoughts",
    "category": "Spiritual",
    "user": "Sid",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journaling",
    "description": "Write daily thoughts",
    "category": "Spiritual",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Journaling",
    "description": "Write daily thoughts",
    "category": "Spiritual",
    "user": "Sanju",
    "start_date": "2025-07-15"
  },
  {
    "name": "Coding practice",
    "description": "Work on side projects",
    "category": "Fun",
    "user": "Shruti",
    "start_date": "2025-07-15"
  },
  {
    "name": "Coding practice",
    "description": "Work on side projects",
    "category": "Fun",
    "user": "Sanju",
    "start_date": "2025-07-15"
  }
]

HABIT_DAYS_DATA = [
  {
    "habit": "Fiction",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Spiritual",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Swim",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Run",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Consume Leaves",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Take Supplements",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "AI Projects",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Upskill",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Journal",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Grounding",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Social Club Meet",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Visit Orphanage/ Old Age Home",
    "user": "Shruti",
    "date": "2025-07-13",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Walk",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Hand Stand / Pull Up / Pole Session",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Have Fruits",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Drink Vegetable Juice",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Get Aligned High Income Job Offers",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "AI Projects",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Community Service",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Music Jam",
    "user": "Sid",
    "date": "2025-07-14",
    "completed": true,
    "day": 0
  },
  {
    "habit": "Community Service",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Social Club Meet",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Social Club Meet",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Hackathons",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Music Jam",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Drink Coconut Water",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Declutter / Organise",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Visit Orphanage/ Old Age Home",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Spiritual",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Play guitar",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Drink Coconut Water",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Sleep Well / Binaural Beats",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Run",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Football",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Drink Vegetable Juice",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Play guitar",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Mantra Chanting",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Passion Projects",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Gym",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Run",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Painitng, Gardening, Sketch",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Drink Water",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Go To The Office",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Create Content",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Attend an Event",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Dance",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Get Aligned High Income Job Offers",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Passion Projects",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Gym",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Go To The Park",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Study fintech",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Feed The Dogs",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Swim",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Drink 8 glasses water",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Prepare Meal / Cook Dinner",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Attend an Event",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Prepare Meal / Cook Dinner",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Go To The Park",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Attend an Event",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Grounding",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Take Chia Seeds",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Save money",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Hackathons",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Drink Matcha",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Drink Vegetable Juice",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Drink Water",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Have Fruits",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Hackathons",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Create Content",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Football",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Gym workout",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Investment research",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Drink Coconut Water",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Grounding",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Play guitar",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Gym workout",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Drink Coconut Water",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Music Jam",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Grounding",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Journal",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Mantra Chanting",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Music Jam",
    "user": "Sid",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Football",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Sleep Well / Binaural Beats",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 1
  },
  {
    "habit": "Sleep Well / Binaural Beats",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Attend an Event",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Planning for Tomorrow",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Read tech blogs",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Read tech blogs",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "7 Minute HIIT",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Save money",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Planning for Tomorrow",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Swim",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Community Service",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Drink Matcha",
    "user": "Shruti",
    "date": "2025-07-20",
    "completed": true,
    "day": 4
  },
  {
    "habit": "Drink Water",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Painitng, Gardening, Sketch",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Drink Coconut Water",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 2
  },
  {
    "habit": "Painitng, Gardening, Sketch",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Go To The Park",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Drink 8 glasses water",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Planning for Tomorrow",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 3
  },
  {
    "habit": "Social Club Meet",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Run",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Gym workout",
    "user": "Sanju",
    "date": "2025-07-20",
    "completed": true,
    "day": 5
  },
  {
    "habit": "Spiritual",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Run",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Dance",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Take Chia Seeds",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Drink water",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Mantra Chanting",
    "user": "Sid",
    "date": "2025-08-02",
    "completed": true,
    "day": 19
  },
  {
    "habit": "Fiction",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Non-Fiction",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Spiritual",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Swim",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Run",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Dance",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Go To The Park",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Walk",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Football",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Have Fruits",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Drink Water",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Drink Vegetable Juice",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Mantra Chanting",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Optimise Linkedin",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Passion Projects",
    "user": "Sid",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Fiction",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Swim",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Drink Matcha",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Consume Leaves",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Mantra Chanting",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Get Aligned High Income Job Offers",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Grounding",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
  },
  {
    "habit": "Social Club Meet",
    "user": "Sanju",
    "date": "2025-08-29",
    "completed": true,
    "day": 46
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
            user = User.objects.get(username=habit_data['user'])
            category = Category.objects.get(name=habit_data['category']) if habit_data['category'] else None
            
            habit, created = Habit.objects.get_or_create(
                name=habit_data['name'],
                user=user,
                defaults={
                    'description': habit_data['description'],
                    'category': category
                }
            )
            
            if created:
                print(f"  ✅ Created habit: {habit.name} for {user.username}")
            else:
                print(f"  ℹ️  Habit already exists: {habit.name} for {user.username}")
                
        except User.DoesNotExist:
            print(f"  ❌ User not found: {habit_data['user']}")
        except Category.DoesNotExist:
            print(f"  ❌ Category not found: {habit_data['category']}")

def import_habit_days():
    """Import habit completion records"""
    print("📥 Importing habit completion records...")
    
    imported_count = 0
    for habit_day_data in HABIT_DAYS_DATA:
        try:
            habit = Habit.objects.get(name=habit_day_data['habit'])
            date = datetime.fromisoformat(habit_day_data['date']).date()
            
            habit_day, created = HabitDay.objects.get_or_create(
                habit=habit,
                date=date,
                defaults={
                    'completed': habit_day_data['completed']
                }
            )
            
            if created:
                imported_count += 1
                
        except Habit.DoesNotExist:
            print(f"  ❌ Habit not found: {habit_day_data['habit']}")
    
    print(f"  ✅ Imported {imported_count} habit completion records")

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
        
        print("🎉 Data import completed successfully!")
        print("\n📊 Summary:")
        print(f"  Users: {len(USERS_DATA)}")
        print(f"  Categories: {len(CATEGORIES_DATA)}")
        print(f"  Habits: {len(HABITS_DATA)}")
        print(f"  Habit Days: {len(HABIT_DAYS_DATA)}")
        
    except Exception as e:
        print(f"❌ Error during import: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
