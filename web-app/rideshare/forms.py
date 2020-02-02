from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import app_user
class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = app_user
        fields = ['username', 'email', 'password1', 'password2']

class DriverInfoForm(forms.ModelForm):
    class Meta:
        model = app_user
        fields = ['user_name','vehicle_plate', 'vehicle_type','vehicle_capacity', 'vehicle_special']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = app_user
        fields = ['email']

