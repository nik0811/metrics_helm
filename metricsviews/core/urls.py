# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin route
    path('', include("authentication.urls")),  # Auth routes - login / register
    path('', include("app.urls")),             # UI Html files
    path('', include("nodes.urls"))            # nodes api
]
