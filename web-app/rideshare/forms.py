from django import forms

from .models import User


class UserForm(forms.Form):
    user_name = forms.CharField(label = 'User Name')
    user_special = forms.CharField(label = 'Special Request', required = False, widget=forms.Textarea())
"""
class SignUpForm(forms.UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
"""
