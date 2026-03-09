from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import ParkingSpace
from .serializers import ParkingSpaceSerializer

class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = ParkingSpace.objects.filter(is_approved=True).order_by('-created_at')

        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, is_approved=False)

class ParkingSpaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

class MyParkingSpaceView(generics.ListAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ParkingSpace.objects.filter(owner=self.request.user).order_by('-created_at')

class PendingParkingApprovalView(generics.ListAPIView):
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ParkingSpace.objects.filter(is_approved=False).order_by('-created_at')

class ApproveParkingView(generics.UpdateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(is_approved=True)