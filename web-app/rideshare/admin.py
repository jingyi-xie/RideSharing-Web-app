from django.contrib import admin
from .models import app_user, app_ride
# Register your models here.

admin.site.register(app_user)
admin.site.register(app_ride)
