from django.urls import path
from .views import (
    ParkingSpaceListCreateView,
    ParkingSpaceDetailView,
    MyParkingSpaceView,
    PendingParkingApprovalView,
    ApproveParkingView
)

urlpatterns = [
    path('', ParkingSpaceListCreateView.as_view(), name='parking-list-create'),
    path('my/', MyParkingSpaceView.as_view(), name='my-parking'),
    path('pending/', PendingParkingApprovalView.as_view(), name='pending-parking'),
    path('approve/<int:pk>/', ApproveParkingView.as_view(), name='approve-parking'),
    path('<int:pk>/', ParkingSpaceDetailView.as_view(), name='parking-detail'),
]