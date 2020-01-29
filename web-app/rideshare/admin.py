from django.contrib import admin
from .models import app_user, app_ride, app_passenger
# Register your models here.

admin.site.register(app_user)
admin.site.register(app_ride)
admin.site.register(app_passenger)