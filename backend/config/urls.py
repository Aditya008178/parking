from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', lambda request: HttpResponse("Backend Running ✅")),
    path('admin/', admin.site.urls),

    path('api/users/', include('accounts.urls')),
    path('api/parking/', include('parking.urls')),
    path('api/bookings/', include('bookings.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]