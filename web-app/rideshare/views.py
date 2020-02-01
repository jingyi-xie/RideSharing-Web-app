from django.shortcuts import render, redirect
from .forms import UserSignupForm, DriverInfoForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import app_user, app_ride, app_passenger
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.db.models import Q


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

@login_required
def driver_info_view(request):
    if request.method == "POST":
        form = DriverInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.instance.will_drive = True
            form.save()
            messages.success(request, f'Driver information updated!')
            return redirect('rideshare:profile')

    else:
        form = DriverInfoForm(instance=request.user)

    return render(request, 'rideshare/driver_info.html', {'form': form}) 

@login_required
def profile_update_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account profile updated!')
            return redirect('rideshare:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'rideshare/driver_info.html', {'form': form}) 

class ride_detail_view(LoginRequiredMixin, DetailView):
    model = app_ride

class ride_request_view(LoginRequiredMixin, CreateView):
    model = app_ride
    fields = ['dest', 'arrival','sharable', 'v_type', 'num_passenger', 'user_special']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.request.remaining = self.request.user.vehicle_capacity - form.instance.num_passenger
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

def ride_list_view(request):
    context = {
        'rides' : app_ride.objects.all()
    }
    return render(request, 'rideshare/app_ride_list.html', context)

"""
class ride_list_view(ListView):
    model = app_ride
    context_object_name = 'rides'
    template_name = 'rideshare/app_ride_list.html'
"""

class ride_join_view(LoginRequiredMixin, CreateView):
    model = app_passenger
    fields = ['party_size']
    def form_valid(self, form):
        form.instance.passenger = self.request.user
        form.instance.ride_id = app_ride.objects.get(pk=self.kwargs.get('pk'))
        app_ride.objects.get(pk=self.kwargs.get('pk')).remaining -= form.instance.party_size
        return super().form_valid(form)

def ridesearch_sharer_view(request):
    qs = app_ride.objects.all()
    dest_query = request.GET.get('dest')
    early = request.GET.get('early')
    late = request.GET.get('late')
    party = request.GET.get('num_passenger')
    if dest_query != '' and dest_query:
        qs = qs.filter(Q(dest = dest_query) &
                        Q(arrival__gte = early) &
                        Q(arrival__lt = late) &
                        Q(remaining__gte = num_passenger)
        )
    context = {
        'queryset' : qs
    }
    return render(request, "rideshare/ridesearch_sharer.html", context)