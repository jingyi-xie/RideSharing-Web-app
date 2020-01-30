from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import app_user, app_ride
from django.views.generic import CreateView, ListView, DetailView, UpdateView


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

def profile_view(request):
    return render(request, 'rideshare/profile.html')
"""
def driver_info_view(request):
    if request.method == "POST":
        form = DriverInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully saved driver information')
            return redirect('rideshare:profile')
    else:
        form = DriverInfoForm
    return render(request, 'rideshare/driver_info.html', {'form': form})
"""
"""
class driver_info_view(LoginRequiredMixin, UpdateView):
    model = app_user
    fields = ['vehicle_plate', 'vehicle_type','vehicle_capacity', 'vehicle_special']
    template_name = 'rideshare/driver_info.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.will_drive = True
        return super().form_valid(form)

    def test_func(self):
        appuser = self.get_object()
        if self.request.user == appuser:
            return True
        return False
  """      

class ride_detail_view(LoginRequiredMixin, DetailView):
    model = app_ride

class ride_request_view(LoginRequiredMixin, CreateView):
    model = app_ride
    fields = ['dest', 'arrival','sharable', 'v_type', 'user_special']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 'open'
        return super().form_valid(form)

class ride_edit_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = app_ride
    fields = ['dest', 'arrival','sharable', 'v_type', 'user_special']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.owner:
            return True
        return False

class ride_confirm_view(LoginRequiredMixin, UpdateView):
    model = app_ride
    fields = []
    template_name = 'rideshare/app_ride_confirm.html'
    def form_valid(self, form):
        form.instance.status = 'confirmed'
        form.instance.driver = self.request.user
        return super().form_valid(form)
    
    """
    Don't delete!

    def test_func(self):
        ride = self.get_object()
        if self.request.user.will_drive == True:
            return True
        return False
    """