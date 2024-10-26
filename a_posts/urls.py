from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home_view, name='home'),
    path('posts/create/', post_create_view, name='post-create'),
    path('posts/delete/<str:pk>', post_delete_view, name='post-delete'),
    path('posts/edit/<str:pk>/', post_edit_view, name='post-edit'),
    path('posts/<str:pk>/', post_page_view, name='post-page'),
    
    path('category/<str:tag>/', home_view, name='category-view'),
    path('comment/sent/<str:pk>/', comment_sent, name='comment-sent'),
    path('comment/delete/<str:pk>/', comment_delete, name='comment-delete')
    
]



# urlpatterns = [
#     # Other URL patterns...
#     path('admin/get-comments/', get_comments, name='get_comments'),
# ]