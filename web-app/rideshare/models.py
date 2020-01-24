import datetime
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    user_name = models.CharField(max_length = 100)
    user_type = models.CharField(max_length = 100)
    user_special = models.CharField(max_length = 500)
    user_share = models.BooleanField(default = False)
    
    vehicle_plate = models.CharField(max_length = 100)
    vehicle_type = models.CharField(max_length = 100)
    vehicle_capacity = models.IntegerField(default = 0)
    vehicle_special = models.CharField(max_length = 500)
    
    def  __str__(self):
        return self.user_name

class Ride(models.Model):
    status = models.CharField(max_length = 100)
    dest = models.CharField(max_length = 100)
    arrival = models.DateTimeField()

    num_passenger = models.IntegerField(default = 0)
    sharable = models.BooleanField(default = False)
    user_special = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_request")
    vehicle_special = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "vehicle_request")

    driver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name = "driver")
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name = "owner")
    sharer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name = "sharer")

    passenger_list = ArrayField(models.CharField(max_length = 100))

