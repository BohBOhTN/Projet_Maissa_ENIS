from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255)  # City or region
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # GPS latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # GPS longitude

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.location})"
