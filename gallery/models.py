from django.db import models
from django.conf import settings
from django.utils import timezone




class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.title