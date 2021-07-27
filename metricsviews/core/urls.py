# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin route
    re_path(r'^', include('home.urls')),
    path('auth/', include("authentication.urls")),  # Auth routes - login / register
    #path('', include("nodes.urls"))            # nodes api
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
