from rest_framework import serializers
from user.models import User, Role, Post, UserRole, Schedule, DoctorSpecialty

class UserSerializer(serializers.ModelSerializer):
    # write_only => receive data but never return it
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Fields => Include specific fields
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_verified', 'password']

    def create(self, validated_data):
        # created_user => Automatically hash the passsword
        user = User.objects.create_user(**validated_data)
        # **validate_datad => Unpack dictionary as named arguments
        return user

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    # Display all nested object data
    user = UserSerializer(read_only=True)
    # Use read_only mode to prevent submitting existing data
    role = RoleSerializer(read_only=True)

    class Meta:
        model = UserRole
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):

    post = PostSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'

class DoctorSpecialtySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = DoctorSpecialty
        fields = '__all__'
