# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""
from django.contrib import admin

# Register your models here.

from authentication.models.auth_model import UserProfile, UserProfileAdmin

admin.site.register(UserProfile, UserProfileAdmin)
