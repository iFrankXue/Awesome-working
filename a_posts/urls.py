from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home_view, name='home'),
    path('create/', post_create_view, name='post-create'),
    path('delete/<str:pk>', post_delete_view, name='post-delete'),
    path('edit/<str:pk>/', post_edit_view, name='post-edit'),
    path('<str:pk>/', post_page_view, name='post-page'),
    
    path('category/<str:tag>/', home_view, name='category-view'),
    
]