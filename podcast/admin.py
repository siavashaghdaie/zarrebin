from django.contrib import admin

# Register your models here.
from .models import Podcaster,Podcast

admin.site.register(Podcast)
admin.site.register(Podcaster)
