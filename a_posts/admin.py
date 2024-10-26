from django.contrib import admin

from .models import Post, Tag, Comment
# from .forms import CommentAdminForm


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)


# class CommentAdmin(admin.ModelAdmin):
#     form = CommentAdminForm
#     list_display = ['author', 'parent_post', 'body', 'created']
    
#     class Media:
#         js = ('js/admin_dynamic_comment.js',)  # Path to the custom JavaScript file

# admin.site.register(Comment, CommentAdmin)