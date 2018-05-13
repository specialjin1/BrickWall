from django import forms

from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('feel','title', 'text',)

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('opinion','text',)

class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('username','password','email',)
