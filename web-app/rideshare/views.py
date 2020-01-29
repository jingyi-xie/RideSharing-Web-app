from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import app_user, app_ride
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

class ride_request_view(CreateView):
    model = app_ride
    fields = ['dest', 'arrival','sharable', 'v_type', 'user_special']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)