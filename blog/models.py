from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    publish = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
   

    def get_absolute_url(self):
        return reverse("detail", kwargs={"year": self.publish.year,
                                         "slug": self.slug})

   