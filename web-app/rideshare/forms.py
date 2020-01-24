from django import forms

from .models import User

class UserForm(forms.Form):
    user_special = forms.CharField(label = 'Special Request', widget=forms.Textarea())
