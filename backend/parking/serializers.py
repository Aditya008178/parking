from rest_framework import serializers
from .models import ParkingSpace

class ParkingSpaceSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ParkingSpace
        fields = '__all__'
        read_only_fields = ['owner', 'created_at'] 