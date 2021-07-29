# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""
from django.urls import path
from authentication.views import auth

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'authentication-api'

urlpatterns = [

    path('register/', auth.RegisterView.as_view(), name='register'),
    path('login/', auth.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),


    path('profile_update/', auth.UserProfileUpdate.as_view(), name="profile_update"), 
    path('profile_update/photo/', auth.ProfilePictureUpdate.as_view(), name="profile_update_photo"), 

    path('<str:username>/', auth.user, name="user"),

    # Forget password or reset password
    path('password/change/',auth.passwordChange,name="password-change"),
    # path('password/reset/',views.passwordReset,name="password-reset"),

    # email verification urls
    path('email/send-email-activation',auth.sendActivationEmail,name='send-activation-email'),
    path('verify/<uidb64>/<token>/',auth.activate, name='verify'),
]
