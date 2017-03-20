from __future__ import unicode_literals

from django.db import models
from eventtools.models import BaseEvent, BaseOccurrence
from cloudinary.models import CloudinaryField
# Create your models here.


class Event(BaseEvent):
    title = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    event_pic = CloudinaryField('image')
    introduction = models.TextField(blank=True)
    objectives = models.TextField(blank=True)
    target = models.TextField(blank=True)
    facilitators = models.TextField(blank=True)
    registration_link = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title


class Occurrence(BaseOccurrence):
    event = models.ForeignKey(Event)