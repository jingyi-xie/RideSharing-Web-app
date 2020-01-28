from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Ride
from django.views.generic import CreateView, ListView, DetailView

def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Sign Up!')
            return redirect('rideshare:login')
    else:
        form = UserSignupForm
    return render(request, 'rideshare/signup.html', {'form': form})

@login_required
def ride_request_view(CreateView):
    """
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    return render(request, "rideshare/profile.html", {'form': form})
    """
    model = Ride
    fields = ['dest']
