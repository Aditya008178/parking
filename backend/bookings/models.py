from django.db import models
from django.conf import settings
from parking.models import ParkingSpace
import uuid

class Booking(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('wallet', 'Wallet'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, related_name='bookings')
    vehicle_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='upi')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='paid')
    booking_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    qr_data = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.booking_code:
            self.booking_code = f"BK-{uuid.uuid4().hex[:8].upper()}"
        if not self.qr_data:
            self.qr_data = f"BOOKING:{self.booking_code}|VEHICLE:{self.vehicle_number}|PARKING:{self.parking_space_id}|DATE:{self.date}|TIME:{self.time}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} - {self.booking_code}"