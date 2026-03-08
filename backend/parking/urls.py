from django.urls import path
from .views import ParkingSpaceListCreateView, ParkingSpaceDetailView, MyParkingSpaceView

urlpatterns = [
    path('', ParkingSpaceListCreateView.as_view(), name='parking-list-create'),
    path('my/', MyParkingSpaceView.as_view(), name='my-parking'),
    path('<int:pk>/', ParkingSpaceDetailView.as_view(), name='parking-detail'),
]