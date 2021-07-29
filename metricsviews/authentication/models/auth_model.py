from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import uuid


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    email_verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    """
    profile = UserProfile.objects.first()           
    """

    def __str__(self):
        return str(self.user.username)


class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
