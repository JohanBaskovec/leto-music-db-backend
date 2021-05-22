from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.OneToOneField(User, null=False, blank=False, on_delete=models.DO_NOTHING)
