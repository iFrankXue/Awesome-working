from django.template import Library
from django.db.models import Count, Sum
from ..models import Post, Tag, Comment

register = Library()

@register.inclusion_tag('includes/sidebar.html')
def sidebar_view(tag=None, user=None):
    categories = Tag.objects.all()
    # top_posts = Post.objects.annotate(top_points=Sum('likes__count')+Sum('comments__count')).filter(top_points__gt=0).order_by('-top_points')[:5]
    # top_comments = Comment.objects.annotate(top_points=Sum('likes__count')+Sum('replies__count')).filter(top_points__gt=0).order_by('-top_points')[:5]
    
    top_posts = Post.objects.annotate(top_points=Count('likes')+Count('comments')).filter(top_points__gt=0).order_by('-top_points')[:5]
    top_comments = Comment.objects.annotate(top_points=Count('likes')+Count('replies')).filter(top_points__gt=0).order_by('-top_points')[:5]
    
    context = {
        'categories': categories,
        'top_posts': top_posts,
        'top_comments': top_comments,
        'tag': tag,
        'user': user,
    }
    
    return context