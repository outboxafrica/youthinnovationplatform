from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from YouthInnovPltfrm import settings

from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    username = models.CharField(unique=False, max_length=150)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='static/profile_images',
        blank=True,
        default=settings.STATIC_URL + 'img/user-placeholder.png'
    )
    website = models.URLField(null=True, blank=True)
    blog = models.URLField(null=True, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    summary = models.TextField()
    age = models.IntegerField(blank=True, default=20)
    timestamp = models.DateTimeField(auto_now=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=timezone.now())
    role = models.CharField(max_length=50, null=True)
    """
    check whether a user has created a company, community hub or innovation profile
    """
    has_created_entity = models.BooleanField(default=False)

    def get_picture(self):
            try:
                return "" + self.picture.url
            except:
                return settings.STATIC_URL + 'img/user-placeholder.png'

    def __str__(self):
        return self.get_full_name()

    REQUIRED_FIELDS = [email]


class Mentor(User):
    competencies = models.CharField(max_length=255, blank=True)
    support_stage = models.CharField(max_length=255)
    support_type = models.TextField()
    experience = models.TextField()


class Investor(User):
    resume = models.FileField(upload_to='static/uploads/%Y/%m/%d/', blank=True)


class Innovator(User):
    experience = models.TextField()


class ProgramManager(User):
    program = models.CharField(max_length=100, null=True, blank=True)


class HubManager(User):
    has_hub = models.BooleanField(default=False)







