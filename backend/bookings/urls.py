from django.urls import path
from .views import BookingListCreateView, ConfirmPaymentView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
    path('confirm-payment/<int:pk>/', ConfirmPaymentView.as_view(), name='confirm-payment'),
]