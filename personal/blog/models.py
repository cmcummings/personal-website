from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True)

class Article(models.Model):
    title = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
