import datetime

from django.db import models
from django.utils import timezone

class Emotion(models.Model):
	emotion = models.CharField(max_length=15)

	def __str__(self):
		return self.emotion

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	feel = models.ForeignKey(Emotion, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Opinion(models.Model):
	opinion = models.CharField(max_length=3)

	def __str__(self):
		return self.opinion

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
