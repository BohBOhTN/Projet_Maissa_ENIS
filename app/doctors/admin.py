# doctors/admin.py
from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'location', 'latitude', 'longitude')
    search_fields = ('first_name', 'last_name', 'email', 'location')

# Register the model in the admin panel
admin.site.register(Doctor)
