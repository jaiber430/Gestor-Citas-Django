from django.contrib.auth.models import AbstractUser
from django.db import models

# Abstractuser brings default fields
class User(AbstractUser):
    # CharField => varchar (Text)
    phone = models.CharField(
        # Maximum characters
        max_length=15,
        # Allow null in the form
        blank=True,
        # Allow null in the DB
        null=True
    )
    # True or False field
    is_verified = models.BooleanField(
        # False start
        default=False
    )

    class Meta:
        # Table name
        db_table = 'users'

    def __str__(self):
        # see name
        return f'{self.first_name} {self.last_name}'

# models.Model identify as database table
class Role(models.Model):
    role_name = models.CharField(
        max_length=15,
    )

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.role_name

class Post(models.Model):
    cargo_type = models.CharField(
        max_length = 100
    )
    # TextField a lot of text
    description = models.TextField(
        blank = True,
        null = True
    )

    class Meta:
        db_table='post'

    def __str__(self):
        return self.cargo_type

class UserRole(models.Model):
    user=models.ForeignKey(
        User,
        # on_delete CASCADE user is delete, their roles are deleted
        on_delete=models.CASCADE,
        # related_name user roles or vice versa (Get roles for this user)
        related_name='user_roles'
    )
    role=models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        # Get users with this role
        related_name='role_users'
    )

    class Meta:
        db_table = 'user_role'
        # A user cannot have the same role twice
        unique_together = ('user', 'role')

    def __str__(self):
        return f'{self.user} - {self.role}'
