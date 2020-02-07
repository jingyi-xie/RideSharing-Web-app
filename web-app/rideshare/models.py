import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

class app_user(AbstractUser):
    #user_name = models.OneToOneField(LoginUser, on_delete=models.CASCADE, related_name="user_name")
    user_name = models.CharField(max_length = 100, verbose_name = 'Your Name')
    will_drive = models.BooleanField(default = False)
    vehicle_plate = models.CharField(max_length = 100, verbose_name = 'Vehicle Plate Number')
    vehicle_type = models.CharField(max_length = 100, verbose_name = 'Vehicle Type')
    vehicle_capacity = models.IntegerField(default = 4, verbose_name = 'Vehicle Capacity')
    vehicle_special = models.CharField(max_length = 500, verbose_name = 'Vehicle Special Information')
"""
    def  __str__(self):
        return self.user_name
"""
class app_ride(models.Model):
    status = models.CharField(max_length = 100)
    dest = models.CharField(max_length = 100, verbose_name = 'Destination')
    arrival = models.DateTimeField(default = timezone.now, null = False, verbose_name = 'Arrival Time')

    num_passenger = models.IntegerField(default = 1, verbose_name = 'Number of Passengers', validators=[MinValueValidator(1)])
    sharable = models.BooleanField(default = False, verbose_name = 'Share?')
    v_type = models.CharField(max_length = 500, blank = True, verbose_name = 'Vehicle Type')
    user_special = models.CharField(max_length = 500, blank = True, verbose_name = 'Special Request')

    driver = models.ForeignKey(app_user, null = True, blank=True, on_delete = models.CASCADE, related_name = "driver")
    owner = models.ForeignKey(app_user, null = True, blank=True, on_delete = models.CASCADE, related_name = "owner")
    remaining = models.IntegerField(default = 4)
    #passenger_list = ArrayField(models.CharField(max_length = 100))

    def get_absolute_url(self):
        return reverse('rideshare:ridedetail', kwargs={'pk': self.pk})

    def  __str__(self):
        return self.dest
         
class app_passenger(models.Model):
    ride_id = models.ForeignKey(app_ride, null = False, blank = True, on_delete = models.CASCADE, related_name = "rideid")
    passenger = models.ForeignKey(app_user, null = True, blank = True, on_delete = models.SET_NULL, related_name = "passenger")
    party_size = models.IntegerField(default = 0, verbose_name = 'Number of Passengers')
    def get_absolute_url(self):
        return reverse('rideshare:ridelist')