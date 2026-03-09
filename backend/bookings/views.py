from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from parking.models import ParkingSpace

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        parking_id = request.data.get('parking_space')

        try:
            parking_space = ParkingSpace.objects.get(id=parking_id, is_approved=True)
        except ParkingSpace.DoesNotExist:
            return Response({"error": "Parking space not found or not approved."}, status=status.HTTP_400_BAD_REQUEST)

        if not parking_space.is_available or parking_space.available_slots <= 0:
            return Response({"error": "No slots available."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        booking = serializer.save(customer=request.user, payment_status='pending')

        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class ConfirmPaymentView(generics.UpdateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()

    def update(self, request, *args, **kwargs):
        booking = self.get_object()

        if booking.customer != request.user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        if booking.payment_status != 'paid':
            booking.payment_status = 'paid'
            parking_space = booking.parking_space
            parking_space.available_slots -= 1
            if parking_space.available_slots <= 0:
                parking_space.available_slots = 0
                parking_space.is_available = False
            parking_space.save()
            booking.save()

        return Response(BookingSerializer(booking).data)