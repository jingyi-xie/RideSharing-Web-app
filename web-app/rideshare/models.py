import datetime
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
"""
class User(models.Model):
    user_name = models.CharField(max_length = 100)
    user_type = models.CharField()
    user_special = models.CharField()
    user_share = models.BooleanField()
    
    vehicle_plate = models.CharField()
    vehicle_type = models.CharField()
    vehicle_capacity = models.IntegerField()
    vehicle_special = models.CharField()
    
    def  __str__(self):
        return self.user_name

class Ride(models.Model):
    status = models.CharField()
    dest = models.CharField()
    arrival = models.DateTimeField()

    num_passenger = models.IntegerField()
    sharable = models.BooleanField()
    user_special = models.ForeignKey(User)
    vehicle_special = models.ForeignKey(User)

    driver = models.ForeignKey(User)
    owner = models.ForeignKey(User)
    sharer = models.ForeignKey(User)

    passenger_list = ArrayField(models.CharField())
"""
