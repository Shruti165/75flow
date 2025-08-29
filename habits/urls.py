from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('', views.home, name='home'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('daily-tracking/', views.daily_tracking, name='daily_tracking'),
    path('excel/', views.excel_view, name='excel'),
    path('admin-habit-manager/', views.admin_habit_manager, name='admin_habit_manager'),
    path('add-participant/', views.add_participant, name='add_participant'),
    path('toggle-habit/<int:habit_id>/', views.toggle_habit, name='toggle_habit'),
    path('category/create/', views.create_category, name='create_category'),
    path('habit/create/', views.create_habit, name='create_habit'),
    path('habit/<int:habit_id>/edit/', views.edit_habit, name='edit_habit'),
    path('habit/<int:habit_id>/delete/', views.delete_habit, name='delete_habit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
] 