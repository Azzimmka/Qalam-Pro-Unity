from django.db import models
from django.utils import timezone
from django.urls import reverse
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug':self.slug})

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    description = models.TextField()
    full_info = models.TextField(null=True)
    date_pub = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='categories')


    def __str__(self):
        return self.title
# Create your models here.
