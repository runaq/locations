from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list') 
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list') 
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
