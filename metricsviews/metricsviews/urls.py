# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.contrib import admin
from django.urls import path, include, re_path  # add this
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('authentication.urls')),
    path('api/view/', include("cluster.urls")),
    path('schema/', get_schema_view(
        title="Metricsviews",
        description="API for the Mumble.dev",
        version="1.0.0"
    ), name="metricsviews-schema"),
    path('', include_docs_urls(
        title="MetricsviewsAPI",
        description="API for the Metricsviews.com",
    ), name="metricsviews-docs")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
