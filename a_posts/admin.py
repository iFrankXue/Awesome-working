from django.contrib import admin

from .models import Post, Tag, Comment
# from .forms import CommentAdminForm


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)

