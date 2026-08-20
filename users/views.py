from rest_framework import viewsets
from users.models import (User, Role, Post, UserRole, Schedule, DoctorSpecialty)
from users.serializers import (UserSerializer, RoleSerializer, PostSerializer, UserRoleSerializer, ScheduleSerializer, DoctorSpecialtySerializer)
from users.permissions import (IsAdmin, isDoctor, IsPatient)

# ModelViewSet => All http methods
class UserViewSet(viewsets.ModelViewSet):
    # Data handled by the view
    queryset = User.objects.all()
    # Convert data to Json
    serializer_class = UserSerializer
    # Role-based permissions
    permission_classes = [IsAdmin]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdmin]


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAdmin]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    #  DRF calls this method to determine which permissions to apply
    def get_permissions(self):
        #  self.action => Detect the GET action or actions
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAdmin | IsDoctor | IsPatient]
        else:
            # self.action => Detect the POST, PUT, DELETE action
            permissions_classes= [IsAdmin]

        return [permissions() for permision in permission_classes]

class DoctorSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DoctorSpecialtySerializer
    permission_classes = [IsAdmin | isDoctor]
