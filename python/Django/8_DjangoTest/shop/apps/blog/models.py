from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_lenght=30)
    family = models.CharField(max_lenght=30)
    slug = models.SlugField(max_lenght=100)
    age = models.IntegerField(default=20)
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_lenght=100)