from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

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
    
    top_level_comments = post.comments.filter(parent_comment__isnull=True)
    comment_form = CommentCreateForm()
    
    context = {
        'post': post,
        'comment_form': comment_form,
        'top_level_comments': top_level_comments,
        
        # Boolean value to determine whether show the replies in a single comment
        'show_replies': True, 
    }
    
    return render(request, 'a_posts/post_page.html', context)


@login_required
def comment_sent(request, pp_pk, cp_pk=None):
    post = get_object_or_404(Post, id=pp_pk)
    parent_comment = get_object_or_404(Comment, id=cp_pk) if cp_pk else None
    
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.parent_comment = parent_comment
            comment.save()
    
    return redirect('post-page', post.id)


@login_required
def comment_delete(request, pk):
    validate_uuid(pk)
    comment = get_object_or_404(Comment, id=pk, author=request.user)
    parent_post_id = comment.parent_post.id
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('post-page', parent_post_id)
    
    context = {
        'comment': comment,
        'show_replies': False,
    }
    return render(request, 'a_posts/comment_delete.html', context)


def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    user_exist = post.likes.filter(username=request.user.username).exists()
    
    if post.author != request.user:
        if user_exist:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    
    context = {
        'post': post,
    }    
    
    return render(request, 'snippets/likes.html', context)