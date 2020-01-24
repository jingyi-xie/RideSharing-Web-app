from django.shortcuts import render

from .forms import UserForm
from .models import User

def owner_create_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, "rideshare/profile.html", context)

def loggedout_view(request):
    return render(request, "rideshare/loggedout.html")
