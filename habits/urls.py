from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('', views.home, name='home'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('daily-tracking/', views.daily_tracking, name='daily_tracking'),
    path('admin-habit-manager/', views.admin_habit_manager, name='admin_habit_manager'),
    path('toggle-habit/<int:habit_id>/', views.toggle_habit, name='toggle_habit'),
    path('category/create/', views.create_category, name='create_category'),
    path('habit/create/', views.create_habit, name='create_habit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
] 