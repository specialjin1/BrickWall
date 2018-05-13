from django.utils import timezone
from django.contrib import admin
from .models import Emotion, Post, Opinion, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('feel', 'title', 'was_published')
	list_filter = ['published_date','feel']
	actions = ['make_published']

	def make_published(self, request, queryset):
		updated_count = queryset.update(published_date=timezone.now())
		self.message_user(request, '{}건의 포스팅을 Publish'.format(updated_count))
	make_published.short_description = '지정 포스팅을 Publish'

admin.site.register(Post, PostAdmin)
admin.site.register(Emotion)
admin.site.register(Comment)
admin.site.register(Opinion)
