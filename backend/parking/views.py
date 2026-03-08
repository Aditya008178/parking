from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import ParkingSpace
from .serializers import ParkingSpaceSerializer

class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all().order_by('-created_at')
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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