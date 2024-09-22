from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True, null=True, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    # Add related_name to resolve conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.email

class EmailVerification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Email verification for {self.user.email}"

    def is_valid(self):
        return timezone.now() <= self.expires_at

class GoogleOAuth2Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    expires_at = models.DateTimeField()
