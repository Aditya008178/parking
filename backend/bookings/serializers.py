from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):

    parking_title = serializers.CharField(source='parking_space.title', read_only=True)
    parking_location = serializers.CharField(source='parking_space.location', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'parking_space',
            'parking_title',
            'parking_location',
            'vehicle_number',
            'date',
            'time',
            'payment_method',
            'payment_status',
            'booking_code',
            'qr_data'
        ]