from django.contrib import admin
from .models import Emotion, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Emotion)
