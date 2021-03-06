from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

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
    return render(request, 'blog/post_edit.html', {'form': form})

def projekt(request):
    return render(request, 'blog/projekt.html',)

def subory(request):
    return render(request, 'blog/subory.html',)

def foto(request):
    return render(request, 'blog/foto.html',)

def video(request):
    return render(request, 'blog/video.html',)

def post_list_en(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list_en.html', {'posts': posts})

def post_detail_en(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail_en.html', {'post': post})

def projekt_en(request):
    return render(request, 'blog/projekt_en.html',)

def subory_en(request):
    return render(request, 'blog/subory_en.html',)

def foto_en(request):
    return render(request, 'blog/foto_en.html',)

def video_en(request):
    return render(request, 'blog/video_en.html',)