from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import uuid

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.username

class CompanyProfileAdmin(admin.ModelAdmin):
    readonly_fields=('company_id',)
