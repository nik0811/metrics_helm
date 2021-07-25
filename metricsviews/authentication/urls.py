# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.urls import path
from authentication.views.auth import login_view, register_user, passwordChange, sendActivationEmail, activate, verification
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    #path('api-token-auth/', auth_views.obtain_auth_token)
    # Forget password or reset password
    path('password/change/', passwordChange, name="password-change"),
    path('email/send-email-activation', sendActivationEmail, name='send-activation-email'),
    path('verify/<uidb64>/<token>/', activate, name='verify'),
    #path('verification/', verification, name='email_verification')
]
