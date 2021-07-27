# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Metricsviews.com
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from authentication.forms import LoginForm, SignUpForm, CompanyProfileForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                messages.error(request, 'Invalid Credentials, Reset Password?')    
        else:
            messages.error(request, 'Login Validation Failed')    

    return render(request, "login.html", {"form": form})

def register_user(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = CompanyProfileForm(request.POST)
        print(profile_form.is_valid())
        print(form)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            messages.success(request, 'User created - ' + username)
            
            return redirect("/login/")

        else:
             messages.error(request, 'Form is not valid')    
    else:
        form = SignUpForm()
        profile_form = CompanyProfileForm()
    context = {"form": form, 'profile_form': profile_form}
    return render(request, "accounts/register.html", context)

# THIS EMAIL VERIFICATION SYSTEM IS ONLY VALID FOR LOCAL TESTING
# IN PRODUCTION WE NEED A REAL EMAIL , TILL NOW WE ARE USING DEFAULT EMAIL BACKEND
# THIS DEFAULT BACKEND WILL PRINT THE VERIFICATION EMAIL IN THE CONSOLE 
# LATER WE CAN SETUP SMTP FOR REAL EMAIL SENDING TO USER

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def sendActivationEmail(request):
    user = request.user
    user_profile = CompanyProfile.objects.get(user=user)
    try:
        mail_subject = 'Verify your Metricsviews account.'
        message = render_to_string('verify-email.html', {
            'user': user_profile,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = user.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        print("Email Sent")
        return Response('Mail sent Successfully',status=status.HTTP_200_OK)
    except Exception as e:
        return Response('Something went wrong , please try again',status=status.HTTP_403_FORBIDDEN)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def verification(request):
    return render(request, "verification.html")

@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user_profile = CompanyProfile.objects.get(user=user)
        user_profile.email_verified = True
        user_profile.save()
        return Response("Email Verified")
    else:
        return Response('Something went wrong , please try again',status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def passwordChange(request):
    user = request.user
    data = request.data
    new_password = data.get('new_password')
    new_password_confirm = data.get('new_password_confirm')
    if new_password_confirm and new_password is not None:
        if new_password == new_password_confirm:
            user.set_password(new_password)
            user.save()
            return Response({'detail':'Password changed successfully'},status=status.HTTP_200_OK)
        else:
            return Response({"detail":'Password doesn\'t match'})
    elif new_password is None:
        return Response({'detail':'New password field required'})
    elif new_password_confirm is None:
        return Response({'detail':'New password confirm field required'})
