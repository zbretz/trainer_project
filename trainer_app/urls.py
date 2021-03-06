from django.urls import path
from trainer_app import views

app_name = 'trainer_app'

urlpatterns = [
    path('current_workout/', views.current_workout, name='current_workout'),
    path('last_workout', views.last_workout, name='last_workout'),
    path('complete', views.workout_complete, name='workout_complete'),    
    path('', views.home, name='home'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('time_check', views.time_check, name='time_check'),
    path('log_workout_time', views.log_workout_time, name='log_workout_time'),
    path('trainer_portal', views.trainer_portal, name='trainer_portal'),

]