from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from bs4 import BeautifulSoup
import requests

from .models import Post, Tag, Comment
from .forms import PostCreateForm, PostEditForm, CommentCreateForm
from .utils import validate_uuid
# Create your views here.

def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
    
    categories = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag,
    }
    return render(request, 'a_posts/home.html', context)


@login_required
def post_create_view(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data['url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')

            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com"]')
            image = find_image[0]['content']
            post.image = image
            
            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist
            
            post.author = request.user
            
            post.save()
            form.save_m2m()
            return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, 'a_posts/post_create.html', context)


@login_required
def post_delete_view(request,pk):
    validate_uuid(pk)
    post = get_object_or_404(Post, id=pk, author=request.user)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
    
    context = {
        'post': post,
    }
    return render(request, 'a_posts/post_delete.html', context)


@login_required
def post_edit_view(request, pk):
    validate_uuid(pk)
    post = get_object_or_404(Post, id=pk, author=request.user)
    
    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully!')
            return redirect('home')
    else:
        form = PostEditForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'a_posts/post_edit.html', context)


def post_page_view(request, pk):
    validate_uuid(pk)    
    post = get_object_or_404(Post, id=pk)
    
    comment_form = CommentCreateForm()

    context = {
        'post': post,
        'comment_form': comment_form,
    }
    
    return render(request, 'a_posts/post_page.html', context)


@login_required
def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()
    
    return redirect('post-page', post.id)


@login_required
def comment_delete(request, pk):
    validate_uuid(pk)
    comment = get_object_or_404(Comment, id=pk, author=request.user)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('post-page', comment.parent_post.id)
    
    context = {
        'comment': comment
    }
    return render(request, 'a_posts/comment_delete.html', context)



def get_comments(request):
    post_id = request.GET.get('post_id')
    comments = Comment.objects.filter(parent_post_id=post_id).values('id', 'body')
    return JsonResponse({'comments': list(comments)})