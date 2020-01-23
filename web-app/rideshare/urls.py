from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'rideshare'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
]
