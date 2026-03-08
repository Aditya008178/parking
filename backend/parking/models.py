from django.db import models
from django.conf import settings

class ParkingSpace(models.Model):
    VEHICLE_CHOICES = (
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('suv', 'SUV'),
    )

    PARKING_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    parking_type = models.CharField(max_length=20, choices=PARKING_TYPE_CHOICES)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title