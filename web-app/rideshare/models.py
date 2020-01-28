import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class app_user(models.Model):
    user_name = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "username")
    will_drive = models.BooleanField(default = False)
    vehicle_plate = models.CharField(max_length = 100)
    vehicle_type = models.CharField(max_length = 100)
    vehicle_capacity = models.IntegerField(default = 4)
    vehicle_special = models.CharField(max_length = 500)
    
    def  __str__(self):
        return self.user_name

class app_ride(models.Model):
    status = models.CharField(max_length = 100)
    dest = models.CharField(max_length = 100)
    arrival = models.DateTimeField()

    num_passenger = models.IntegerField(default = 0)
    sharable = models.BooleanField(default = False)
    user_special = models.CharField(max_length = 500, blank = True)

    driver = models.ForeignKey(app_user, null=True, blank=True, on_delete=models.SET_NULL, related_name = "driver")
    owner = models.ForeignKey(app_user, null=True, blank=True, on_delete=models.SET_NULL, related_name = "owner")

    passenger_list = ArrayField(models.CharField(max_length = 100))

