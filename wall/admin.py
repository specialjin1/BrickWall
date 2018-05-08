from django.contrib import admin
from .models import Emotion, Post, Opinion, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Emotion)
admin.site.register(Comment)
admin.site.register(Opinion)
