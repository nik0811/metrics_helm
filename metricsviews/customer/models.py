from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class Customer(User):
    objects = UserManager()
