from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="auth/login/")
def ssh(request):
    return render(request, 'ssh.html')
