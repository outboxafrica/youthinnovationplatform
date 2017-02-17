from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from YouthInnovPltfrm import settings

from projects.models import InvestmentCompany, CommunityHub, Innovation

from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='static/profile_images',
        blank=True,
        default=settings.STATIC_URL + 'img/user-placeholder.png'
    )
    linkedin = models.URLField()
    blog = models.URLField()
    linkedin = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    summary = models.TextField()
    age = models.IntegerField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_picture(self):
            try:
                return "/" + self.picture.url
            except:
                return "/"

    def __str__(self):
        return self.get_full_name()

    REQUIRED_FIELDS = [email, gender, country]


class Mentor(models.Model):
    user = models.OneToOneField(User)
    competencies = models.CharField(max_length=255, blank=True)
    support_stage = models.CharField(max_length=255)
    support_type = models.TextField()
    experience = models.TextField()


class Investor(models.Model):
    user = models.OneToOneField(User)
    resume = models.FileField(upload_to='static/uploads/%Y/%m/%d/', blank=True)
    company = models.ForeignKey(InvestmentCompany)  # to the investment company table


class Innovator(models.Model):
    user = models.OneToOneField(User)
    experience = models.TextField()
    team = models.ForeignKey(Innovation)  # to the innovation table


class ProgramManager(models.Model):
    user = models.OneToOneField(User)


class HubManager(models.Model):
    user = models.OneToOneField(User)
    hub = models.ForeignKey(CommunityHub)  # to the community hub table





