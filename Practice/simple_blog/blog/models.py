import datetime as dt

from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(null=True, blank=True)
    short_content = models.TextField(max_length=600)
    content = models.TextField()
    published_at = models.DateTimeField(default=dt.datetime.utcnow)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show', kwargs={"slug": self.slug})
