from django.db import models
from django.contrib.auth.models import User
import uuid


class Post(models.Model):
    # id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likedposts', through='LikedPost')
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']
        
        
class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.post.title}'


class Tag(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    # image = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        
        
        
class Comment(models.Model):
    # id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  # Self-referential field
    likes = models.ManyToManyField(User, related_name='likedcomments', through='LikedComment')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        try:
            return f'{self.author.username}: {self.body[:30]}'
        except:
            return f'no author: {self.body[:30]}'
        
    class Meta:
        ordering = ['-created']
     
    @property   
    def total_replies_count(self):
        # Count direct replies
        reply_count = self.replies.count()
        
        # Recursively add counts of replies to each reply
        for reply in self.replies.all():
            reply_count += reply.total_replies_count
        
        return reply_count

class LikedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.comment.body[:30]}'