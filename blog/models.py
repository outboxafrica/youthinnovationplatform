from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from users.models import User
# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='title', unique_with='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    blog_pic = CloudinaryField('image')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_date',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

