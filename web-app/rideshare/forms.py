from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import app_user
class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = app_user
        fields = ['username', 'email', 'password1', 'password2']
"""
class DriverInfoForm(forms.ModelForm):
    class Meta:
        model = app_user
        fields = ['vehicle_plate', 'vehicle_type','vehicle_capacity', 'vehicle_special']
"""
class UserForm(forms.Form):
    user_name = forms.CharField(label = 'User Name')
    user_special = forms.CharField(label = 'Special Request', required = False, widget=forms.Textarea())

