from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from rideshare.views import signup_view, ride_request_view

app_name = 'rideshare'
urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rideshare/logout.html'), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name='rideshare/login.html'), name = 'login'),
    path('riderequest/', ride_request_view, name = 'riderequest'),
]
