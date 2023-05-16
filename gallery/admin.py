from django.contrib import admin
from .models import Image

admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
# Register your models here.

