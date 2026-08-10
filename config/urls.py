from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/appointments/', include('appointments.urls')),

    # Create token
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Renew token
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
