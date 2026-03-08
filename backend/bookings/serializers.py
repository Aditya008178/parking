from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    customer_username = serializers.ReadOnlyField(source='customer.username')
    parking_title = serializers.ReadOnlyField(source='parking_space.title')

    class Meta:
        model = Booking
        fields = ['id', 'customer', 'customer_username', 'parking_space', 'parking_title', 'date', 'time', 'created_at']
        read_only_fields = ['customer', 'created_at']