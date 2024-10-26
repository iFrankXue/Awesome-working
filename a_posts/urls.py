from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home_view, name='home'),
    path('posts/create/', post_create_view, name='post-create'),
    path('posts/delete/<str:pk>', post_delete_view, name='post-delete'),
    path('posts/edit/<str:pk>/', post_edit_view, name='post-edit'),
    path('posts/<str:pk>/', post_page_view, name='post-page'),
    
    path('category/<str:tag>/', home_view, name='category-view'),
    
    
    # path('comment/sent/<str:pp_pk>/<str:cp_pk>/', comment_sent, name='comment-sent'),
    
    # URL pattern for a top-level comment (no parent comment)
    path('comment/sent/<uuid:pp_pk>/', comment_sent, name='comment-sent-top'),
    
    # URL pattern for a reply to a specific comment
    path('comment/sent/<uuid:pp_pk>/<uuid:cp_pk>/', comment_sent, name='comment-sent-reply'),

    path('comment/delete/<str:pk>/', comment_delete, name='comment-delete')
    
]

