from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from rideshare.views import signup_view, profile_view, ride_request_view, ride_detail_view, ride_edit_view, ride_confirm_view

app_name = 'rideshare'
urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rideshare/logout.html'), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name='rideshare/login.html'), name = 'login'),
    path('profile', profile_view, name = 'profile'),
    path('ride/<int:pk>/', ride_detail_view.as_view(), name = 'ridedetail'),
    path('ride/<int:pk>/edit', ride_edit_view.as_view(), name = 'rideedit'),
    path('ride/<int:pk>/confirm', ride_confirm_view.as_view(), name = 'rideconfirm'),
    path('ride/request/', ride_request_view.as_view(), name = 'riderequest'),
]
