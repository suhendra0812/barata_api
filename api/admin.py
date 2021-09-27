from django.contrib import admin

# Register your models here.
from .models import Satellite, Sensor, Beam, Planning

admin.site.register(Satellite)
admin.site.register(Sensor)
admin.site.register(Beam)
admin.site.register(Planning)