from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('', views.home, name='home'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('daily-tracking/', views.daily_tracking, name='daily_tracking'),
    path('admin-habit-manager/', views.admin_habit_manager, name='admin_habit_manager'),
    path('toggle-habit/<int:habit_id>/', views.toggle_habit, name='toggle_habit'),
    path('category/create/', views.create_category, name='create_category'),
    path('habit/create/', views.create_habit, name='create_habit'),
    path('habit/edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('habit/delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
] 