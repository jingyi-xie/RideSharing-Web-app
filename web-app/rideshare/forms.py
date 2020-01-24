from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Owner:
        model = User
        fields = [
            'destination',
        ]
