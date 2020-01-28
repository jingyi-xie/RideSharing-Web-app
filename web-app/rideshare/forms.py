from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import app_user, app_ride

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RequestRideForm(forms.Form):
    class Meta:
        model = app_ride
    #user_name = app_user.user_name
    user_special = forms.CharField(label = 'Special Request', required = False, widget=forms.Textarea())
