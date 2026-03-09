from django.contrib import admin
from .models import ParkingSpace

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'owner', 'is_approved', 'available_slots']
    list_filter = ['is_approved', 'parking_type', 'vehicle_type']
    search_fields = ['title', 'location', 'area']