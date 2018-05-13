from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Emotion
from .forms import PostForm, CommentForm, UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'wall/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'wall/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method=="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'wall/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'wall/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('create_date')
	return render(request, 'wall/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(reuqest, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')

def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'wall/add_comment_to_post.html', {'form': form})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			#username = form.cleaned_data.get('username')
			#raw_password = form.cleaned_data.get('password')
			#user = authenticate(username=username, password=raw_password,backend='django.contrib.auth.backends.ModelBackend')
			login(request, new_user)
			return redirect('post_list')
	else :
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})
