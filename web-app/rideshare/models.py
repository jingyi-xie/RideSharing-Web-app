import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class app_user(AbstractUser):
    #user_name = models.OneToOneField(LoginUser, on_delete=models.CASCADE, related_name="user_name")
    user_name = models.CharField(max_length = 100)
    will_drive = models.BooleanField(default = False)
    vehicle_plate = models.CharField(max_length = 100)
    vehicle_type = models.CharField(max_length = 100)
    vehicle_capacity = models.IntegerField(default = 4)
    vehicle_special = models.CharField(max_length = 500)

"""
    def  __str__(self):
        return self.user_name
   """ 
class app_ride(models.Model):
    status = models.CharField(max_length = 100)
    dest = models.CharField(max_length = 100)
    arrival = models.DateTimeField(default = timezone.now, null = False)

    num_passenger = models.IntegerField(default = 0)
    sharable = models.BooleanField(default = False)
    v_type = models.CharField(max_length = 500, blank = True)
    user_special = models.CharField(max_length = 500, blank = True)

    driver = models.ForeignKey(app_user, null = True, blank=True, on_delete = models.CASCADE, related_name = "driver")
    owner = models.ForeignKey(app_user, null = True, blank=True, on_delete = models.CASCADE, related_name = "owner")
    remaining = models.IntegerField(default = 4)
    #passenger_list = ArrayField(models.CharField(max_length = 100))

    def get_absolute_url(self):
        return reverse('rideshare:ridedetail', kwargs={'pk': self.pk})

class app_passenger(models.Model):
    ride_id = models.ForeignKey(app_ride, null = False, blank = True, on_delete = models.CASCADE, related_name = "rideid")
    passenger = models.ForeignKey(app_user, null = True, blank = True, on_delete = models.SET_NULL, related_name = "passenger")
    party_size = models.IntegerField(default = 0)
    def get_absolute_url(self):
        return reverse('rideshare:ridelist')