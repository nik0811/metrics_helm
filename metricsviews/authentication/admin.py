# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.contrib import admin
from authentication.models.company import *

admin.site.register(CompanyProfile, CompanyProfileAdmin)
