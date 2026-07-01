from rest_framework import viewsets
from users.models import User, Role, Post, UserRole, Schedule, DoctorSpecialty
from users.serializers import UserSerializer, RoleSerializer, PostSerializer, UserRoleSerializer, ScheduleSerializer, DoctorSpecialtySerializer

# Create your views here.

# ModelViewSet => All http methods
class UserViewSet(viewsets.ModelViewSet):
    # Data handled by the view
    queryset = User.objects.all()
    # Convert data to Json
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class DoctorSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer
