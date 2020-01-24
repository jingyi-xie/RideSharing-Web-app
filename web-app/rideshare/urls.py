from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from rideshare.views import owner_create_view, loggedout_view

app_name = 'rideshare'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('loggedout/', loggedout_view, name = 'loggedout'),
    path('profile/', owner_create_view, name = 'profile'),
]
