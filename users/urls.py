"""users/urls.py"""
from django.urls import path
# ~ from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('singup/', views.singup, name='singup'),
]
