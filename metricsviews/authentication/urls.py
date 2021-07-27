# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.urls import path, re_path
from authentication.views.auth import login_view, register_user, passwordChange, sendActivationEmail, activate, verification
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    re_path(r'^login/', login_view, name="login"),
    re_path(r'^register/', register_user, name="register"),
    re_path(r'^logout/', LogoutView.as_view(), name="logout"),
    #path('api-token-auth/', auth_views.obtain_auth_token)
    # Forget password or reset password
    re_path(r'^password/change/', passwordChange, name="password-change"),
    re_path(r'^email/', sendActivationEmail, name='send-activation-email'),
    re_path(r'^verify/<uidb64>/<token>/', activate, name='verify'),
    #path('verification/', verification, name='email_verification')
]
