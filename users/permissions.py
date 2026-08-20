# BasePermission => DFR base class for custom permissions
from rest_framework.permissions import BasePermission
from .models import (UserRole)

class IsAdmin(BasePermission):
    #  Method that DRF class automatically access verification (True or False)
    def has_permission(self, request, view):
        return UserRole.objects.filter(
            # request.user => User making the request (Django extracts it from the JWT)
            user=request.user,
            # Double underscore search for related method
            role__role_name='admin'
        ).exists()

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return UserRole.objects.filter(
            user=request.user,
            role__role_name='doctor'
        ).exists()

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return UserRole.objects.filter(
            user=request.user,
            role__role_name='patient'
        ).exists()
