from django.contrib import admin

# Register your models here.

from cluster.models.socket import LoggedInUser

admin.site.register(LoggedInUser)
