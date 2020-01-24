from django.shortcuts import render

from .forms import UserForm
from .models import User

def owner_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "rideshare/profile.html", context)


