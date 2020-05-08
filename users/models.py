
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

from .managers import CustomUserManager

    
class UserProfile(AbstractUser):

    is_professor = models.BooleanField(default=False)
    is_site_admin = models.BooleanField(default=False)

    objects = CustomUserManager()