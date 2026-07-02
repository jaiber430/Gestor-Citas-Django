from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import (UserViewSet, RoleViewSet, PostViewSet, UserRoleViewSet, ScheduleViewSet, DoctorSpecialtyViewSet)

router = DefaultRouter()

# genera → /api/users/
router.register('users', UserViewSet)

router.register('roles', RoleViewSet)

router.register('posts', PostViewSet)

router.register('user-roles', UserRoleViewSet)

router.register('schedules', ScheduleViewSet)

router.register('doctor-specialties', DoctorSpecialtyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
