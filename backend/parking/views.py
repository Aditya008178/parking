from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import ParkingSpace
from .serializers import ParkingSpaceSerializer

class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = ParkingSpace.objects.all().order_by('-created_at')
        location = self.request.query_params.get('location')

        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ParkingSpaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

class MyParkingSpaceView(generics.ListAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ParkingSpace.objects.filter(owner=self.request.user).order_by('-created_at')