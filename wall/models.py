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

	def __str__(self):
		return self.title
