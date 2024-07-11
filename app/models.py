from django.db import models
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    description = models.TextField()
    date_pub = models.DateTimeField(default=timezone.now)


# Create your models here.
