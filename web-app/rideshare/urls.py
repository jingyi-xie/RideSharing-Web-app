from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from rideshare.views import signup_view, profile_view, ride_request_view, ride_detail_view, ride_edit_view, ride_confirm_view, driver_info_view, profile_update_view, ride_list_view, ride_join_view, ridesearch_sharer_view, ride_complete_view, ride_list_view_driver,ridesearch_driver_view

app_name = 'rideshare'
urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rideshare/logout.html'), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name='rideshare/login.html'), name = 'login'),
    path('profile/', profile_view, name = 'profile'),
    path('profile/update/', profile_update_view, name = 'profileupdate'),
    path('ride/<int:pk>/', ride_detail_view.as_view(), name = 'ridedetail'),
    path('ride/<int:pk>/edit/', ride_edit_view.as_view(), name = 'rideedit'),
    path('ride/<int:pk>/confirm/', ride_confirm_view.as_view(), name = 'rideconfirm'),
    path('ride/<int:pk>/join/', ride_join_view.as_view(), name = 'ridejoin'),
    path('ride/<int:pk>/complete/', ride_complete_view.as_view(), name = 'ridecomplete'),
    path('ride/request/', ride_request_view.as_view(), name = 'riderequest'),
    path('ride/all/', ride_list_view.as_view(), name = 'ridelist'),
    path('ride/joinsearch/', ridesearch_sharer_view, name = 'ridesearchsharer'),
    path('driver/info/', driver_info_view, name = 'driverinfo'),
    path('driver/confirm/', ridesearch_driver_view, name = 'ridesearchdriver'),
    path('driver/complete/', ride_list_view_driver.as_view(), name = 'drivercomplete'),
]
